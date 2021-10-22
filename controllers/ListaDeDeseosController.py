import sys
from flask import render_template, redirect, url_for, request, abort, flash, session
from models.ListaDeDeseo import ListaDeDeseo as lista_de_deseos_model
from models.Producto import Producto as producto_model

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()


def index():
    if session['auth_rol'] == "usuariofinal":
        lista_de_deseos = lista_de_deseos_model.query.filter_by(lis_usuario_id = session['auth_id']).join(producto_model, lista_de_deseos_model.lis_producto_id== producto_model.pro_id).add_columns(lista_de_deseos_model.lis_id,producto_model.pro_id, producto_model.pro_nombre)
        print(lista_de_deseos)
    else:
        lista_de_deseos = lista_de_deseos_model.query.join(producto_model, lista_de_deseos_model.lis_producto_id== producto_model.pro_id).add_columns(lista_de_deseos_model.lis_id,producto_model.pro_id, producto_model.pro_nombre)
    
    return render_template('lista_de_deseos/index.html', lista_de_deseos=lista_de_deseos)

def eliminar():
    id = request.form.get("inp-eliminar-id")
    registro = lista_de_deseos_model.query.filter_by(lis_id=id).first()
    lista_de_deseos_model.eliminar(registro)
    flash('Eliminado correctamente.', 'info')
    return redirect(url_for('lista_de_deseos_bp.index'))

def agregar(id):
    errors = []

    # valido si ya tiene el producto en el carrito
    valida_deseo = lista_de_deseos_model.query.filter_by(lis_producto_id=id ,lis_usuario_id = session['auth_id']).count()

    if valida_deseo == 0:
        elemento_lista_deseo = lista_de_deseos_model()
        elemento_lista_deseo.lis_producto_id = id
        elemento_lista_deseo.lis_usuario_id  = session['auth_id']
        result = elemento_lista_deseo.save()
        if result != True:
            errors.append(result)
            print(errors)
        else:
            flash('Agregado correctamente.', 'success')
            return redirect(url_for('lista_de_deseos_bp.index'))
    else:
        flash('Ya contiene este producto en la lista de deseos', 'danger')
        return redirect(url_for('lista_de_deseos_bp.index'))
        
    return redirect(url_for('lista_de_deseos_bp.index'))