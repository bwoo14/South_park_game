import json

class User:
    def __init__(self, user_id, username, password, scores=None) -> None:
        self.user_id = user_id
        self.username = username
        self.password = password
        if scores != None:
            self.scores = scores
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
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'scores': [score.to_dict() for score in self.scores]
        }