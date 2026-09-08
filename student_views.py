from mysql import connector

class DbConnect:
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Athulya@2907",
                database="gym_db_b3"
            )
            return self.connection
        except Exception as e:
            return None
    def post(self):
        print("POST method ")
        pass
