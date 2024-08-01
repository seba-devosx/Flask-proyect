import os

from flask import Flask
from . import db
from . import auth

def create_app(test_config=None):
    # crea la instancia y la configura
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # cargar la configuración de la instancia, si existe, cuando no se esté probando
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # asegura de que la carpeta de la instancia exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # ruta para cuando se crea la app
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    
    db.init_app(app)

    
    app.register_blueprint(auth.bp)

    return app