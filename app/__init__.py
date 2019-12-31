from flask import Flask
# from flask_cors import CORS
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address


def register_blueprints(app):
    from app.api.cms import bp_cms
    from app.api.v1 import bp_v1
    app.register_blueprint(bp_cms, url_prefix='/cms')
    app.register_blueprint(bp_v1, url_prefix='/v1')


# def apply_cors(app):
#     CORS(app)

def create_tables(app):
    from app.libs.db import db
    with app.app_context():
        db.create_all()

def create_app(environment='production'):
    app = Flask(__name__, static_folder='./api/static')
    app.config['ENV'] = environment
    env = app.config.get('ENV')
    if env == 'production':
        app.config.from_object('app.config.setting.ProductionConfig')
        app.config.from_object('app.config.secure.ProductionSecure')
    elif env == 'development':
        app.config.from_object('app.config.setting.DevelopmentConfig')
        app.config.from_object('app.config.secure.DevelopmentSecure')

    # Limiter(key_func=get_remote_address, headers_enabled=True, default_limits=["1000/minute"]).init_app(app)
    register_blueprints(app)
    # apply_cors(app)
    # 创建所有表格
    # create_tables(app)

    return app



