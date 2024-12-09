from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.TableClasses import Users, add_user

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
    name = request.form.get('name')
    address = request.form.get('address')
    role = request.form.get('role')
    phone_number = request.form.get('phone_number')

    print(f"Received form data: Name={name}, Address={address}, Role={role}, Phone Number={phone_number}")

    if not name or not address or not role or not phone_number:
        flash('All fields are required!', 'danger')
        return redirect(url_for('views.signup'))

    try:
        add_user(name, address, role, phone_number)  # Call to add_user function
        flash('Signup successful!', 'success')
        return redirect(url_for('views.signup'))
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('views.signup'))