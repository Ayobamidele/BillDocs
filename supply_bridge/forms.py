from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
import phonenumbers
from .models import User


# from flask_login import login_required, current_user

class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname',
                            validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Lastname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField('Phone',
                        validators=[DataRequired()])
    email = EmailField('Email address',
                       validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign-up")

    @staticmethod
    def validate_phone(phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')

    @staticmethod
    def validate_email(email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class UserEdit(FlaskForm):
    firstname = StringField('Firstname',
                            validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Lastname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email',
                       validators=[DataRequired(), Email()])
    save = SubmitField("Save")

    cancel = SubmitField(label='Cancel',
                         render_kw={'form-novalidate': True, 'class': ' btn-warning'})

    @staticmethod
    def validate_email(email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class PhoneChangeForm(FlaskForm):
    phone = StringField('Phone',
                        validators=[DataRequired()])

    @staticmethod
    def validate_phone(phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')


class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')


class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=1, max=2000)])
    submit = SubmitField('Submit')
