import json
class ScoreList:
    def __init__(self):
        self.load_from_json()
    def load_from_json(self):
        with open('scores/scores.json') as f:
            self.scores = json.load(f)


if __name__ == '__main__':
    s = ScoreList()
    print(s.scores)