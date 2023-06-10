from Controller.Controller import UserController

controller = UserController()

while True:
    print("1. Cadastrar usuário")
    print("2. Mostrar usuários")
    print("3. Sair")

    choice = input("Digite a opção desejada: ")

    if choice == '1':
        controller.create_user()
    elif choice == '2':
        controller.show_users()
    elif choice == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")