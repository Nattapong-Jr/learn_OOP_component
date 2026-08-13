class Usser:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def __str__(self):
        return f"User(ID:{self.user_id}, Username:{self.username}, Email:{self.email})"