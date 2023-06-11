from Controller.Controller import MainController

control = MainController()

while True:
    print("1. Testar conexão com a Database")
    print("2. Ver as Amostras do Database")
    print("3. Criar uma Amostra para o Database")

    choice = input("Digite a opção desejada: ")

    if choice == '1':
        print("")
        control.see_database_samples()

    elif choice == '2':
        print("")
        control.create_database_sample()

    elif choice == '3':
        print("")
        print("Coloque os valores das amostras respectivamente:")
        print("")

        get_mp10 = int(input("Coloque o mp10: "))
        get_mp25 = int(input("Coloque o mp25: "))
        get_o3 = int(input("Coloque o o3: "))
        get_co = int(input("Coloque o co: "))
        get_no2 = int(input("Coloque o no2: "))
        get_so2 = int(input("Coloque o so2: "))
        
        control.create_database_sample(get_mp10, get_mp25, get_o3, get_co, get_no2, get_so2)
    else:
        print("Opção inválida. Tente novamente.")
