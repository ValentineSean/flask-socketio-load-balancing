import socket

from flask_socketio import emit, join_room
from config.socket import socketio

# WEBSOCKET
@socketio.on("send-message")
def send_message(data):
    server_address = socket.gethostname()
    sender = data.get("username")
    if sender is not None:
        sender = sender.upper()
    text_message = data.get("text_message")

    message = {
        "server_address": server_address,
        "sender": sender,
        "text_message": text_message,
    }

    socketio.emit("receive-message", message)