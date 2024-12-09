from flask import Flask
from app.views import views  
from app.TableClasses import db

def create_app():
    app = Flask(__name__)

     # Set app configurations 
    app.config['SECRET_KEY'] = 'SoilMarketKey123'  # Ensure this is random/secure in production
    app.config['SQLALCHEMY_DATABASE_URI'] = 'root@localhost:3306'  # Update with correct values
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the db with the apps
    db.init_app(app)

    app.register_blueprint(views)
    return app

