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
        cursor.execute('create table if not exists users(name text not null, location text,club text);')

    def execute(self, db_filename, sql=None):
        cursor = sqlite3.connect(db_filename)
        return cursor.execute(f'select * from users');

    def load_user_from_db(self, csv_filename, db_filename):
        with open(csv_filename, 'r') as csv_file:
            cursor = sqlite3.connect(db_filename).cursor()
            for line in csv_file:
                name, location, club = line.split(',')
                self.users.append(name)

                # print(db.execute('select * from users').fetchall())
                cursor.execute(f'insert into users values ("{name}", "{location}", "{club}");')

            print(cursor.execute('select * from users').fetchall())

            print(cursor.execute(f"select * from users where name='Vince'").fetchall())

    def get_user_detail(self, user_name, filename):
        db = sqlite3.connect(filename)
        print(db.execute('select * from users').fetchall())
        print(db.execute(f"select * from users where name='Vince'").fetchall())
        return "Arsenal", "Highbury", "London"