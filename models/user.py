import json
from models.score import Score

class User:
    def __init__(self, username, password, scores=None) -> None:
        self.username = username
        self.password = password
        if scores != None:
            self.scores = []
            for score in scores:
                self.scores.append(Score(score['score_id'], score['username'], score['score'], score['time'], score['character'], score['date']))
        else:
            self.scores = []

    def add_score(self, score):
        self.scores.append(score)
    
    def delete_score(self, score_id):
        for score in self.scores:
            if score.score_id == score_id:
                self.scores.remove(score)
                return True
        return False
    
    def most_played_character(self):
        """
        This function returns the most played character
        """
        character_count = {}
        if len(self.scores) == 0:
            return 'cartman'
        for score in self.scores:
            if score.character in character_count:
                character_count[score.character] += 1
            else:
                character_count[score.character] = 1
        return max(character_count, key=character_count.get)

    def get_high_score(self):
        """
        This function returns the highest score
        """
        high_score = 0
        for score in self.scores:
            if score.score > high_score:
                high_score = score.score
        return high_score
    
    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'scores': [score.to_dict() for score in self.scores]
        }