import unittest

from matchers import All, Or, Not, And, HasAtLeast, HasFewerThan, PlaysIn
from query import Query

from statistics import Statistics
from player_reader import PlayerReader

class TestMatchers(unittest.TestCase):
        
    def test_at_least_fewer_than(self):

        url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
        reader = PlayerReader(url)
        stats = Statistics(reader)


        matcher1 = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
        )

        matcher2 = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
        )

        self.assertEqual(stats.matches(matcher1), stats.matches(matcher2))


    def test_or(self):
        url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
        reader = PlayerReader(url)
        stats = Statistics(reader)


        matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
        )

        self.assertEqual(9, len(stats.matches(matcher)))

        matcher = And(
            HasAtLeast(70, "points"),
            Or(
                PlaysIn("NYR"),
                PlaysIn("FLA"),
                PlaysIn("BOS")
            )
        )

        self.assertEqual(8, len(stats.matches(matcher)))



    def test_len(self):
        url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
        reader = PlayerReader(url)
        stats = Statistics(reader)


        filtered_with_all = stats.matches(All())
        self.assertEqual(1058, len(filtered_with_all))

    
    def test_builder(self):
        url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
        reader = PlayerReader(url)
        stats = Statistics(reader)

        matcher = (Query()
                   .playsIn("NYR")
                   .hasAtLeast(10, "goals")
                   .hasFewerThan(20, "goals")
                   .build())
        
        self.assertEqual(5, len(stats.matches(matcher)))

        url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
        reader = PlayerReader(url)
        stats = Statistics(reader)

        m1 = (
        Query()
            .playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build()
        )

        m2 = (
        Query()
            .playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
        )

        matcher = Query().oneOf(m1, m2).build()
    
        self.assertEqual(8, len(stats.matches(matcher)))



