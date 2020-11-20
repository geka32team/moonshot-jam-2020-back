from flask import current_app, request


def handler():
    current_app.logger.debug(f"connect namespace '{request.namespace}'")
