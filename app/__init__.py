# from flask import Flask
# from config import DevConfig
# from flask_bootstrap import Bootstrap

# bootstrap = Bootstrap()



# #Initializing our app

# app= Flask(__name__,instance_relative_config = True)  # app instances we pass instance_config as the argument.


# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# # Initializing Flask Extensions
# bootstrap = Bootstrap(app)

# from app import views
# from app import error

from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE

login_manager = LoginManager()
login_manager.session_protection = 'strong'# session protection provides different security levels by setting to strong.
login_manager.login_view = 'auth.login'
mail=Mail()
simple=SimpleMDE()


bootstrap = Bootstrap()
db = SQLAlchemy()
photos=UploadSet('photos',IMAGES)

def create_app(config_name):

    app = Flask(__name__) #template_folder='templates'

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    #configure the Uploadset
    configure_uploads(app,photos)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app) #initializing the mail.
    simple.init_app(app)#initializing the simple editor markdown.

    
    # Registering the blueprint
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    # setting config
    from .requests import configure_request
    configure_request(app)
    return app
