from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models.user import User
from app import TableClasses




auth = Blueprint("auth", __name__)

# @auth.route("/signup")
# def signup():
#     return render_template("signup.html")

# @auth.route("/signuppost", methods=['GET', 'POST'])
# def signup_post():
#     if request.method == 'POST':
#         user_id = request.form.get('user_id')
#         password = request.form.get('password')
#         name = request.form.get('name')
#         address = request.form.get('address')
#         role = request.form.get('role')
#         phone_number = request.form.get('phone_number')
        
        
#         existing_user = User.findMatchOR(('user_id',), (user_id,))

#         if existing_user: 
#             if existing_user.name.lower() == name.lower():
#                 flash("Your name are already registered")
#             if str(existing_user.id) == user_id:
#                 flash("User ID already registered")
#             return redirect(url_for('auth.signup'))
        
#         hashed_password = generate_password_hash(password, method='scrypt')

#         # Create new user instance
#         new_user = User(user_id=user_id, password=hashed_password, name=name, address=address, role=role, phone_number=phone_number)
        
#         from app import db
#         # Save to database
#         db.session.add(new_user)
#         db.session.commit()
#         flash('Account created successfully!', 'success')
#         return redirect(url_for('auth.login'))  # Redirect to login page after successful sign up
#     return render_template('signup.html')
@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        name = request.form.get('name')
        address = request.form.get('address')
        role = request.form.get('role')
        phone_number = request.form.get('phone_number')
        
        '''existing_user = User.findMatchOR(('user_id',), (user_id,))
        if existing_user: 
            if existing_user.name.lower() == name.lower():
                flash("Your name is already registered")
            if str(existing_user.id) == user_id:
                flash("User ID already registered")
            return redirect(url_for('auth.signup'))'''
        
        #hashed_password = generate_password_hash(password, method='scrypt')

        # Create new user instance
        #new_user = User(user_id=user_id, password=hashed_password, name=name, address=address, role=role, phoneNumber=phone_number)
        new_user = TableClasses.Users(user_id=user_id, password=password, name=name, address=address, role=role, phone_number=phone_number)
        from app import db
        # Save to database
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.login'))  # Redirect to login page after successful sign up
    
    return render_template('signup.html')

    # result = executeCommit(
    #     "INSERT INTO Users (`user_id`, `password`, `name`, `address`, `role`, 'phone_number') VALUES (%s, %s, %s, %s, %s, %s)", 
    #     (user_id, hashed_password, name, address, role, phone_number)
    # )
    # # If the insert was successful, redirect to login page
    # if result:
    #     flash("Sign-up successful! Please log in.")
    #     return redirect( url_for('auth.login'))
    # else:
    #     flash("An error occurred while creating your account. Please try again.")
    #     return redirect(url_for('auth.signup'))
    # print(result)
    
    # return redirect(url_for('auth.login'))

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