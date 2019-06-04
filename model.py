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


    def share(self,email,story):

        post = {
            "email": email,
            "story": story
        }

        query = """INSERT INTO share (email,story)
            VALUES(%(email)s, %(story)s);"""

        self.cursor.execute(query, post)
        self.database.conn.commit()

        return post


    def stories(self):
        query = "SELECT share_id,story,post_date,email FROM share ORDER BY share_id DESC;"
        self.cursor.execute(query)
        stories= self.cursor.fetchall()

        return stories

    def respond(self, share_id, comment, email):
        resp = {
            "share_id": share_id,
            "comment": comment,
            "email": email
        }

        query = """INSERT INTO comments(share_id,comment,email)VALUES(%(share_id)s,%(comment)s,%(email)s)"""

        self.cursor.execute(query, resp)
        self.database.conn.commit()

        return resp

    def get_title(self,share_id):
        query = "SELECT story,post_date FROM share where share_id = '%s';" % (share_id)
        self.cursor.execute(query)
        title = self.cursor.fetchone()

        return title



    def get_respond(self,share_id):
        query = "SELECT comment,postedon FROM comments where share_id = '%s' ORDER BY comment_id DESC;" % (share_id)
        self.cursor.execute(query)
        stories= self.cursor.fetchall()

        return stories




