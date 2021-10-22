import sys
from flask import render_template, redirect, url_for, request, abort
from models.Producto import Producto as producto_model
from models.Comentario import Comentario as comentario_model
from forms.comentarios.form import Form as ComentarioForm
from models.Usuario import Usuario as usuario_model


def producto(id):
    form = ComentarioForm()
    errors = []

    producto = producto_model.query.filter_by(pro_id=id).first()

    comentarios = comentario_model.query.filter_by(com_producto_id=id).join(usuario_model, comentario_model.com_usuario_id == usuario_model.usu_id).add_columns(
        comentario_model.com_id, comentario_model.com_comentario, usuario_model.usu_nombres, usuario_model.usu_apellidos).all()

    return render_template('tienda/producto.html', producto=producto, form=form, errors=errors, comentarios=comentarios)
