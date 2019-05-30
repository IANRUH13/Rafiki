from db_con import database_setup

class User():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def save_users(self, name, email,password, photo):

        user = {

            "name": name,
            "email": email,
            "password": password,
            "photo": photo

        }

        query = """INSERT INTO Users (name,email,password,photo)
            VALUES(%(name)s,%(email)s, %(password)s,%(photo)s);"""

        self.cursor.execute(query, user)
        self.database.conn.commit()

        return user

    def login(self, email, password):

        query = "SELECT name,email,photo FROM Users WHERE email = '%s' AND password = '%s';" % (email, password)
        self.cursor.execute(query)
        users = self.cursor.fetchone()

        return users
