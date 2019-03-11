from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from models.users.users import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class AdminAddUserForm(FlaskForm):
    registration_number = StringField('Registration Number',
                                      validators=[DataRequired(),
                                                  Length(min=1, max=20)])
    surname = StringField('Surname',
                          validators=[DataRequired(),
                                      Length(min=1, max=20)])
    middle_name = StringField('Middle Name',
                              validators=[DataRequired(),
                                          Length(min=1, max=20)])
    first_name = StringField('First Name',
                             validators=[DataRequired(),
                                         Length(min=1, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=2)])
    submit = SubmitField('Register')

    def validate_email(self, email):
        _, all_emails_from_database = User.find_all_emails_and_registration_number()
        if email.data:
            if email.data in all_emails_from_database:
                raise ValidationError("That email is taken. Please choose another one!")
        else:
            raise ValidationError("This field cannot be blank!")

    def validate_registration_number(self, registration_number):
        all_registration_number_from_database, _ = User.find_all_emails_and_registration_number()
        if registration_number.data:
            if registration_number.data in all_registration_number_from_database:
                raise ValidationError("That Registration Number is taken. Please choose another one!")


class UserLoginForm(FlaskForm):
    registration_number = StringField('Registration Number/Username',
                                      validators=[DataRequired(),
                                                  Length(min=1)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=2)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    registration_number = StringField('Registration Number',
                                      validators=[DataRequired(),
                                                  Length(min=1)])
    surname = StringField('Surname',
                          validators=[DataRequired(),
                                      Length(min=1, max=20)])
    middle_name = StringField('Middle Name',
                              validators=[DataRequired(),
                                          Length(min=1, max=20)])
    first_name = StringField('First Name',
                             validators=[DataRequired(),
                                         Length(min=1, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=2)])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        _, all_emails_from_database = User.find_all_emails_and_registration_number()
        if email.data != current_user.email:
            if email.data in all_emails_from_database:
                raise ValidationError("That email is taken. Please choose another one!")


class UpdateAdminAccountForm(FlaskForm):
    registration_number = StringField('Username',
                                      validators=[DataRequired(),
                                                  Length(min=1)])
    surname = StringField('Surname',
                          validators=[DataRequired(),
                                      Length(min=1, max=20)])
    middle_name = StringField('Middle Name',
                              validators=[DataRequired(),
                                          Length(min=1, max=20)])
    first_name = StringField('First Name',
                             validators=[DataRequired(),
                                         Length(min=1, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=2)])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        _, all_emails_from_database = User.find_all_emails_and_registration_number()
        if email.data != current_user.email:
            if email.data in all_emails_from_database:
                raise ValidationError("That email is taken. Please choose another one!")


class AdminUpdateStudentAccountForm(FlaskForm):
    registration_number = StringField('Registration Number',
                                      validators=[DataRequired(),
                                                  Length(min=1)])
    surname = StringField('Surname',
                          validators=[DataRequired(),
                                      Length(min=1, max=20)])
    middle_name = StringField('Middle Name',
                              validators=[DataRequired(),
                                          Length(min=1, max=20)])
    first_name = StringField('First Name',
                             validators=[DataRequired(),
                                         Length(min=1, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])
    submit = SubmitField('Update')

    def validate_email(self, email):
        _, all_emails_from_database = User.find_all_emails_and_registration_number()
        if email.data:
            if email.data in all_emails_from_database:
                raise ValidationError("That email is taken. Please choose another one!")


class SelectElectiveCourses(FlaskForm):
    user_type = SelectField('Select Suited Area Of Specialization', validators=[DataRequired()],
                            choices=(("ai", "Artificial Intelligence"), ("cn", "Computer Networks"),
                                     ("se", "Software Engineering"), ("sye", "Systems Engineering")))
    submit = SubmitField('START TEST')


class StartQuiz(FlaskForm):
    submit = SubmitField('START TEST')


class QuestionForm(FlaskForm):
    question_option = RadioField("Answers", coerce=str)
    submit_next = SubmitField('NEXT')
    # submit_previous = SubmitField('PREVIOUS')
