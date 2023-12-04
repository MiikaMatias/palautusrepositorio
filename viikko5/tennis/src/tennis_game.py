class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

        self.tie_dict = {0:"Love-All", 1:"Fifteen-All", 2:"Thirty-All", 3:"Deuce", 4:"Deuce"}
        self.game_dict = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 +=1

    def get_tie_score(self):
        return self.tie_dict[self.m_score1]
    
    def get_leading_player(self, score):
        return "player2" if score < 0 else "player1"

    def get_overflow_score(self):
        minus_result = self.m_score1 - self. m_score2
        if abs(minus_result) >= 2:
            return f"Win for {self.get_leading_player(minus_result)}"
        else:
            return f"Advantage {self.get_leading_player(minus_result)}"
        
    def get_game_score(self):
        score = self.game_dict[self.m_score1] + "-" + self.game_dict[self.m_score2]
        return score

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_tie_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_overflow_score()
        else:
            return self.get_game_score()
