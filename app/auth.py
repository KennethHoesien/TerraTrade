from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.db_manager import fetchone, executeCommit
from .models.user import User

auth = Blueprint("auth", __name__)

@auth.route("/signup")
def signup():
    return render_template("signup.html")

@auth.route("/signup", methods=['POST'])
def signup_post():
    user_id = request.form.get('user_id')
    password = request.form.get('password')
    name = request.form.get('name')
    address = request.form.get('address')
    role = request.form.get('role')
    phone_number = request.form.get('phone_number')
    
    
    user = User.findMatchOR(('name', 'user_id'), (name, user_id))
    if user: 
        if user.name.lower() == name.lower(): flash("Your name are already registered")
        if str(user.id) == user_id: flash("User ID already registered")
        return redirect(url_for('auth.signup'))
    
    result = executeCommit(
        "INSERT INTO Users (`user_id`, `password`, `name`, `address`, `role`, 'phone_number') VALUES (%s, %s, %s, %s, %s)", 
        (user_id, generate_password_hash(password, method='scrypt'), name, address, role, phone_number)
    )
    print(result)
    
    return redirect(url_for('auth.login'))

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/login", methods=['POST'])
def login_post(): 
    user_id = request.form.get('user_id')
    password = request.form.get('password')
    user = User.findMatchOR(('user_id',), (user_id,)) #fetchone("SELECT `Password` FROM Users WHERE `Email`=%s", (email,))
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    
    print("Logging in:", login_user(user))
    return redirect(url_for('views.index'))

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))