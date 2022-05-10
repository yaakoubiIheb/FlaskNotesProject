from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from .models import CommentTodo, Note, Todo, User,Comment
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        classe=request.form.get('classe')

        if len(note) < 1:
            flash('Note is too short!', category='error')

        else:
            
            username=current_user.first_name+" "+current_user.last_name
            new_note = Note(data=note, user_id=current_user.id,username=username,classe=classe)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)





@views.route('/studentHome', methods=['GET'])
@login_required
def studentHome():


    notes=Note.query.filter_by(classe=current_user.classe)
    
    
    return render_template("studentHome.html", user=current_user,notes=notes)









@views.route('/comment/<int:noteId>', methods=['POST'])
@login_required
def comment(noteId):


    comment = request.form.get('comment')

    if len(comment) < 1:
        flash('Comment is too short!', category='error')

    else:
            
        username=current_user.first_name+" "+current_user.last_name
        new_comment = Comment(data=comment, note_id=noteId,username=username)
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment added!', category='success')


    
    
    
    return redirect(url_for('views.studentHome'))











@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})









@views.route('/todo', methods=['GET'])
@login_required
def todo():

    ingA=User.query.filter_by(classe="3ingA")
    ingB=User.query.filter_by(classe="3ingB")
    todo_list=Todo.query.filter_by(matiere=current_user.matiere)
    for todo in todo_list:
        user = User.query.filter_by(id=todo.user_id).first()
        username=user.first_name+" "+user.last_name
        todo.username=username
        


    return render_template("todo.html", user=current_user,ingA=ingA,ingB=ingB,todo_list=todo_list)










@views.route('/addTodo/<string:matiere>/<int:userId>', methods=['POST'])
@login_required
def addTodo(matiere,userId):

    data = request.form.get('todo')

    if len(data) < 1:
        flash('Assignment is too short!', category='error')

    else:
            
        username=current_user.first_name+" "+current_user.last_name
        new_todo = Todo(data=data, user_id=userId,username=username,matiere=matiere)
        db.session.add(new_todo)
        db.session.commit()
        flash('Assignment added!', category='success')


    
    
    
    return redirect(url_for('views.todo'))







    
@views.route('/todoStudent', methods=['GET'])
@login_required
def todoStudent():


    return render_template("todoStudent.html", user=current_user)









@views.route('/commentTodo/<int:todoId>', methods=['POST'])
@login_required
def commentTodo(todoId):


    comment = request.form.get('comment')

    if len(comment) < 1:
        flash('Comment is too short!', category='error')

    else:
            
        username=current_user.first_name+" "+current_user.last_name
        new_comment = CommentTodo(data=comment, todo_id=todoId,username=username)
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment added!', category='success')



    if(current_user.userType=="teacher"):
        return redirect(url_for('views.todo'))
 
    
    
    return redirect(url_for('views.todoStudent'))










@views.route('/deleteTodo', methods=['POST'])
def delete_todo():
    todo = json.loads(request.data)
    todoId = todo['todoId']
    todo = Todo.query.get(todoId)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        
        

    return jsonify({})