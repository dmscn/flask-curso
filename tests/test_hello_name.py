import pytest
from flask import url_for


@pytest.fixture
def resp(client):
    response = client.get(url_for('hello_name', name="Leo"))
    return response


def test_root_status_code(resp):
    """Testing status code from root"""
    assert resp.status_code == 200


def test_root_message(resp):
    assert "Hello Leo" in resp.get_data(as_text=True)
