from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator
from schoolapp.models import User


class InsertForm(FlaskForm):
    full_name = StringField('Full Name',
                           validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    grade = IntegerField("Grade", validators=[DataRequired()])
    date_of_birth = StringField("Date Of Birth", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    tuition_fee = StringField("Tuition Fee")
    additional_info = StringField("Additional Info")
    gender = StringField("Gender")
    active = IntegerField("Active")

    def validate_full_name(self, full_name):
        user = User.query.filter_by(full_name=full_name.data).first()
        if user:
            raise ValidationError("That name is taken. Please Choose a different one.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please Choose a different one.")


class RegistrationForm(FlaskForm):
    full_name = StringField('Full Name',
                           validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    grade = IntegerField("Grade", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    tuition_fee = StringField("Tuition Fee")
    additional_info = StringField("Additional Info")
    gender = StringField("Gender")
    date_of_birth = StringField("Date Of Birth", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_full_name(self, full_name):
        user = User.query.filter_by(full_name=full_name.data).first()
        if user:
            raise ValidationError("That name is taken. Please Choose a different one.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please Choose a different one.")


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    grade = IntegerField("Grade", validators=[DataRequired()])
    date_of_birth = StringField("Date Of Birth", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    tuition_fee = StringField("Tuition Fee")
    additional_info = StringField("Additional Info")
    gender = StringField("Gender")
    address = StringField("Address", validators=[DataRequired()])
    picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField('Update')

    def validate_full_name(self, full_name):
        if full_name.data != current_user.full_name:
            user = User.query.filter_by(full_name=full_name.data).first()
            if user:
                raise ValidationError("That name is taken. Please Choose a different one.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is taken. Please Choose a different one.")

