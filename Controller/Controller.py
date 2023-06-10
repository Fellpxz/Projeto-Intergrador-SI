from Models.Model import UserModel
from Views.View import UserView

class UserController:
    def __init__(self):
        self.model = UserModel()
        self.view = UserView()

    def create_user(self):
        name, email = self.view.get_user_input()
        self.model.create_user(name, email)

    def show_users(self):
        users = self.model.get_users()
        self.view.show_users(users)