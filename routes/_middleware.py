from flask import Blueprint, request, session, redirect, url_for, flash

permisos_bp = Blueprint('permisos_bp', __name__)

permisos_globales = [
    'index',
    'usuarios_bp.iniciarSesion',
    'usuarios_bp.cerrarSesion',
    'usuarios_bp.registrarse',
    'tienda_bp.producto',
]

permisos_usuariofinal = permisos_globales + [
    'inicio_bp.index',
    'lista_de_deseos_bp.index',
    'lista_de_deseos_bp.eliminar',
    'lista_de_deseos_bp.agregar',
    'comentarios_bp.index',
    'comentarios_bp.actualizar',
    'comentarios_bp.eliminar',
    'comentarios_bp.agregar',
]

permisos_administrador = permisos_usuariofinal + [
    'productos_bp.index',
    'productos_bp.agregar',
    'productos_bp.ver',
    'productos_bp.actualizar',
    'productos_bp.eliminar',
]


def comprobarPermisos():

    if request.endpoint is not "static":

        # print(' ==** endpoint: %s' % (request.endpoint))

        if 'auth_id' not in session and request.endpoint not in permisos_globales:
            flash('Antes debe iniciar sesion.', 'warning')
            return redirect(request.referrer)

        if 'auth_rol' in session and session['auth_rol'] == 'usuariofinal':
            if request.endpoint not in permisos_usuariofinal:
                flash('Privilegios insufientes para acceder a este modulo.', 'warning')
                return redirect(request.referrer)

        if 'auth_rol' in session and session['auth_rol'] == 'administrador':
            if request.endpoint not in permisos_administrador:
                flash('Privilegios insufientes para acceder a este modulo.', 'warning')
                return redirect(request.referrer)


permisos_bp.before_app_request(comprobarPermisos)
