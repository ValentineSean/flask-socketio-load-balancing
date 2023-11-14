import socket

from flask import Flask, jsonify
from flask_socketio import SocketIO
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)
socketio = SocketIO(logger=True, engineio_logger=True)

socketio.init_app(app)

# HTTP
@app.route("/home")
def home():
    print("shall we play a game...")
    return f"Container ID: {socket.gethostname()}"

# Command to fire up containers: 'docker-compose up -d --force-recreate --build --scale [SERVICE_NAME]=3'

"""
    02 August 2023:
        -> Server fires up 3 instances (Docker containers)...
        -> But the system is using only 1 instance for socketIO...
        -> NGINX: 'upstream' is only promising solution at the moment...

        -> Possible Solutions:
            - https://www.nginx.com/resources/glossary/layer-4-load-balancing/
            - https://www.quora.com/Is-it-possible-to-scale-Socket-io-vertically-without-Redis
            - https://ably.com/topic/scaling-socketio
            - There is need of SYNC Mechanism, eg Redis Adapter (Pub/Sub) or equivalent


            - https://www.youtube.com/watch?v=x-ydCL8pj40&list=TLPQMjcxMDIwMjNYZcPqAAI1jQ&index=1&pp=gAQBiAQB  
            - https://www.youtube.com/watch?v=DJBXOmyhAKM&list=TLPQMjcxMDIwMjNYZcPqAAI1jQ&index=2&pp=gAQBiAQB
            - https://www.youtube.com/watch?v=gzIcGhJC8hA&list=TLPQMjcxMDIwMjNYZcPqAAI1jQ&index=3&pp=gAQBiAQB
            - https://www.youtube.com/watch?v=xtCddOjITvo&list=TLPQMjcxMDIwMjNYZcPqAAI1jQ&index=4&pp=gAQBiAQB
"""


# WEBSOCKET
@socketio.on("home")
def socket_home(data):
    print("This is socket home...")

    socketio.emit("home-response", f">HOME RESPONSE: {socket.gethostname()}")


if __name__ == "__main__":
    pywsgi.WSGIServer(("", 5000), app,
        handler_class=WebSocketHandler
    ).serve_forever()