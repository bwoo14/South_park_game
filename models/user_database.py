import json
from models.user import User

class UserDatabase:
    def __init__(self) -> None:
        self.filename = './data/users.json'
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
        user = User(len(self.users), username, password)
        self.users.append(user)

    def get_user(self, username):
        """
        Returns a user object if the user exists in the database
        """
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def remove_user(self, user_id):
        """
        Removes a user from the database
        """
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                return True
        return False

    def get_scores(self):
        """
        Returns a list of all scores in the database
        """
        scores = []
        for user in self.users:
            scores.extend(user.scores)
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