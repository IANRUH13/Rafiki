import psycopg2

url = "dbname='d6lr2vksjitmj6' user='jtcwlloyeskdyt' host='ec2-174-129-240-67.compute-1.amazonaws.com' port=5432 password='3d37fb15ca22276c757200f620e10905ca8f44d27eb6358519a2a13da1c400c4'"


class database_setup(object):

    def __init__(self):
        self.conn = psycopg2.connect(url)
        self.cursor = self.conn.cursor()

    def destroy_tables(self):
        self.cursor.execute("""DROP TABLE IF EXISTS user CASCADE;""")

        self.conn.commit()

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
            user_id SERIAL NOT NULL,
            name VARCHAR(50) NOT NULL,
            post_date DATE NOT NULL DEFAULT CURRENT_DATE,
            email VARCHAR(50)  UNIQUE NOT NULL,
            password VARCHAR(256) NOT NULL,
            photo VARCHAR(255) NOT NULL,
            isRafiki BOOLEAN NOT NULL,
            PRIMARY KEY (email)
            );""")


        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Share (
            share_id SERIAL NOT NULL,
            story TEXT NOT NULL,
            post_date DATE NOT NULL DEFAULT CURRENT_DATE,
            email VARCHAR(50) REFERENCES Users(email) NOT NULL,
            PRIMARY KEY (share_id)
            );""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Comments (
            comment_id SERIAL NOT NULL,
            comment TEXT NOT NULL,
            postedon DATE NOT NULL DEFAULT CURRENT_DATE,
            email VARCHAR(50) REFERENCES Users(email),
            share_id INT REFERENCES Share(share_id),
            PRIMARY KEY (comment_id)

            );""")


        self.conn.commit()
