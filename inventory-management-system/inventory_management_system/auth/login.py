# login.py
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class AuthSystem:
    def __init__(self):
        self.users = {
            'admin': User('admin', 'adminpass', 'Admin'),
            'user': User('user', 'userpass', 'User')
        }

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        else:
            raise ValueError("Invalid username or password")
