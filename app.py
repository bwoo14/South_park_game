
from flask import Flask, render_template, request, url_for
from models.score import Score
from models.user_database import UserDatabase
import os
from flask_login import login_user, current_user, logout_user, login_required
from forms import LoginForm

app = Flask(__name__)

# @app.route("/score_id", methods=['GET'])

@app.route("/")
def index():
    form = LoginForm()
    return render_template("login.html")

@app.route("/home")
def home():
    database = UserDatabase()
    scores = database.get_scores()
    return render_template("home.html", scores=scores.scores)

@app.route("/score_info/<string:score_id>", methods=['GET'])
def score_info(score_id):
    database = UserDatabase()
    score = database.get_score(score_id)

    return render_template("view_score.html", score=score.to_dict())


@app.route("/submitscore", methods=['POST'])
def submitscore():
    if request.method == 'POST':
        print(request)
        print(request.data)
        database = UserDatabase()
        score_info = request.json
        #scores.add_to_json(score_info)
        return "Success!", 200

if __name__ == "__main__":
    app.run(debug=True)
