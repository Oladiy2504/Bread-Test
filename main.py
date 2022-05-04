from flask import Flask
from flask import render_template, redirect, session, make_response
from flask_login import LoginManager, login_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run(port=8080, host="127.0.0.1")


if __name__ == '__main__':
    main()