import json
import os
import sentry_sdk
from bson import ObjectId
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask.json import JSONEncoder
from sentry_sdk.integrations.flask import FlaskIntegration

import db_helper.mongodb_connect as dbc

load_dotenv()

sentry_sdk.init(
    dsn="https://d67b87bf0c65453d939925d6676eb31d@o358880.ingest.sentry.io/6741779",
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

# Set up the app and point it to Vue
app = Flask(__name__, static_folder='dist/', static_url_path='/')


# json load of mongodb file
class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)


app.json_encoder = MongoJSONEncoder


# sentry verification
@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0


# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/influco.api', methods=['get'])
def hello_backend():
    """create new order"""
    try:
        number = request.args.get("number")
        res = "Hello, InfluCo backend!"
    except Exception:
        return jsonify("error")
    return jsonify(res)


@app.route('/influco.api/influencer/<string:influencer_id>', methods=['get'])
def get_one_influencer(influencer_id):
    """create new order"""
    try:
        # number = request.args.get("influencer_id")
        res = dbc.get_one_influencer(influencer_id)
    except Exception:
        return jsonify("error")
    return jsonify(res)


@app.route('/influco.api/user/<string:username>', methods=['get'])
def get_one_user(username):
    """get info for one user"""
    res = []
    try:
        res = dbc.get_one_user(username)
    except Exception:
        return jsonify("error")
    return jsonify(res)


@app.route('/influco.api/user/<string:username>', methods=['post'])
def register_one_user(username):
    """get info for one user"""
    res = "Empty username!"
    try:
        user_info = request.json
        # create if not exist in db
        if not dbc.get_one_user(username):
            res = dbc.insert_one_user(user_info)
        else:
            res = "Username already exist!!!"
    except Exception:
        return jsonify("Error")
    return jsonify(res)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
