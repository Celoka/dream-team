from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 
from wtforms.ext.sqlalchemy.fields import QuerySelectField 

from ..models import Department, Role 


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department 
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit role
    """

    name = StringField('Name', validators=[DataRequired()])
    description =StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assing departments and roles to employees
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name", get_pk=lambda x:"id")
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name", get_pk=lambda x:"id")
    submit = SubmitField('Submit')