from flask import current_app


def handler():
    current_app.logger.debug("new connection")
