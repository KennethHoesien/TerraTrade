from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.TableClasses import Users

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("index.html")

@views.route('/listing')
def listing():
    return render_template('listing.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/signup')
def signup_form():
    return render_template('signup.html')

@views.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    address = request.form['address']
    role = request.form['role']
    phone_number = request.form['phone_number']

    if not name or not address or not role or not phone_number:
        flash('All fields are required!', 'danger')
        return redirect(url_for('views.signup_form'))

    try:
        # Use the static method from Users class to add a new user
        Users.add_user(name, address, role, phone_number)
        flash('User signed up successfully!', 'success')
        return redirect(url_for('views.signup_form'))
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('views.signup_form'))