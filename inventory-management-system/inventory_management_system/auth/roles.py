# roles.py
class Roles:
    ADMIN = "Admin"
    USER = "User"

def is_admin(user):
    return user.role == Roles.ADMIN

def is_user(user):
    return user.role == Roles.USER
