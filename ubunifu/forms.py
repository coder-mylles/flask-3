from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from ubunifu.models import User,Post 
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

        
#   .......................Registartion forms class definition...........................
    

class RegistrationForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(),Length(min=3,max=21)])
    email = StringField("email", validators=[Email(),DataRequired()])
    password = PasswordField("password" ,validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("Sign Up")


# ...................Custom Validation for username..............

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken,please choose another username')

# .....................custom validation for email...............

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken,please choose another username')



class LoginForm(FlaskForm):
    email = StringField("email", validators=[Email(),DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")



# ............................to update our account information...............


class UpdateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),Length(min=3,max=21)])

    email = StringField("email", validators=[Email(),DataRequired()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])

    password = PasswordField("password" ,validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",validators=[DataRequired(),EqualTo("password")])

    submit = SubmitField("Update")

    


# ...................Custom Validation for username..............

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken,please choose another username')

# .....................custom validation for email...............

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=username.data).first()
            if user:
                raise ValidationError('That email is taken,please choose another username')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


