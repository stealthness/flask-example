from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return "<h1>Hello Flask Example</h1>"


if __name__ == "__main__":
    app.run()

    # Optional, host address often required if running on a VM
    # app.run(debug=True, host="0.0.0.0")