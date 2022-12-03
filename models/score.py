import json
class Score:
    def __init__(self, score_id, username, score, time, character, date) -> None:
        self.score_id = score_id
        self.username = username
        self.score = score
        self.time = time
        self.character = character
        self.date = date

    def to_dict(self):
        return {
            'score_id': self.score_id,
            'username': self.username,
            'score': self.score,
            'time': self.time,
            'character': self.character,
            'date': self.date
        }
           

# if __name__ == '__main__':
#     s = ScoreList()
#     print(s.get_score("fffffffffffffffffff"))