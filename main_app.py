import os
from random import shuffle
import re

from flask import Flask, render_template, redirect, url_for, request
from markupsafe import escape
from data_manager import SimpleDataManager

db_filename = os.path.join('res', 'user_db.db')
csv_users_filename = os.path.join('res', 'full_user_data.csv')
csv_clubs_filename = os.path.join('res', 'clubs_data.csv')

app = Flask(__name__)
data = SimpleDataManager()
data.create_tables(db_filename)
data.load_users_from_db(csv_users_filename, db_filename)
data.load_clubs_from_db(csv_clubs_filename, db_filename)

CLEANR = re.compile("('),")

@app.route('/', methods=(['POST', 'GET']))
@app.route('/index', methods=(['POST', 'GET']))
def get_home_page():
    if request.method == 'POST':
        user = escape(request.form['name'])
        if user.title() in data.users:
            return redirect(url_for('get_user_page', username=user.lower()))
        else:
            return redirect(url_for('get_new_user_page'))

    return render_template('index.html', title='Home Page')

@app.route('/about')
def get_about_page():
    users = []
    for _ in range(3):
        shuffle(data.users)
        users = data.users[:3]

    return render_template('about.html', title='Home Page', users=users)


@app.route('/warn')
def get_warning_page(message=''):
    return render_template('error_page.html', title='Error Page', message=message)


@app.route('/user/<string:username>')
def get_user_page(username):
    safe_username = escape(username).strip()
    if safe_username == 'all_users':
        return redirect(url_for("get_all_users_page"))
    if not safe_username.title() in data.users:
        return redirect(url_for('get_warning_page'))
    stadium = None
    league = None
    location, club = data.get_user_detail(safe_username.title(), db_filename)
    if location is None or location == '':
        location = 'none'


    if club not in data.clubs:
        club = "none"
    else:
        stadium, league = data.get_club_detail(club.title(), db_filename)

    print(f'{club}, {stadium}, {location}, {league}')

    return render_template('user_page.html', title='User Page' ,username=safe_username, club=club, location=location, league=league)


@app.route('/all_users')
def get_all_users_page():
    users = [item[0] for item  in data.execute_sql(db_filename, sql='select user_name from users')]
    print(users)

    return render_template("all_users.html", title="All Users Page", users=data.users)


@app.route('/new_user', methods = ([ 'POST','GET']))
def get_new_user_page():
    if request.method == 'POST':
        new_user = escape(request.form['name']).strip().title()
        location = escape(request.form['location']).title()
        club = escape(request.form['club']).title()
        if new_user in data.users or new_user == '':
            print(new_user)
            return render_template('add_new_user_page.html')
        if not club in data.clubs:
            print(club)
            return render_template('add_new_user_page.html')
        print(f'<3> {new_user} {location} {club}')
        data.add_new_user(new_user, location, club, db_filename)
        return redirect(url_for ('get_user_page', username=new_user.lower()))
    return render_template('add_new_user_page.html', title="New User Page")

@app.route('/tables')
def get_tables():
    return data.get_tables(db_filename)


if __name__ == "__main__":
    # app.run()

    # Optional, host address often required if running on a VM
    app.run(debug=True, host="0.0.0.0")