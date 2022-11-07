import json
import sentry_sdk
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from sentry_sdk.integrations.flask import FlaskIntegration
import os

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


# sentry verification
@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0


# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/influco.api', methods=['get'])
def create_order():
    """create new order"""
    try:
        number = request.args.get("number")
        res = "Hello, InfluCo backend!"
    except Exception:
        return jsonify("error")
    return jsonify(res)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
