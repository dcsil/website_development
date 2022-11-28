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
@app.route('/', defaults={'path': ''})
@app.route("/<path>")
# @app.route("/popular")
def index(path):
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


@app.route('/influco.api/tag/<string:tag_str>', methods=['get'])
def get_influencers_by_tag(influencer_id):
    """return a influencers list by searching a specific tags"""
    try:
        # TODO: return a influencers list by searching a specific tags
        # If no influence have the searching tags return empty list
        res = []
        # Return error if and only if connection error
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


@app.route('/influco.api/register/<string:username>', methods=['post'])
def register(username):
    """get info for one user"""
    response_object = {'status':'fail'}
    try:
        if request.method == "POST":
            user_info = request.get_json()
            data = {
                "username": user_info.get('username'),
                "password": user_info.get('password'),
            }
            # create if username not exist in db
            user = dbc.get_one_user(data["username"])
            if not user:
                data["likes"], data["history"] = [], []
                dbc.insert_one_user(data)
                response_object['status'] = 'success'
    except Exception:
        return jsonify("Error")
    return jsonify(response_object)


@app.route('/influco.api/login/<string:username>', methods=['post'])
def login(username):
    response_object = {'status':'fail'}
    try:
        if request.method == "POST":
            user_info = request.get_json()
            data = {
                "username": user_info.get('username'),
                "password": user_info.get('password'),
            }
            if not dbc.get_one_user(data["username"]):
                return jsonify(response_object)
            user_info = dbc.get_one_user(data["username"])
            ############## will be replaced ##############
            if user_info['password'] != data["password"]:
            ##############################################
                return jsonify(response_object)
            response_object['status'] = 'success'
    except Exception:
        return jsonify({'status':'error'})
    return jsonify(response_object)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
