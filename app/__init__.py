from flask import Flask

#Initializing our app

app= Flask(__name__)  # app instances


from app import views
