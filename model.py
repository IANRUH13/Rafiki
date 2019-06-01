from db_con import database_setup
from passlib.hash import sha256_crypt

class User():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def save_users(self, name, email,password, photo):

        user = {

            "name": name,
            "email": email,
            "password":sha256_crypt.encrypt(password),
            "photo": photo

        }

        query = """INSERT INTO Users (name,email,password,photo)
            VALUES(%(name)s,%(email)s, %(password)s,%(photo)s);"""

        self.cursor.execute(query, user)
        self.database.conn.commit()

        return user

    def login(self, email, password):

        query = "SELECT password FROM Users WHERE email = '%s';" % (email)
        self.cursor.execute(query)
        pword = self.cursor.fetchone()

        isValid = sha256_crypt.verify(password,pword[0])

        if isValid:
            query = "SELECT name,email,photo FROM Users WHERE email = '%s';" % (email)
            self.cursor.execute(query)
            users = self.cursor.fetchone()

            return users
