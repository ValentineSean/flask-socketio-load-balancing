import json
import traceback

from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

# Configurations
from config.socket import socketio

# Events
from events.join_room import join_room
from events.send_message import send_message
from events.get_server_address import get_server_address

app = Flask(__name__)
CORS(app)
# socketio.init_app(app)


def create_app():
    # SocketIO
    # socketio.init_app(app, cors_allowed_origins=["http://localhost:6001"])
    socketio.init_app(app, cors_allowed_origins=["http://localhost:6001"], message_queue="redis://flask-socketio-load-balancing-redis:6379")
    return app

app = create_app()