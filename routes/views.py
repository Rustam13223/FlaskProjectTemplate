from flask import Blueprint
from controllers.ViewsController import home

views = Blueprint('views', __name__)

views.route('/', methods=["GET"])(home)
