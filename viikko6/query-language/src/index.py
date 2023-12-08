from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn
from query import Query

def main():
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
    
    for player in stats.matches(matcher):
        print(player)
if __name__ == "__main__":
    main()
