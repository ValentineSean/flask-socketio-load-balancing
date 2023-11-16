FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
# CMD gunicorn --bind 0.0.0.0:5000 app:app
ENTRYPOINT gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 app:app -b 0.0.0.0:5003