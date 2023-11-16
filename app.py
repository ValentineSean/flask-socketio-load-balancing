from gevent import monkey
monkey.patch_all()

import socket
import redis
import json

from flask import Flask, jsonify
from flask_socketio import SocketIO
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from redis_pub_sub.publisher import publish
from redis_pub_sub.subscriber import subscribe

app = Flask(__name__)
# socketio = SocketIO(logger=True, engineio_logger=True, message_queue="redis://0.0.0.0:5002")
socketio = SocketIO(logger=True, engineio_logger=True, message_queue="redis://flask-socketio-load-balancing-redis:6379")

socketio.init_app(app)

# # REDIS CONNECTION
# r = redis.Redis(
#     host="flask-socketio-load-balancing-redis",
#     port=6379,
#     decode_responses=True
# )

# HTTP
@app.route("/home")
def home():
    print("shall we play a game...")
    redis_channel = "DEFCON-2"
    server_address = socket.gethostname()


    return f"Container ID: {socket.gethostname()}"

# Command to fire up containers: 'docker-compose up -d --force-recreate --build --scale [SERVICE_NAME]=3 --remove-orphans'

"""
    02 August 2023:
        -> Server fires up 3 instances (Docker containers)...
        -> But the system is using only 1 instance for socketIO...
            - It is now randomly changing from 1 instance to 2 instances (AFTER ADDING MONKEY PATCHING && REDIS MESSAGE QUEUE ARGUMENT), but not yet sure how:
                - https://flask-socketio.readthedocs.io/en/latest/deployment.html#using-multiple-workers
            -
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
    redis_channel = "DEFCON-1"
    print("This is socket home...")
    subscriber_message = dict()

    server_address = socket.gethostname()
    client_os = data['client_os']

    # REDIS PUBLISH
    data = {
        "server_address": server_address,
        "client_os": client_os,
    }
    # publish(redis_channel=redis_channel, data=data)

    # # REDIS SUBSCRIBE
    # subscriber_message = subscribe(redis_channel)

    socketio.emit("home-response", f">SERVER ADDRESS: {server_address}, CLIENT OS: {client_os}")
    # socketio.emit("home-response", subscriber_message)


if __name__ == "__main__":
    pywsgi.WSGIServer(("", 5000), app,
        handler_class=WebSocketHandler
    ).serve_forever()