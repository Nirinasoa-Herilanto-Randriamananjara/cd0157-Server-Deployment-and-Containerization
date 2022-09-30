'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'myjwtsecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjU3NzU1NTcsIm5iZiI6MTY2NDU2NTk1NywiZW1haWwiOiJuaHJAbWFpbC5jb20ifQ.5N1w0RSwGdKM-pRkz1fC0YcHWIeThhr8F4u-Jawu7gY"'
EMAIL = 'nhr@mail.com'
PASSWORD = 'azerty'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy ...'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
