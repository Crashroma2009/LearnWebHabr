from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={'class':'form-control'})
    password = PasswordField('пароль', validators=[DataRequired()], render_kw={'class':'form-control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn-primary'})