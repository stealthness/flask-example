import sqlite3
from markupsafe import escape

class SimpleDataManager:

    def __init__(self):
        self.clubs = []


    def create_tables(self, db_filename):
        cursor = sqlite3.connect(db_filename).cursor()
        cursor.execute('drop table if exists users;')
        cursor.execute('drop table if exists clubs;')
        cursor.execute('create table if not exists users(user_name text primary key, location text,club text);')
        cursor.execute('create table if not exists clubs(club_name text primary key, stadium text, league text);')

    def execute_sql(self, db_filename, sql):
        cursor = sqlite3.connect(db_filename)
        return cursor.execute(sql).fetchall();

    def load_users_from_db(self, csv_filename, db_filename):
        with open(csv_filename, 'r') as csv_file:
            with sqlite3.connect(db_filename) as db:
                cursor = db.cursor()
                for line in csv_file:
                    name, location, club = line.split(',')
                    cursor.execute(f'insert into users values ("{name}", "{location}", "{club.strip()}");')

            print(cursor.execute(f'select * from users').fetchall())


    def get_user_list(self, db_filename):

        return [item[0] for item  in self.execute_sql(db_filename, sql='select user_name from users')]

    def load_clubs_from_db(self, csv_filename, db_filename):
        with open(csv_filename, 'r') as csv_file:
            with sqlite3.connect(db_filename) as db:
                cursor = db.cursor()
                for line in csv_file:
                    name, stadium, league = line.strip().split('\t')
                    self.clubs.append(name)

                    cursor.execute(f'insert into clubs values ("{name}", "{stadium}", "{league}");')

            print(cursor.execute(f'select club_name, stadium from clubs').fetchall())

    def add_new_user(self, new_user, location, club, db_filename):
        """
        Adds a new user, it assumes that all have been checked as safe
        :param new_user:
        :param location:
        :param club:
        :param db_filename:
        :return:
        """
        if club not in self.clubs:
            return

        with sqlite3.connect(db_filename) as db:
            cursor = db.cursor()
            cursor.execute(f'insert into users values("{new_user}","{location}" ,"{club}" )').fetchall()

    def get_user_detail(self, user_name, db_filename):
        with sqlite3.connect(db_filename) as db:
            cursor = db.cursor()
            sql_output = cursor.execute(f'select * from users where user_name="{user_name}"').fetchall()
            print(f'<1>output:{sql_output}')
            _, location, club= sql_output[0]
            return location, club.strip('\n')

    def get_club_detail(self, club_name, db_filename):

        with sqlite3.connect(db_filename) as db:

            cursor = db.cursor()
            print(f"clubname: {club_name}")
            sql_output = cursor.execute(f'select * from clubs where club_name="{club_name}"').fetchall()
            print(f'<2>output:{sql_output}')
            _, stadium, league = sql_output[0]

            return stadium, league

    def get_tables(self, db_filename):
        with sqlite3.connect(db_filename) as db:
            cursor = db.cursor()
            html = f"""
            <p>{str(cursor.execute(f'select * from users').fetchall())}</p>
            <p>{str(cursor.execute(f'select * from clubs').fetchall())}</p>"""

            return html