import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Oliot:")

    players_sorted = sorted(players, key=lambda x: x.total, reverse=True)
    players_sorted = list(filter(lambda x: x.nationality == "FIN", players_sorted))

    for player in players_sorted:
        print(player)

if __name__ == "__main__":
    main()
