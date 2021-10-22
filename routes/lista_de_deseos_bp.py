from flask import Blueprint
from controllers.ListaDeDeseosController import index,eliminar, agregar

lista_de_deseos_bp = Blueprint('lista_de_deseos_bp', __name__)
lista_de_deseos_bp.route('/', methods=['GET'])(index)
lista_de_deseos_bp.route('/agregar/<int:id>', methods=['GET','POST'])(agregar)
lista_de_deseos_bp.route('/eliminar', methods=['POST'])(eliminar)