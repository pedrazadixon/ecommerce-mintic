import sys
from flask import render_template, redirect, sessions, url_for, request, abort, flash, session
from models.Comentario import Comentario as comentario_model
from models.Producto import Producto as producto_model
from forms.comentarios.form import Form as ComentarioForm


def index():
    comentarios = comentario_model.query.filter_by(com_usuario_id=session['auth_id']).join(producto_model, comentario_model.com_producto_id == producto_model.pro_id).add_columns(
        comentario_model.com_id, comentario_model.com_comentario, producto_model.pro_id, producto_model.pro_nombre)
    return render_template('comentarios/index.html', comentarios=comentarios)


def agregar(prodId):
    form = ComentarioForm()
    errors = []

    if request.method == 'POST' and form.validate_on_submit():
        comentario = comentario_model()
        form.populate_obj(comentario)
        comentario.com_usuario_id = session['auth_id']
        comentario.com_producto_id = prodId
        result = comentario.save()
        if result != True:
            errors.append(result)
            print(errors)
        else:
            flash('Agregado correctamente.', 'success')
            return redirect(url_for('tienda_bp.producto', id=prodId, _anchor='comentarios'))


def actualizar(id):
    form = ComentarioForm()
    errors = []

    comentario = comentario_model.query.filter_by(com_id=id).first()
    producto = producto_model.query.filter_by(
        pro_id=comentario.com_producto_id).first()

    # Datos traidos de la db para el formulario
    form.com_comentario.data = comentario.com_comentario

    if request.method == 'POST' and form.validate_on_submit():
        # datos a actualizar en la db
        comentario.com_comentario = request.form.get("com_comentario")

        actualizar_comentario = comentario_model()
        result = actualizar_comentario.actualizar()
        if result != True:
            errors.append(result)
        else:
            flash('Actualizado correctamente.', 'success')
            return redirect(url_for('comentarios_bp.index'))
    return render_template('comentarios/actualizar.html', comentario=comentario, producto=producto, form=form, errors=errors)


def eliminar():
    id = request.form.get("inp-eliminar-id")
    registro = comentario_model.query.filter_by(com_id=id).first()
    comentario_model.eliminar(registro)
    flash('Eliminado correctamente.', 'info')
    return redirect(url_for('comentarios_bp.index'))
