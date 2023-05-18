from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def get_home_page():
    return """<h1>The Football Supporter Site - Home Page</h1>
    <p>Welcome to the football supporter site</p>
    <p><a href='/index'>Home</a> | <a href='/about'>About</a></p>"""

@app.route('/about')
def get_about_page():
    return """<h1>The Football Supporter Site - About Page</h1>
    <p>This flask example will create a football supporter site</p>
    <p><a href='/index'>Home</a> | <a href='/about'>About</a></p>"""


if __name__ == "__main__":
    # app.run()

    # Optional, host address often required if running on a VM
    app.run(debug=True, host="0.0.0.0")