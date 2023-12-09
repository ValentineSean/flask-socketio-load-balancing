import socket

from flask_socketio import emit, join_room
from config.socket import socketio

# WEBSOCKET
@socketio.on("get-server-address")
def get_server_address(data):
    server_address = socket.gethostname()

    data = {
        "server_address": server_address,
    }

    emit("receive-server-address", data)