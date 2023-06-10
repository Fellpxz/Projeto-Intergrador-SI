class UserModel:
    def __init__(self):
        self.users = []

    def create_user(self, name, email):
        user = {
            'name': name,
            'email': email
        }
        self.users.append(user)

    def get_users(self):
        return self.users