from Controller.Controller import MainController

def main():
    controller = MainController()
    controller.test_database_connection()
    controller.see_database_samples()

if __name__ == "__main__":
    main()
