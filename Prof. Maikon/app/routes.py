from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db, bcrypt, socketio
from app.models import User, Message
from flask_socketio import send
from app.forms import RegistrationForm, LoginForm

bp = Blueprint('main', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            session['username'] = user.username
            return redirect(url_for('main.chat'))
        else:
            flash('Login failed. Check your username and/or password', 'danger')
    return render_template('login.html', form=form)

@bp.route('/chat')
@login_required
def chat():
    return render_template('chat.html', username=current_user.username)

@socketio.on('message')
def handle_message(msg):
    if current_user.is_authenticated:
        user_id = current_user.id
        encrypted_msg = msg  # Add encryption here if needed
        new_message = Message(user_id=user_id, message=encrypted_msg)
        db.session.add(new_message)
        db.session.commit()
        send(msg, broadcast=True)

@bp.route('/calculator')
@login_required
def calculator():
    return render_template('calculator.html')
