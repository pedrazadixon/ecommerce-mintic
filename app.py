from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from routes._middleware import permisos_bp
from routes.usuarios_bp import usuarios_bp
from routes.inicio_bp import inicio_bp
from routes.lista_de_deseos_bp import lista_de_deseos_bp
from routes.tienda_bp import tienda_bp
from routes.productos_bp import productos_bp
from routes.comentarios_bp import comentarios_bp
from models.Producto import Producto as producto_model


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
app.register_blueprint(inicio_bp, url_prefix='/inicio')
app.register_blueprint(lista_de_deseos_bp, url_prefix='/lista-de-deseos')
app.register_blueprint(tienda_bp, url_prefix='/tienda')
app.register_blueprint(productos_bp, url_prefix='/productos')
app.register_blueprint(comentarios_bp, url_prefix='/comentarios')

app.register_blueprint(permisos_bp)


@app.route('/')
def index():
    if request.args.get('q') is None:
        productos = producto_model.query.all()
    else:
        productos = producto_model.query.filter(
            producto_model.pro_nombre.ilike("%"+request.args.get('q')+"%")).all()
    return render_template('index.html', productos=productos)


if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run()
