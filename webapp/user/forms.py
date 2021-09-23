from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={'class':'form-control'})
    password = PasswordField('пароль', validators=[DataRequired()], render_kw={'class':'form-control'})
    remember_me = BooleanField('запомнить меня', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить', render_kw={'class': 'btn-primary'})