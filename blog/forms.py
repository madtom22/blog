# blog/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.routing import ValidationError
from config import Config


class LoginForm(FlaskForm):
    username = StringField('Użytkownik', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])

    def validate_username(self, field):
        if field.data != Config.ADMIN_USERNAME:
            raise ValidationError("Niepoprawna nazwa użytkownika")
        return field.data

    def validate_password(self, field):
        if field.data != Config.ADMIN_PASSWORD:
            raise ValidationError("Niepoprawne hasło")
        return field.data

class EntryForm(FlaskForm):
    title = StringField('Tytuł wpisu', validators=[DataRequired()])
    body = TextAreaField('Treść wpisu', validators=[DataRequired()])
    is_published = BooleanField('Czy opublikowany')