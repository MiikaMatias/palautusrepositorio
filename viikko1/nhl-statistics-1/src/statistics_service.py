from player_reader import PlayerReader
from enum import Enum
from sortby import SortBy

def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists


class StatisticsService:
    def __init__(self, player_reader: PlayerReader):
        reader = player_reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, basis=SortBy(1)):
   
        sorting_method = sort_by_points if basis==SortBy.POINTS else sort_by_goals if basis==SortBy.GOALS else sort_by_assists if basis==SortBy.ASSISTS else sort_by_points

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sorting_method
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
