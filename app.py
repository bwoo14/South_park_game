
from flask import Flask, render_template, request, url_for, redirect, flash, session
from models.score import Score
from models.user_database import UserDatabase
from datetime import timedelta
import os

from forms.login_form import LoginForm
from forms.resgister_form import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b88a7564a30c56d91df77da2c24c4433'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    This function handles the login page
    """
    if "user" in session:
        return redirect(url_for('home'))
    else:
        database = UserDatabase()
        form = LoginForm()
        if form.validate_on_submit():
            user = database.get_user(form.username.data)
            # Check if the user exists, and their password matches
            if user and user.password == form.password.data:
                flash(f'Welcome!', 'success')
                # puts user in the sesion
                session['user'] = user.username
                session.permanent = True
                return redirect(url_for('home'))
            flash(f'Incorrect Username or Password', 'danger')
        return render_template('login.html', title='login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    """
    This function handles the register page
    """
    database = UserDatabase()
    form = RegistrationForm()
    if form.validate_on_submit():
        
        # if user not in database, add user to database
        if not database.get_user(form.username.data):
            database.create_user(form.username.data, form.password.data)
            database.save_users()
            user = database.get_user(form.username.data)
            session['user'] = user.username
            session.permanent = True
            flash(f'Welcome!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Username already exists', 'danger')
    return render_template('register.html', title='Register', form=form)


@app.route("/home")
def home():
    """
    This is the home page of the website
    """
    if "user" in session:
        database = UserDatabase()
        scores = database.get_scores(sorted=True)
        return render_template("home.html", scores=scores)
    else:
        flash('Please login to view this page', 'danger')
        return redirect(url_for('login'))

@app.route("/score_info/<string:score_id>", methods=['GET'])
def score_info(score_id):
    """
    This is the page that shows the score information
    """
    if "user" in session:
        database = UserDatabase()
        score = database.get_score(score_id)

        return render_template("view_score.html", score=score.to_dict())
    else:
        flash('Please login to view this page', 'danger')
        return redirect(url_for('login'))

@app.route("/view_user/<string:username>", methods=['GET'])
def view_user(username):
    """
    This is the page that shows the user information
    """
    if "user" in session:
        database = UserDatabase()
        user = database.get_user(username)
        most_played_character = user.most_played_character()
        high_score = user.get_high_score()
        return render_template("view_user.html", user=user.to_dict(), mpc=most_played_character, hs = high_score)
    else:
        flash('Please login to view this page', 'danger')
        return redirect(url_for('login'))

@app.route("/submitscore", methods=['POST'])
def submitscore():
    """
    This is the page that submits the score
    """
    if request.method == 'POST':
        database = UserDatabase()
        req = request.json
        score_info = request.json['score']
        # checks if password and username are correct
        user = database.username_and_password(req['username'], req['password'])
        if user:
            score = Score(score_info['score_id'], score_info['username'], score_info['score'], score_info['time'], score_info['character'], score_info['date'])
            # adds score to database
            user.add_score(score)
            database.save_users()
            return "Score added", 200
        return "Username or Password Incorrect", 400

@app.route("/logout")
def logout():
    """
    This is the page that logs the user out
    """
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route("/delete_score/<string:username> /<string:score_id>", methods=['GET' , 'POST'])
def delete_score(score_id, username):
    """
    This is the page that deletes the score
    """
    if "user" in session:
        database = UserDatabase()
        # get the user
        user = database.get_user(username)
        # get the score
        user.delete_score(score_id)
        database.save_users()
        # redirect to the user page
        return redirect(url_for('view_user', username=username))
    else:
        flash('Please login to view this page', 'danger')
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=False)
