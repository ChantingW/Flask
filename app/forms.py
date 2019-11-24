from flask_wtf import Form
from wtforms import StringField, BooleanField,  TextAreaField, SelectMultipleField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from .models import Task

class TaskForm(Form):
    task_name = StringField('task name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    deadline = DateField('deadline', validators=[DataRequired()])
#As the state is set to 'uncompelte' by default, so the user do not need to input it in the form

class DeadlineForm(Form):
    deadline_search = DateField('deadline_search', validators=[DataRequired()])
