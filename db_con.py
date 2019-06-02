import psycopg2

url = "dbname='rafiki' user='postgres' host='localhost' port=5432 password='Boywonder47'"


class database_setup(object):

    def __init__(self):
        self.conn = psycopg2.connect(url)
        self.cursor = self.conn.cursor()

    def destroy_tables(self):
        self.cursor.execute("""DROP TABLE IF EXISTS user CASCADE;""")

        self.conn.commit()

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
            name VARCHAR(50) NOT NULL,
            post_date TIMESTAMP,
            email VARCHAR(50)  UNIQUE NOT NULL,
            password VARCHAR(256) NOT NULL,
            photo VARCHAR(255) NOT NULL,
            PRIMARY KEY (email)
            );""")


        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Share (
            share_id SERIAL NOT NULL,
            story VARCHAR(500) NOT NULL,
            post_date TIMESTAMP,
            email VARCHAR(25) REFERENCES Users(email) NOT NULL,
            PRIMARY KEY (share_id)
            );""")



        self.conn.commit()
