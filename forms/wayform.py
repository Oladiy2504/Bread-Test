from flask_wtf import FlaskForm
from wtforms import SubmitField


class WayForm(FlaskForm):
    submit = SubmitField('УЗНАТЬ!')