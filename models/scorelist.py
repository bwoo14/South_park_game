import json
class ScoreList:
    def __init__(self):
        self.load_from_json()
    def load_from_json(self):
        with open('scores/scores.json') as f:
            self.scores = json.load(f)

    def add_to_json(self, score_object):
        with open('scores/scores.json','r+') as file:
            file_data = json.load(file)
            file_data.append(score_object)
            file.seek(0)
            json.dump(file_data, file, indent = 4)

if __name__ == '__main__':
    s = ScoreList()
    print(s.scores)