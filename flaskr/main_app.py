import os
from random import shuffle

from flask import Flask, render_template, redirect, url_for, request
from markupsafe import escape
from flaskr.data_manager import SimpleDataManager

app = Flask(__name__)
data = SimpleDataManager()
data.load_users(os.path.join('res', 'user_data.csv'))

@app.route('/', methods=(['POST', 'GET']))
@app.route('/index', methods=(['POST', 'GET']))
def get_home_page():
    if request.method == 'POST':
        user = escape(request.form['name'])
        if user.title() in data.users:
            return redirect(url_for('get_user_page', username=user.lower()))
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

    return render_template('user_page.html', title='User Page' ,username=safe_username)


@app.route('/all_users')
def get_all_users_page():
    return render_template("all_users.html", title="All Users Page", users=data.users)


if __name__ == "__main__":
    # app.run()

    # Optional, host address often required if running on a VM
    app.run(debug=True, host="0.0.0.0")