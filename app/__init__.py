# from flask import Flask
# from app.views import views 

# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(views)
#     return app


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.views import views




CONFIG_FILE = "../config.py"

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    #app.register_blueprint(api.api)
    app.config.from_pyfile(CONFIG_FILE)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://liquid:1234@localhost/terratrade'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the db with the app
    db.init_app(app)

    #Setup Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'views.login' 
    login_manager.init_app(app)

    from app.auth import auth
    app.register_blueprint(views)
    app.register_blueprint(auth, url_prefix='/auth')
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        return User.findMatchOR(('user_id',), (user_id))

    return app
