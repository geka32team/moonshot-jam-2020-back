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
    #  app.on_event('echo', echo.handler, namespace=ns.API)

    #
    #  from flask_socketio import join_room, leave_room, send, emit, rooms
    #  from flask import request
    #
    #  def message(message):
    #      print("'room111' handler")
    #      send(message, room="room111", include_self=False)
    #
    #  app.on_event("room111", message, namespace=ns.API)
    #
    #  def on_join(data):
    #      print(f"'on_join' handler, data = {data}")
    #      username = data['username']
    #      room = data['room']
    #      join_room(room)
    #      rms=rooms()
    #      print(f"rooms = {rms}")
    #      send(f'{username} has entered the room. sid={request.sid}', room=room, include_self=False)
    #      emit('lobby', f'lobby: {username} has entered the room. sid={request.sid}', room=room)
    #
    #  app.on_event("join", on_join, namespace=ns.API)
    #
