import json
from models.user import User
import os
class UserDatabase:
    """
    a class for the database
    """
    def __init__(self) -> None:
        self.filename = os.path.abspath('./data/users.json')
        self.users = []
        self.load_users()

    def load_users(self):
        """
        Loads the users and their information from the json file
        """
        with open(self.filename, 'r') as f:
            users = json.load(f)
            for user in users:
                self.users.append(User(user['username'], user['password'], user['scores']))
        
    def create_user(self, username, password):
        """
        Creates a new user in the database
        """
        user = User(username, password)
        self.users.append(user)

    def get_user(self, username):
        """
        Returns a user object if the user exists in the database
        """
        for user in self.users:
            if user.username == username:
                return user
        return None

    def get_scores(self, sorted=False):
        """
        Returns a list of all scores in the database
        """
        scores = []
        for user in self.users:
            scores.extend(user.scores)
        if sorted:
            scores.sort(key=lambda x: x.score, reverse=True)
        return scores

    def get_score(self, score_id):
        """
        Returns a score object if the score exists in the database
        """
        for user in self.users:
            for score in user.scores:
                if score.score_id == score_id:
                    return score
        return None
    
    def username_and_password(self, username, password):
        """
        Returns a user object if the user exists in the database
        """
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def save_users(self):
        """
        Saves the users and their informatio to the json file
        """
        users = []
        for user in self.users:
            users.append(user.to_dict())
        with open(self.filename, 'w') as f:
            json.dump(users, f, indent=4)
    
    def login(self, username, password):
        """
        Returns a user object if the user exists in the database
        """
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def reload(self):
        """
        Reloads the users from the json file
        """
        self.users = []
        self.load_users()