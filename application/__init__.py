from flask import Flask, request, jsonify
import time
import threading
from flask_bcrypt import Bcrypt

app = Flask(__name__)
flask_bcrypt = Bcrypt(app)
lock = threading.Lock()
app.config.from_object('application.settings')

from application.decorators import authenticate_user


@app.route("/me", methods=["GET", "POST"])
@authenticate_user
def func(*args, **kwargs):

    auth = request.authorization
    delay = request.args.get("delay")
    incr = request.args.get("increment")
    username = auth.username

    lock.acquire()
    with open(app.config.get('COUNTER_INF_PATH'), "r") as f:
        line = (f.read()).strip()
        if line:
            counter = int(line)
        else:
            counter = 0

    counter += int(incr)
    with open(app.config.get('COUNTER_INF_PATH'), "w") as f:
        f.write(str(counter))

    lock.release()
    time.sleep(float(delay))

    return jsonify(username=username, counter=counter, delay=delay)
