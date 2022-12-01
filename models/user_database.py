import json
from user import User

class UserDatabase:
    def __init__(self) -> None:
        self.filename = './data/users.json'
        self.users = []
        self.load_users()

    def load_users(self):
        with open(self.filename, 'r') as f:
            users = json.load(f)
            for user in users:
                self.users.append(User(user['user_id'], user['username'], user['password'], user['scores']))
        
    def create_user(self, username, password):
        user = User(len(self.users), username, password)
        self.users.append(user)

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def remove_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                return True
        return False

    def save_users(self):
        users = []
        for user in self.users:
            users.append(user.to_dict())
        with open(self.filename, 'w') as f:
            json.dump(users, f, indent=4)