"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from asyncio import tasks
from typing import final
from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, length
from flaskdb.widgets import ButtonField

class LoginForm(FlaskForm):
    username = StringField(
        "User Name",
        validators = [
            DataRequired(message="User Name is required."),
            length(max=64, message="User Name should be input within 64 characters."),
        ],
    )
    password = PasswordField(
        "Password",
        validators = [
            DataRequired(message="Password is required."),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Login")

    def copy_from(self, user):
        self.username.data = user.username
        self.password.data = user.password

    def copy_to(self, user):
        user.username = self.username.data
        user.password = self.password.data

class AddItemForm(FlaskForm):
    itemname = StringField(
        "Item Name",
        validators = [
            DataRequired(message="Item Name is required."),
        ],
    )
    price = IntegerField(
        "Price",
        validators = [
            DataRequired(message="Price is required."),
        ],
    )
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.itemname.data = item.itemname
        self.price.data = item.price

    def copy_to(self, item):
        item.itemname = self.itemname.data
        item.price = self.price.data

class AddTaskForm(FlaskForm):
    category = StringField(
        "Category Name",
        validators = [
            DataRequired(message="Category Name is required."),
        ],
    )
    
    role = StringField(
        "Role",
        validators = [
            DataRequired(message="Role is required."),
        ],
    )
    
    task = StringField(
        "Task",
        validators = [
            DataRequired(message="Task is required."),
        ],
    )
    
    start_date = DateField(
        "Startdate",
        format='%Y/%m/%d',
        validators = [
            DataRequired(message="startdate is required."),
        ],
    )
    
    final_date = DateField(
        "Finaldate",
        format='%Y/%m/%d',
        validators = [
            DataRequired(message="finaldate is required."),
        ],
    )
    
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.category.data = item.category
        self.task.data = item.task
        self.role.data = item.role
        self.start_date.data=item.start_date
        self.final_date.data=item.final_date

    def copy_to(self, item):
        item.category = self.category.data
        item.task = self.task.data
        item.role = self.role.data
        item.start_date = self.start_date.data
        item.final_date = self.final_date.data
        

class SearchItemForm(FlaskForm):
    itemname = StringField(
        "Item Name",
        validators = [
            DataRequired(message="Item Name is required."),
        ],
    )
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.itemname.data = item.itemname

    def copy_to(self, item):
        item.itemname = self.itemname.data
        
class SearchCategoryForm(FlaskForm):
    category = StringField(
        "Search Category",
        validators = [
            DataRequired(message="Category is required."),
        ],
    )
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.category.data = item.category

    def copy_to(self, item):
        item.category = self.category.data
