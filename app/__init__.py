# from flask import Flask
# from app.views import views 

# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(views)
#     return app


from flask import Flask
from flask_login import LoginManager
from app import views, auth, api
from .models.user import User
CONFIG_FILE = "../config.py"

def create_app():
    app = Flask(__name__)
    app.register_blueprint(views.blueprint)
    app.register_blueprint(api.api)
    app.config.from_pyfile(CONFIG_FILE)

    #Setup Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'views.login' 
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.findMatchOR(('user_id',), (user_id))

    return app
