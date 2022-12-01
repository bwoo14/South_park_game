import json
from models.score import Score

class User:
    def __init__(self, username, password, scores=None) -> None:
        self.username = username
        self.password = password
        if scores != None:
            for score in scores:
                self.scores.append(Score(score['score_id'], score['score'], score['time'], score['character'], score['date']))
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
    
    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'scores': [score.to_dict() for score in self.scores]
        }