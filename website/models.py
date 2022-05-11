from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    username = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    classe = db.Column(db.String(20))
    comments = db.relationship('Comment')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    classe = db.Column(db.String(20))
    userType = db.Column(db.String(20))
    matiere = db.Column(db.String(50))
    notes = db.relationship('Note')
    marks = db.relationship('Mark')
    todo = db.relationship('Todo')




class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    username = db.Column(db.String(300))
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))





class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cc = db.Column(db.Float)
    ds = db.Column(db.Float)
    exam = db.Column(db.Float)
    matiere = db.Column(db.String(300))
    username = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))




    

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    username = db.Column(db.String(300))
    comments = db.relationship('CommentTodo')
    matiere = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))














class CommentTodo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    username = db.Column(db.String(300))
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'))