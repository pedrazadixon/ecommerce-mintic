from flask import Blueprint
from controllers.UsuariosController import index, agregar, ver, actualizar, eliminar, iniciarSesion, registrarse, cerrarSesion

usuarios_bp = Blueprint('usuarios_bp', __name__)
usuarios_bp.route('/', methods=['GET'])(index)
usuarios_bp.route('/iniciar-sesion', methods=['GET', 'POST'])(iniciarSesion)
usuarios_bp.route('/cerrar-sesion', methods=['GET'])(cerrarSesion)
usuarios_bp.route('/registrarse', methods=['GET', 'POST'])(registrarse)
usuarios_bp.route('/agregar', methods=['GET', 'POST'])(agregar)
usuarios_bp.route('/<int:id>', methods=['GET'])(ver)
usuarios_bp.route('/actualizar/<int:id>', methods=['GET', 'POST'])(actualizar)
usuarios_bp.route('/eliminar', methods=['POST'])(eliminar)
