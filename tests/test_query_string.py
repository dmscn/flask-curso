import pytest
from flask import url_for


@pytest.fixture()
def resp(client):
    query = {
        'name': 'Leo',
        'surname': 'Damasceno'
    }
    return client.get(url_for('names.name_surname'), query_string=query)


def test_status_code(resp):
    assert resp.status_code == 200


def test_msg(resp):
    assert 'Hello Leo Damasceno' in resp.get_data(as_text=True)
