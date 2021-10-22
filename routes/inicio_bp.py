from flask import Blueprint
from controllers.InicioController import index

inicio_bp = Blueprint('inicio_bp', __name__)
inicio_bp.route('/', methods=['GET'])(index)
