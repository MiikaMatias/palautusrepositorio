import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.team = dict['team']
        self.games = dict['games']

        self.total = self.assists + self.goals

    def __str__(self):
        return f"{self.name:25} {self.team:5} {self.goals:4} + {self.assists:2} = {self.total}"

class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()

        self.players = []

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)



class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players_sorted = sorted(self.reader.players, key=lambda x: x.total, reverse=True)
        return list(filter(lambda x: x.nationality == nationality, players_sorted))