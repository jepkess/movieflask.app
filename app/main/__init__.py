from flask import Blueprint
main = Blueprint('main',__name__) # blueprint takes in argument main as the name of the blueprint and __name__ to finds the location of the blueprint.
from . import views,error