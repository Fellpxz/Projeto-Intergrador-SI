import mysql.connector

# Database Shortcuts
class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    # Connect
    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    # Disconnect
    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()

    # Execute a Query
    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    # Fetches, Select information
    def fetch_data(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
