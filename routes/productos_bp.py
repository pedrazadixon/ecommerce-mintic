from flask import Blueprint
from controllers.ProductosController import index, agregar, ver, actualizar, eliminar

productos_bp = Blueprint('productos_bp', __name__)
productos_bp.route('/', methods=['GET'])(index)
productos_bp.route('/agregar', methods=['GET', 'POST'])(agregar)
productos_bp.route('/<int:id>', methods=['GET'])(ver)
productos_bp.route('/actualizar/<int:id>', methods=['GET', 'POST'])(actualizar)
productos_bp.route('/eliminar', methods=['POST'])(eliminar)
