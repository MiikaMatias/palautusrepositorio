import unittest

from matchers import All, Not, And, HasAtLeast, HasFewerThan, PlaysIn

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


    def test_len(self):
        url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
        reader = PlayerReader(url)
        stats = Statistics(reader)


        filtered_with_all = stats.matches(All())
        self.assertEqual(1058, len(filtered_with_all))