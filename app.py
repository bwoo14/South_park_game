
from flask import Flask, render_template
from models.scorelist import ScoreList

app = Flask(__name__)

@app.route("/")
def home():
    scores = ScoreList()
    return render_template("home.html", scores=scores.scores)

if __name__ == "__main__":
    app.run(debug=True)