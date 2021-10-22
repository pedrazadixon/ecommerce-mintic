from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    usu_id = db.Column(db.Integer, primary_key=True)
    usu_usuario = db.Column(db.String)
    usu_email = db.Column(db.String)
    usu_password = db.Column(db.String)
    usu_rol = db.Column(db.String)
    usu_nombres = db.Column(db.String)
    usu_apellidos = db.Column(db.String)

    @ property
    def serialize(self):
        return {
            'usu_id': self.usu_id,
            'usu_usuario': self.usu_usuario,
            'usu_email': self.usu_email,
            'usu_password': self.usu_password,
            'usu_rol': self.usu_rol,
            'usu_nombres': self.usu_nombres,
            'usu_apellidos': self.usu_apellidos
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
