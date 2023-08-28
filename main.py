import logging
from threading import Thread

from flask import Response, app, Flask
from flask_cors import CORS

from objects.Camera import Camera
from objects.Config import Config

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

config = Config("config.ini")

camera = Camera(config.camera_stream_link(), config.camera_refresh_rate())

app = Flask(__name__)
CORS(app)


@app.route("/stream")
def stream():
    return Response(camera.read(), mimetype='multipart/x-mixed-replace; boundary=frame')


def run_api():
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    thread = Thread(target=run_api)
    thread.daemon = True
    thread.start()

while True:
    pass
