from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy import null
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                if user.userType=="teacher":

                    return redirect(url_for('views.home'))
                else:
                    return redirect(url_for('views.studentHome'))

            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        userType= request.form.get('userType')
        matiere= request.form.get('matiere')
        secretKey=request.form.get('secretKey')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        classe= request.form.get('classe')

        
        user = User.query.filter_by(email=email).first()
        teacher = User.query.filter_by(matiere=matiere).first()


        if user:
            flash('Email already exists.', category='error')
        elif email.find("@sesame.com.tn",2)==-1:
            flash('Email format is invalid. example of valid email : example@sesame.com.tn.', category='error')
        elif len(first_name) < 2:
            flash('First name must be longer than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be longer than 1 character.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif userType is None:
            flash('User type is mandatory.', category='error')
        elif userType == "teacher" and len(matiere) < 1:
            flash('Subject is mandatory while creating a teacher account.', category='error')
            
        elif userType == "teacher" and teacher:
            flash('There is already a teacher teaching this subject. If there is an issue please contact the administration .', category='error')
        elif userType == "teacher" and len(secretKey) < 1:
            flash('Secret key is mandatory while creating a teacher account. if you don\'t have the secret key please contact the administration', category='error')
        elif userType == "teacher" and secretKey!="sesamesecretkey":
            flash('Secret key is incorrect. if you don\'t have the secret key please contact the administration', category='error')
        elif userType == "student" and classe is None:
            flash('You must select a class.', category='error')
    
    
        else:
            if userType=="teacher":
                new_user = User(email=email, first_name=first_name,last_name=last_name, password=generate_password_hash(
                    password1, method='sha256'),userType=userType,matiere=matiere)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created!', category='success')

                return redirect(url_for('views.home'))

            else:

                new_user = User(email=email, first_name=first_name,last_name=last_name, password=generate_password_hash(
                password1, method='sha256'),userType=userType,classe=classe)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created!', category='success')

                return redirect(url_for('views.studentHome'))


    
    
    return render_template("sign_up.html", user=current_user)