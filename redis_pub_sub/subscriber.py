import redis
import json

r = redis.Redis(
    host="flask-socketio-load-balancing-redis",
    port=6379,
    decode_responses=True
)


def subscribe(redis_channel):
    subsriber_message = dict()
    mobile = r.pubsub()
    mobile.subscribe(redis_channel)

    for message in mobile.listen():
        if isinstance(message["data"], str):
            # Convert data bytes to dictionary (DECODING)
            subsriber_message = json.loads(message["data"])

    return subsriber_message