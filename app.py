
from flask import Flask, render_template, request
from models.scorelist import ScoreList

app = Flask(__name__)

@app.route("/score_id", methods=['GET'])
@app.route("/")
def home():
    scores = ScoreList()
    return render_template("home.html", scores=scores.scores)

@app.route("/score_info/<string:score_id>", methods=['GET'])
def score_info(score_id):
    print(score_id)
    scores = ScoreList()
    score = scores.get_score(score_id)
    print(score)
    return render_template("view_score.html", score_data=score)


@app.route("/submitscore", methods=['POST'])
def submitscore():
    if request.method == 'POST':
        print(request)
        print(request.data)
        scores = ScoreList()
        score_info = request.json
        scores.add_to_json(score_info)
        return "Success!", 200

if __name__ == "__main__":
    app.run(debug=True)
