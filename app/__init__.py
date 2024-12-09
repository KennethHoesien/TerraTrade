from flask import Flask
from app.views import views  
from app.TableClasses import db

def create_app():
    app = Flask(__name__)

<<<<<<< Updated upstream
     # Set app configurations 
    app.config['SECRET_KEY'] = 'SoilMarketKey123'  # Ensure this is random/secure in production
    app.config['SQLALCHEMY_DATABASE_URI'] = 'root@localhost:3306'  # Update with correct values
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
=======
    #app.register_blueprint(api.api)
    # In app initialization file (e.g., __init__.py or the main app file)
    app.config.from_pyfile('config.py')

    #print(app.config)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Chunniboy123#@localhost/soilmarket'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
>>>>>>> Stashed changes

    # Initialize the db with the apps
    db.init_app(app)

    app.register_blueprint(views)
    return app

