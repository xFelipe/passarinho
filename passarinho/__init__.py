import os

from flask import Flask


def create_app(test_config=None):
    # Cria e configura o app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'passarinho.sqlite'),
    )

    if test_config is None:
        # Carrega a configuração de instância
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carrega a configuração de teste se passar
        app.config.from_mapping(test_config)

    # Garante que pasta da instância está criada
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    return app
