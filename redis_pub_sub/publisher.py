import redis
import json

r = redis.Redis(
    host="flask-socketio-load-balancing-redis",
    port=6379,
    decode_responses=True
)


def publish(redis_channel, data):
    data_bytes = json.dumps(data).encode("utf-8")
    r.publish(redis_channel, data_bytes)