import socket

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

app_demo = Flask(__name__)
CORS(app_demo)
socketio = SocketIO(logger=True, engineio_logger=True)
socketio.init_app(app_demo)

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

if __name__ == "__main__":
    pywsgi.WSGIServer(("", 5009), app_demo,
        handler_class=WebSocketHandler
    ).serve_forever()