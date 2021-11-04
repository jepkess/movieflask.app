from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views, forms # forms that register new users in the application.


  
