# ecommerce - mintic

## Demo

Ver app en pythonanywhere: https://pedrazadixon.pythonanywhere.com/

Credenciales:

- super : super
- admin : admin
- usuariofinal : usuariofinal

## Instalación

1. Instalar dependencias usando el comando:

   `python -m pip install -r requirements.txt`

2. crear base de datos sqlite, crear tables y crear usuarios de prueba usando el comando:

   `flask db upgrade`

3. Iniciar servidor

   `python app.py`

4. Ingresar a la aplicación en el sitio `http://127.0.0.1:5000/` e iniciar sesión usando cualquiera de las siguientes credenciales:

- super : super
- admin : admin
- usuariofinal : usuariofinal

## Actualizar modelo db (opcional)

1. eliminar el archivo ecommerce.db
2. actualiza las tablas con base a los nuevos modelos
   `flask db upgrade`
