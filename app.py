
from flask import Flask, render_template, request, url_for
from models.score import Score
from models.user_database import UserDatabase
import os
from flask_login import login_user, current_user, logout_user, login_required
# from forms import LoginForm

app = Flask(__name__)

# @app.route("/score_id", methods=['GET'])

# @app.route("/")
# def index():
#     form = LoginForm()
#     return render_template("login.html")

@app.route("/")
def home():
    """
    This is the home page of the website
    """
    database = UserDatabase()
    scores = database.get_scores()
    return render_template("home.html", scores=scores)

@app.route("/score_info/<string:score_id>", methods=['GET'])
def score_info(score_id):
    """
    This is the page that shows the score information
    """
    database = UserDatabase()
    score = database.get_score(score_id)

    return render_template("view_score.html", score=score.to_dict())

@app.route("/view_user/<string:username>", methods=['GET'])
def view_user(username):
    """
    This is the page that shows the user information
    """
    database = UserDatabase()
    user = database.get_user(username)
    most_played_character = user.most_played_character()
    high_score = user.get_high_score()
    return render_template("view_user.html", user=user.to_dict(), mpc=most_played_character, hs = high_score)

@app.route("/submitscore", methods=['POST'])
def submitscore():
    """
    This is the page that submits the score
    """
    if request.method == 'POST':
        database = UserDatabase()
        req = request.json
        score_info = request.json['score']
        user = database.username_and_password(req['username'], req['password'])
        if user:
            score = Score(score_info['score_id'], score_info['username'], score_info['score'], score_info['time'], score_info['character'], score_info['date'])
            user.add_score(score)
            database.save_users()
            return "Score added", 200
        return "Username or Password Incorrect", 200

if __name__ == "__main__":
    app.run(debug=True)
