from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()


class ListaDeDeseo(db.Model):
    __tablename__ = 'lista_de_deseos'
    lis_id = db.Column(db.Integer, primary_key=True)
    lis_usuario_id = db.Column(db.Integer)
    lis_producto_id = db.Column(db.Integer)

    @ property
    def serialize(self):
        return {
            'lis_id': self.lis_id,
            'lis_usuario_id': self.lis_usuario_id,
            'lis_producto_id': self.lis_producto_id
        }

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error
    
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