from flask import Blueprint
from controllers.TiendaController import producto

tienda_bp = Blueprint('tienda_bp', __name__)
tienda_bp.route('/<int:id>', methods=['GET'])(producto)
