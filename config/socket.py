from gevent import monkey
monkey.patch_all()

from flask_socketio import SocketIO

socketio = SocketIO(logger=True, engineio_logger=True)