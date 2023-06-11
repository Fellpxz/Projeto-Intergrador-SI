from Models.Model import DatabaseOperations

class MainController:
    # Seting the Self Operator
    def __init__(self):
        self.database = DatabaseOperations('us-cdbr-east-06.cleardb.net', 'be4227e4b6f77a', 'c1f135ca', 'heroku_c9cd53735e57e53')

    # Controls:
    def see_database_samples(self):
        self.database.see_samples()
    
    def create_database_sample(self, id, mp10, mp25, o3, co, no2, so2):
        self.database.create_sample()
