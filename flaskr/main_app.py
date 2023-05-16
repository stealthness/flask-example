from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def get_home_page():
    return render_template('index.html', title='Home Page')

@app.route('/about')
def get_about_page():
    return render_template('about.html', title='Home Page')


@app.route('/warn')
def get_warning_page(message=''):
    return render_template('error_page.html', title='Error Page', message=message)


if __name__ == "__main__":
    # app.run()

    # Optional, host address often required if running on a VM
    app.run(debug=True, host="0.0.0.0")