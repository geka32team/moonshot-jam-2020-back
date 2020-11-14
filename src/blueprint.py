from . import api


def register_all(app):
    app.register_blueprint(api.register.bp)
    app.register_blueprint(api.signin.bp)
    app.register_blueprint(api.signout.bp)
