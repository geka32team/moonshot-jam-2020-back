from . import (
    global_connect,
    public_connect,
    api_connect,
    echo,
)
from .namespace import Namespace as ns


def register_all(app):
    app.on_event('connect', global_connect.handler)

    app.on_event('connect', public_connect.handler, namespace=ns.PUBLIC)

    app.on_event('connect', api_connect.handler, namespace=ns.API)
    app.on_event('echo', echo.handler, namespace=ns.API)
