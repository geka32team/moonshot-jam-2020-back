from . import (
    signin,
    register,
    signout,
)


def register_all(app):
    app.register_blueprint(register.bp)
    app.register_blueprint(signin.bp)
    app.register_blueprint(signout.bp)
