import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_correct(self):
        self.assertEqual(str(self.stats.search("Semenko")), str(Player("Semenko", "EDM", 4, 12)))

    def test_search_incorrect(self):
        self.assertEqual(self.stats.search("Does not exist"), None)

    def test_team_correct(self):
        self.assertEqual(str(self.stats.team("PIT")[0]), str([Player("Lemieux", "PIT", 45, 54)][0]))

    def test_top(self): 
        self.assertEqual(str(self.stats.top(1)[0]), str([Player("Gretzky", "EDM", 35, 89)][0]))