
from flask import Flask, render_template, request, url_for, redirect, flash
from models.score import Score
from models.user_database import UserDatabase
import os
from flask_login import login_user, current_user, logout_user, login_required

from forms.login_form import LoginForm
from forms.resgister_form import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b88a7564a30c56d91df77da2c24c4433'

# @app.route("/score_id", methods=['GET'])

@app.route("/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f' {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
# def login():
#     database = UserDatabase()
#     # if current_user.is_authenticated:
#     #    return redirect(url_for('home'))  # USE THE NAME OF THE FUNCTION NOT THE NAME OF THE HTML FILE, redirecting to homepage after register
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = database.get_user(form.username.data)
#         if user and user.password == form.password.data:  # Checking if the inputted password matches the actual password
#             login_user(user, remember=form.remember.data)
#             next_page = request.args.get('next')  # Redirects you to next page if you tried to access the page and were redirected to the login
#             return redirect(next_page) if next_page else redirect(url_for('home')) # check if next_page is safe
#         else: 
#             flash('Login Unsuccessful. Incorrect Username or Password', 'danger') # Shows failed login message using bootstrap class 'danger'
#     return render_template('login.html', title='Login', form=form)


@app.route("/home")
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
