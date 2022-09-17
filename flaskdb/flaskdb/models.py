"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from datetime import timezone
from flaskdb import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.id

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    itemname = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return "<Item %r>" % self.id

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(128),nullable=False)
    task = db.Column(db.String(128),nullable=False)
    role = db.Column(db.String(128),nullable=False)
    start_date=db.Column(db.Timestamp)
    final_date=db.Column(db.Timestamp)
    
    def __repr__(self):
        return "<Task %r>" % self.id
