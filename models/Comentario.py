from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()


class Comentario(db.Model):
    __tablename__ = 'comentarios'
    com_id = db.Column(db.Integer, primary_key=True)
    com_comentario = db.Column(db.String)
    com_usuario_id = db.Column(db.Integer)
    com_producto_id = db.Column(db.Integer)

    @ property
    def serialize(self):
        return {
            'com_id': self.com_id,
            'com_comentario': self.com_comentario,
            'com_usuario_id': self.com_usuario_id,
            'com_producto_id': self.com_producto_id
        }

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
