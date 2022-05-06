from flask_wtf import FlaskForm
from wtforms import SubmitField


class EndForm(FlaskForm):
    submit = SubmitField('УЗНАТЬ ЕЩЁ РАЗ!')