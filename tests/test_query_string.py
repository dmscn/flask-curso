import pytest
from flask import url_for


@pytest.fixture()
def resp(client):
    query = {
        'name': 'Leo',
        'surname': 'Damasceno'
    }
    return client.get(url_for('name_surname'), query_string=query)


def test_status_code(resp):
    assert resp.status_code == 200
