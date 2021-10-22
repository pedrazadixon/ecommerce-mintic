import sys
from flask import render_template, redirect, url_for, request, abort, flash, session
from models.Usuario import Usuario as usuario_model
from forms.usuarios.agregar import Form as UsuarioForm
from werkzeug.security import generate_password_hash, check_password_hash


def index():
    usuarios = usuario_model.query.all()
    return render_template('usuarios/index.html', usuarios=usuarios)


def agregar():
    form = UsuarioForm()
    errors = []

    if request.method == 'POST' and form.validate_on_submit():
        nuevo_usuario = usuario_model()
        form.populate_obj(nuevo_usuario)
        nuevo_usuario.usu_password = generate_password_hash(
            nuevo_usuario.usu_password)
        result = nuevo_usuario.save()
        if result != True:
            errors.append(result)
        else:
            flash('Agregado correctamente.', 'success')
            return redirect(url_for('usuarios_bp.index'))

    return render_template('usuarios/agregar.html', form=form, errors=errors)


def ver(id):
    usuario = usuario_model.query.filter_by(usu_id=id).first()
    form = UsuarioForm(request.form, obj=usuario)
    return render_template('usuarios/ver.html', form=form)


def actualizar(id):
    usuario = usuario_model.query.filter_by(usu_id=id).first()
    form = UsuarioForm(request.form, obj=usuario)
    errors = []

    form.usu_password.validators = []
    form.usu_password2.validators = []

    if request.method == 'POST' and form.validate_on_submit():
        old_password = usuario.usu_password
        form.populate_obj(usuario)

        # si el campo password viene vacio, dejo la contrase anterior, de lo contrario hasheo el nuevo password
        if request.form.get("usu_password") == '':
            usuario.usu_password = old_password
        else:
            usuario.usu_password = generate_password_hash(
                usuario.usu_password)

        result = usuario.actualizar()
        if result != True:
            errors.append(result)
        else:
            flash('Actualizado correctamente.', 'success')
            return redirect(url_for('usuarios_bp.index'))

    return render_template('usuarios/actualizar.html', form=form, errors=errors)


def eliminar():
    id = request.form.get("inp-eliminar-id")
    registro = usuario_model.query.filter_by(usu_id=id).first()
    usuario_model.eliminar(registro)
    flash('Eliminado correctamente.', 'info')
    return redirect(url_for('usuarios_bp.index'))


def iniciarSesion():
    if 'auth_id' in session:
        return redirect(url_for('inicio_bp.index'))

    if request.method == 'POST':
        if _validarCredenciales(request.form.get("usu_usuario"), request.form.get("usu_password")):
            flash('Bienvenido ' + request.form.get("usu_usuario") +
                  '. Puedes pulsar en el boton "My Dashboard" para administrar tu cuenta.', 'success')
            return redirect(url_for('index'))
        flash('Credenciales incorrectas.', 'danger')

    return render_template('usuarios/iniciar_sesion.html')


def cerrarSesion():
    session.pop('auth_id', None)
    session.pop('auth_usuario', None)
    session.pop('auth_nombres', None)
    session.pop('auth_apellidos', None)
    session.pop('auth_rol', None)
    return redirect(url_for('index'))


def _validarCredenciales(usuario, password):
    objUsuario = usuario_model.query.filter_by(usu_usuario=usuario).first()

    if objUsuario is None:
        return False

    if not check_password_hash(objUsuario.usu_password, password):
        return False

    # credencailes correctas
    session['auth_id'] = objUsuario.usu_id
    session['auth_usuario'] = objUsuario.usu_usuario
    session['auth_nombres'] = objUsuario.usu_nombres
    session['auth_apellidos'] = objUsuario.usu_apellidos
    session['auth_rol'] = objUsuario.usu_rol

    return True


def registrarse():
    form = UsuarioForm()
    errors = []

    form.usu_rol.validators = []

    form.usu_rol.data = 'usuariofinal'

    if request.method == 'POST' and form.validate_on_submit():
        nuevo_usuario = usuario_model()
        form.populate_obj(nuevo_usuario)
        nuevo_usuario.usu_password = generate_password_hash(
            nuevo_usuario.usu_password)
        result = nuevo_usuario.save()
        if result != True:
            errors.append(result)
        else:
            flash('Registrado correctamente. Ya puedes iniciar sesion.', 'success')
            return redirect(url_for('index'))

        print(errors)

    return render_template('usuarios/registrarse.html', form=form, errors=errors)
