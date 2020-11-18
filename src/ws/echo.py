#  from flask_socketio import emit, send

#  from flask import Blueprint, request, current_app, session
from flask import current_app
#  from flask_json import json_response, JsonError
#
#  from ..auth import signin_required
#
#  bp = Blueprint("ws.ping", __name__, url_prefix="/ws")
#


def handler(message):
    current_app.logger.debug(
        f"on_message: '{message}'")
    return "echo: " + message


#  @socketio.on('message')
#  def handle_message(message):
#      current_app.logger.error(
#          f"ws: recevied message: '{message}'")

#  class Namespace(_Namespace):
#      def on_connect(self):           # pylint: disable=no-self-use
#          current_app.logger.error(
#              "ws: ping: connected")
#          send("nice to see you!")
#
#      def on_disconnect(self):        # pylint: disable=no-self-use
#          current_app.logger.error(
#              "ws: ping: disconnected")
#
#      def on_message(self, message):  # pylint: disable=no-self-use
#          current_app.logger.error(
#              "ws: ping: on_message: '{message}'")
#          emit('pong', "pong :" + message)


#  @bp.route("/signout", methods=["POST"])
#  @signin_required
#  def signin():
#      """Sign out a signed in user. Clear session."""
#      data = request.get_data()
#
#      if data:                        # pragma: no cover
#          current_app.logger.error(
#              f'no data is expected, but recevied {len(data)} bytes.')
#          raise JsonError(message='bad request')
#
#      session.clear()
#
#      return json_response()
