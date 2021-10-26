from flask import Flask
from .config import DevConfig



#Initializing our app

app= Flask(__name__,instance_relative_config = True)  # app instances we pass instance_config as the argument.


# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
