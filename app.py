from main import app
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

@app.route("/test")
def test():
    print("Testing HTTP")
    return "Testing HTTP Done"

if __name__ == "__main__":
    pywsgi.WSGIServer(("", 5003), app,
        handler_class=WebSocketHandler
    ).serve_forever()