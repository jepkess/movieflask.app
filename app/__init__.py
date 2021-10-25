from flask import Flask
from .config import Devconfig

#Initializing our app

app= Flask(__name__)  # app instances

#setting up the configuration
app.config.from_object(Devconfig)


from app import views
