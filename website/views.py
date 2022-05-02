from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User
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