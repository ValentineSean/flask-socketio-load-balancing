import socket

from flask_socketio import emit, join_room
from config.socket import socketio

# WEBSOCKET
@socketio.on("join-room")
def join_room(data):
    server_address = socket.gethostname()
    username = data.get("username")
    room = data.get("room")

    # join_room(room)

    # REDIS PUBLISH
    data = {
        "server_address": server_address,
        "user_name": username,
        "room_name": room,
        "version": 1,
    }

    # emit("join-room-response", data, room=room_name)
    # emit("join-room-response", data)
    # socketio.emit("join-room-response", data, to=room_name)
    socketio.emit("join-room-response", data)