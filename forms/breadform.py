from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class BreadForm(FlaskForm):
    select = SelectField('Какой ты хлеб?', choices=['Багет', 'Оладий', 'Черный хлеб', 'Белый хлеб', 'Я не хлеб!'])
    submit = SubmitField('УЗНАТЬ!')
