import ast

import pytest
from influco_web import app


def test_get_order():
    response = app.test_client().get("/influco.api")

    # convert into python dict
    data = ast.literal_eval(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert data == "Hello, InfluCo backend!"
