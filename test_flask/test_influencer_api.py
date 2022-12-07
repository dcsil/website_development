import ast

from influco_web import app


def test_hello_backend():
    response = app.test_client().get("/influco.api")

    # convert into python dict
    data = ast.literal_eval(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert data == "Hello, InfluCo backend!"


def test_get_one_influencer():
    response = app.test_client().get("/influco.api/influencer/afrae.es")

    # convert into python dict
    data = ast.literal_eval(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert data["author_stats"]["id"] == "afrae.es"


def test_get_influencers_by_tag():
    response = app.test_client().get("/influco.api/tag/dance")

    # convert into python dict
    data = ast.literal_eval(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert len(data) == 68


def test_get_one_user():
    response = app.test_client().get("/influco.api/user/test_user")

    # convert into python dict
    data = ast.literal_eval(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert data == {'_id': '6390dc6030d1e13b11528d29',
                    'history': [],
                    'likes': [],
                    'password': 'test',
                    'username': 'test_user'}


def test_get_login():
    response = app.test_client().post("/influco.api/login/test_user",
                                      json={"username": "test_user",
                                            "password": "test"})

    # convert into python dict
    data = ast.literal_eval(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert data["data"] == {'_id': '6390dc6030d1e13b11528d29',
                            'history': [],
                            'likes': [],
                            'password': 'test',
                            'username': 'test_user'}


def test_add_history():
    response = app.test_client().post("/influco.api/history/test_user",
                                      json={"influ_id": "test_influ"})

    # convert into python dict
    data = ast.literal_eval(response.data.decode('utf-8'))['data']
    assert response.status_code == 200
    assert data["history"][-1]["influ_id"] == "test_influ"


def test_clear_history():
    response = app.test_client().delete("/influco.api/history/test_user")

    # convert into python dict
    data = ast.literal_eval(response.data.decode('utf-8'))['data']
    assert response.status_code == 200
    assert data["history"] == []


def test_add_like():
    response = app.test_client().post("/influco.api/likes/test_user",
                                      json={"influ_id": "test_influ"})

    # convert into python dict
    data = ast.literal_eval(response.data.decode('utf-8'))['data']
    assert response.status_code == 200
    assert data["likes"][-1]["influ_id"] == "test_influ"


def test_remove_like():
    response = app.test_client().delete("/influco.api/likes/test_user",
                                        json={"influ_id": "test_influ"})

    # convert into python dict
    data = ast.literal_eval(response.data.decode('utf-8'))['data']
    assert response.status_code == 200
    assert data["likes"] == []


def test_register_duplicate():
    response = app.test_client().put("/influco.api/register/test_user",
                                        json={"username": "test_user",
                                              "password": "test"})

    # convert into python dict
    data = ast.literal_eval(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert data == {'status': 'fail'}
