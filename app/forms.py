
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, Email, Regexp

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Regexp('^[A-Za-z ]+$')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])