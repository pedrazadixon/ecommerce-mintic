from flask import Blueprint
from controllers.ComentariosController import index, actualizar, eliminar, agregar

comentarios_bp = Blueprint('comentarios_bp', __name__)
comentarios_bp.route('/', methods=['GET'])(index)
comentarios_bp.route('/agregar/<int:prodId>', methods=['POST'])(agregar)
comentarios_bp.route('/actualizar/<int:id>', methods=['GET', 'POST'])(actualizar)
comentarios_bp.route('/eliminar', methods=['POST'])(eliminar)
