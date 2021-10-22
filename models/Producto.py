from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()


class Producto(db.Model):
    __tablename__ = 'productos'
    pro_id = db.Column(db.Integer, primary_key=True)
    pro_nombre = db.Column(db.String)
    pro_precio = db.Column(db.Float)
    pro_descripcion = db.Column(db.String)
    pro_creado = db.Column(db.DateTime)
    pro_img = db.Column(db.String)

    @ property
    def serialize(self):
        return {
            'pro_id': self.pro_id,
            'pro_nombre': self.pro_nombre,
            'pro_precio': self.pro_precio,
            'pro_descripcion': self.pro_descripcion,
            'pro_creado': self.pro_creado,
            'pro_img': self.pro_img
        }

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error
        finally:
            db.session.close()
    

    def eliminar(registro):
        try:
            db.session.delete(registro) 
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error
        finally:
            db.session.close()

    def actualizar(self):
        try:
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error
        finally:
            db.session.close()