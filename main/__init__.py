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

app = Flask(__name__)
CORS(app)
socketio.init_app(app)


def create_app():
    # SocketIO
    socketio.init_app(app, cors_allowed_origin="*")
    return app

app = create_app()