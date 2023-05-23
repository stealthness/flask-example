import os

from flask import Flask

from data_manager import SimpleDataManager


def create_app(test_config=None):
    db_filename = os.path.join('res', 'user_db.db')
    csv_users_filename = os.path.join('res', 'full_user_data.csv')
    csv_clubs_filename = os.path.join('res', 'clubs_data.csv')

    app = Flask(__name__)
    data = SimpleDataManager()
    data.create_tables(db_filename)
    data.load_users_from_db(csv_users_filename, db_filename)
    data.load_clubs_from_db(csv_clubs_filename, db_filename)

