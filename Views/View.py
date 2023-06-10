class UserView:
    def show_users(self, users):
        print("Lista de usuários:")
        for user in users:
            print(f"Nome: {user['name']}, Email: {user['email']}")

    def get_user_input(self):
        name = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        return name, email
