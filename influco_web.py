import json
import os
import sentry_sdk
from bson import ObjectId
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import *
# from flask.json import JSONEncoder
from sentry_sdk.integrations.flask import FlaskIntegration
from flask.json.provider import JSONProvider

import db_helper.mongodb_connect as dbc
import db_helper.influ_da as da

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
CORS(app, supports_credentials=True)


# json load of mongodb file
class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)


class MongoJSONProvider(JSONProvider):
    def dumps(self, obj, **kwargs):
        return json.dumps(obj, **kwargs, cls=MongoJSONEncoder)

    def loads(self, s, **kwargs):
        return json.loads(s)


# app.json_encoder = MongoJSONEncoder
app.json = MongoJSONProvider(app)
app.url_map.strict_slashes = False


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


@app.route('/influco.api', defaults={'path': ''})
@app.route("/influco.api/<path>")
def hello_backend(path):
    """Backend landing page"""
    try:
        # number = request.args.get("number")
        res = "Hello, InfluCo backend!"
    except Exception:
        return jsonify("error")
    return jsonify(res)


@app.route('/influco.api/influencer/<string:influencer_id>', methods=['get'])
def get_one_influencer(influencer_id):
    """return one influencer by id"""
    try:
        # number = request.args.get("influencer_id")
        res = dbc.get_one_influencer(influencer_id)
    except Exception:
        return jsonify("error")
    return jsonify(res)


@app.route('/influco.api/tag/<string:tag_str>', methods=['get'])
def get_influencers_by_tag(tag_str):
    """return a influencers list by searching a specific tags"""
    try:
        all_influ = dbc.get_all_influencer()
        match_list = da.get_match_influ(tag_str, all_influ)
        res = match_list
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


@app.route('/influco.api/username/<string:username>', methods=['post'])
def update_username(username):
    response_object = {'status': 'fail'}
    try:
        new_name = request.get_json().get("new_name")
        res = dbc.update_username(username, new_name)
        # no error message
        if not isinstance(res, str):
            response_object['status'] = 'success'
            response_object['data'] = res
    except Exception:
        return jsonify({'status': 'error'})
    return jsonify(response_object)


@app.route('/influco.api/password/<string:username>', methods=['post'])
def update_password(username):
    response_object = {'status': 'fail'}
    try:
        password = request.get_json().get("password")
        res = dbc.update_password(username, password)
        # no error message
        if not isinstance(res, str):
            response_object['status'] = 'success'
            response_object['data'] = res
    except Exception:
        return jsonify({'status': 'error'})
    return jsonify(response_object)


@app.route('/influco.api/register/<string:username>', methods=['put'])
def register(username):
    """get info for one user"""
    response_object = {'status': 'fail'}
    try:
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
    response_object = {'status': 'fail'}
    try:
        user_info = request.get_json()
        data = {
            "username": user_info.get('username'),
            "password": user_info.get('password'),
        }
        user_info = dbc.get_one_user(data["username"])
        if not user_info:
            return jsonify(response_object)
        if user_info['password'] != data["password"]:
            return jsonify(response_object)
        response_object['status'] = 'success'
        # Frontend: get user data
        response_object['data'] = user_info
    except Exception:
        return jsonify({'status': 'error'})
    return jsonify(response_object)


@app.route('/influco.api/history/<string:username>', methods=['post'])
def add_history(username):
    response_object = {'status': 'fail'}
    try:
        influ_id = request.get_json().get("influ_id")
        res = dbc.update_user_history(username, influ_id, 'post')
        # no error message
        if not isinstance(res, str):
            response_object['status'] = 'success'
            response_object['data'] = res
    except Exception:
        return jsonify({'status': 'error'})
    return jsonify(response_object)


@app.route('/influco.api/history/<string:username>', methods=['delete'])
def clear_history(username):
    response_object = {'status': 'fail'}
    try:
        res = dbc.update_user_history(username, None, 'delete')
        # no error message
        if not isinstance(res, str):
            response_object['status'] = 'success'
            response_object['data'] = res
    except Exception:
        return jsonify({'status': 'error'})
    return jsonify(response_object)


@app.route('/influco.api/likes/<string:username>', methods=['post'])
def add_like(username):
    response_object = {'status': 'fail'}
    try:
        influ_id = request.get_json().get("influ_id")
        res = dbc.update_user_likes(username, influ_id, 'post')
        # no error message
        if not isinstance(res, str):
            response_object['status'] = 'success'
            response_object['data'] = res
    except Exception:
        return jsonify({'status': 'error'})
    return jsonify(response_object)


@app.route('/influco.api/likes/<string:username>', methods=['delete'])
def remove_like(username):
    response_object = {'status': 'fail'}
    try:
        influ_id = request.get_json().get("influ_id")
        res = dbc.update_user_likes(username, influ_id, 'delete')
        # no error message
        if not isinstance(res, str):
            response_object['status'] = 'success'
            response_object['data'] = res
    except Exception:
        return jsonify({'status': 'error'})
    return jsonify(response_object)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
