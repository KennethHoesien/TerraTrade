from flask import Blueprint, render_template

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

