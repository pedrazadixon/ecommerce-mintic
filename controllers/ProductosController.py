import sys
import os
from os import remove
from flask import render_template, redirect, url_for, request, abort, flash, Flask
from models.Producto import Producto as producto_model
from forms.productos.agregar import Form as AgregarProductoForm
import uuid


def index():
    products = producto_model.query.all()
    return render_template('productos/index.html', products=products)


def agregar():
    form = AgregarProductoForm()
    errors = []

    if request.method == 'POST' and form.validate_on_submit():
        nuevo_producto = producto_model()

        form.populate_obj(nuevo_producto)

        if form.pro_img.has_file():
            image_name, extension = os.path.splitext(
                form.pro_img.data.filename)
            image_name = str(uuid.uuid4()) + extension
            file_path = os.path.join("static/img/productos/", image_name)
            form.pro_img.data.save(file_path)
            nuevo_producto.pro_img = image_name

        result = nuevo_producto.save()
        if result != True:
            errors.append(result)
        else:
            flash('Agregado correctamente.', 'success')
            return redirect(url_for('productos_bp.index'))

    return render_template('productos/agregar.html', form=form, errors=errors)


def ver(id):
    product = producto_model.query.filter_by(pro_id=id).first()
    return render_template('productos/ver.html', product=product)


def actualizar(id):
    form = AgregarProductoForm()
    errors = []

    product = producto_model.query.filter_by(pro_id=id).first()

    # Datos traidos de la db para el formulario
    form.pro_nombre.data = product.pro_nombre
    form.pro_descripcion.data = product.pro_descripcion
    form.pro_precio.data = product.pro_precio

    if request.method == 'POST' and form.validate_on_submit():
        # datos a actualizar en la db
        product.pro_nombre = request.form.get("pro_nombre")
        product.pro_descripcion = request.form.get("pro_descripcion")
        product.pro_precio = request.form.get("pro_precio")

        if form.pro_img.has_file():
            image_name, extension = os.path.splitext(
                form.pro_img.data.filename)
            image_name = str(uuid.uuid4()) + extension
            file_path = os.path.join("static/img/productos/", image_name)
            remove("static/img/productos/" + product.pro_img)
            form.pro_img.data.save(file_path)
            product.pro_img = image_name

        actualizar_producto = producto_model()
        result = actualizar_producto.actualizar()
        if result != True:
            errors.append(result)
        else:
            flash('Actualizado correctamente.', 'success')
            return redirect(url_for('productos_bp.index'))
    return render_template('productos/actualizar.html', product=product, form=form, errors=errors)


def eliminar():
    id = request.form.get("inp-eliminar-id")
    registro = producto_model.query.filter_by(pro_id=id).first()
    remove("static/img/productos/" + registro.pro_img)
    producto_model.eliminar(registro)
    flash('Eliminado correctamente.', 'info')
    return redirect(url_for('productos_bp.index'))
