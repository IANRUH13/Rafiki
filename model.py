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
            "photo": photo,
            "isRafiki":True

        }

        query = """INSERT INTO Users (name,email,password,photo,isRafiki)
            VALUES(%(name)s,%(email)s, %(password)s,%(photo)s,%(isRafiki)s);"""

        self.cursor.execute(query, user)
        self.database.conn.commit()

        return user

    def login(self, email, password):

        query = "SELECT password FROM Users WHERE email = '%s';" % (email)
        self.cursor.execute(query)
        pword = self.cursor.fetchone()

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
        query = "SELECT users.name,users.photo,users.isRafiki,comments.comment,comments.postedon FROM users,comments where comments.email =  users.email and comments.share_id = '%s' ORDER BY comment_id DESC;" % (share_id)
        self.cursor.execute(query)
        stories= self.cursor.fetchall()

        return stories

    def search_post(self, search):
        self.cursor.execute("SELECT * FROM share WHERE story LIKE '%s';" % ("%" + search + "%"))
        query = self.cursor.fetchall()
        return query

    def update_photo(self,email,photo):
        user = {
            "photo": photo
        }

        query = "UPDATE users SET photo = '%s' WHERE email = '%s';"% (photo, email)
        self.cursor.execute(query, user)
        self.database.conn.commit()
        return user


    def update_email(self,email,old,new,verify):
        user = {
            "email": new
        }

        if new == verify:
            query = "UPDATE users SET email = '%s' WHERE email = '%s';"% (new, email)
            self.cursor.execute(query, user)
            self.database.conn.commit()
            return user


    def update_password(self,email,password):
        user = {
            "password":sha256_crypt.encrypt(password)
        }

        query = "UPDATE users SET password = '%s' WHERE email = '%s';"% (password, email)
        self.cursor.execute(query, user)
        self.database.conn.commit()
        return user



    def update_name(self,email,name):
        user = {
            "name":name
        }


        query = "UPDATE users SET name = '%s' WHERE email = '%s';"% (name, email)
        self.cursor.execute(query, user)
        self.database.conn.commit()
        return user






