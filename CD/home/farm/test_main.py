from main import app
import pytest


def test_index_route():
    # Get request and checking status code
    response = app.test_client().get('/')
    assert response.status_code == 200
    # checking response data
    expected_content_response = 'Welcome to the updated Flask App V2!'
    assert expected_content_response.encode('utf-8') in response.data


def test_cow_route():
    # Repeat tests for /cow 
    response = app.test_client().get('/cow')
    assert response.status_code == 200

    expected_content_response = 'MOoooOo!'
    assert expected_content_response.encode('utf-8') in response.data
