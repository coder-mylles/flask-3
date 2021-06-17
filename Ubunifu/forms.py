from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),Length(min=3,max=21)])
    email = StringField("email", validators=[Email(),DataRequired()])
    password = PasswordField("password" ,validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("Sign Up")



class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),Length(min=3,max=21)])
    email = StringField("email", validators=[Email(),DataRequired()])
    password = PasswordField("password" ,validators=[DataRequired()])
    remember = BooleanField("Rmember Me")
    submit = SubmitField("Log In")
