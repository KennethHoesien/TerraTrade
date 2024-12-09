from flask import Blueprint, render_template, request, redirect, url_for, flash

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return render_template("index.html")

@views.route('/listing')
def listing():
    return render_template('listing.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

# @views.route('/login')
# def index():
#     return render_template('index.html')

# @views.route('/signup')
# def signup():
#     return render_template('signup.html')
