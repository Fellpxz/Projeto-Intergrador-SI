from Models.Database import Database

class DatabaseOperations:
    # Seting the Self Operator
    def __init__(self, host, user, password, database):
        self.database = Database(host, user, password, database)

    # Database operations:
    def see_samples(self):
        try:
            # Conecta ao banco de dados
            self.database.connect()

            # Cria o Comando para ser executado.
            insert_query = "SELECT * FROM amostra ORDER BY id ASC"

            # Cria um objeto cursor para executar as consultas
            resultados = self.database.fetch_data(insert_query)
            resultado_formatado = []

            for item in resultados:
                item_formatado = [str(valor).replace("Decimal", "").replace("(", "").replace(")", "") for valor in item]
                resultado_formatado.append(item_formatado)

            for item in resultado_formatado:
                print(item)
            print("")

            self.database.disconnect()

        except Exception as Error:
            print("Erro ao conectar ao banco de dados:", str(Error))
            print("")
    
    def test_sample(self):
        try:
            self.database.connect()
            self.database.disconnect()
        
        except Exception as Error:
            print("Erro ao conectar ao banco de dados:", str(Error))
            print("")

    def create_sample(self):
        try:
            self.database.connect()
            self.database.disconnect()
        
        except Exception as Error:
            print("Erro ao conectar ao banco de dados:", str(Error))
            print("")
    
    def delete_sample(self):
        try:
            self.database.connect()
            self.database.disconnect()
        
        except Exception as Error:
            print("Erro ao conectar ao banco de dados:", str(Error))
            print("")
    
    def edit_sample(self):
        try:
            self.database.connect()
            self.database.disconnect()
        
        except Exception as Error:
            print("Erro ao conectar ao banco de dados:", str(Error))
            print("")