import os
import sqlite3


class SimpleDataManager:

    def __init__(self):
        self.users = []


    def load_users(self, filename):
        with open(filename) as csv_file:
            for name in csv_file:
                self.users.append(name.strip())

    def create_tables(self, db_filename):
        cursor = sqlite3.connect(db_filename).cursor()
        cursor.execute('drop table users;')
        cursor.execute('create table if not exists users(name text primary key, location text,club text);')

    def execute(self, db_filename, sql=None):
        cursor = sqlite3.connect(db_filename)
        return cursor.execute(f'select * from users;');

    def load_user_from_db(self, csv_filename, db_filename):
        with open(csv_filename, 'r') as csv_file:
            with sqlite3.connect(db_filename) as db:
                cursor = db.cursor()
                for line in csv_file:
                    name, location, club = line.split(',')
                    self.users.append(name)

                    cursor.execute(f'insert into users values ("{name}", "{location}", "{club}");')

            print(cursor.execute(f'select Location from users where name="{name}"').fetchall())
            print(cursor.execute(f"select * from users where name='{name}'").fetchall())

    def get_user_detail(self, user_name, db_filename):

        with sqlite3.connect(db_filename) as db:

            cursor = db.cursor()

            # print(cursor.execute('.tables').fetchall())
            sql_output = cursor.execute(f"select * from users where name='{user_name}'").fetchall()
            print(sql_output)
            print(type(sql_output[0]))
            _, location, club = sql_output[0]

            return club, "...", location