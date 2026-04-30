import requests
from utils.validators import validate_schema

from schemas.user_schema import (
    user_status_success_schema,
    user_organisations_success_schema
)
from schemas.error_schema import (
    error_401_schema,
    error_status_403_schema
)

TIMEOUT = 10


# Verify organisations are successfully retrieved for an authenticated user

def test_get_organisations_valid_token(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/organisations",
        headers=auth_context["headers"],
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code == 200

    assert "data" in body
    assert isinstance(body["data"], list)

    validate_schema(body, user_organisations_success_schema)

    # explicit check
    if body["data"]:
        org = body["data"][0]
        assert "id" in org


# Attempt to retrieve organisations without authentication token (should return unauthorized/forbidden)

def test_get_organisations_no_token(base_url):
    response = requests.get(
        f"{base_url}/users/organisations",
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [401, 403]

    if response.status_code == 401:
        validate_schema(body, error_401_schema)
    else:
        validate_schema(body, error_status_403_schema)


# Attempt to retrieve organisations with an invalid token (should return unauthorized/forbidden)

def test_get_organisations_invalid_token(base_url):
    response = requests.get(
        f"{base_url}/users/organisations",
        headers={
            "Authorization": "Bearer invalid",
            "Content-Type": "application/json"
        },
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [401, 403]

    if response.status_code == 401:
        validate_schema(body, error_401_schema)
    else:
        validate_schema(body, error_status_403_schema)


# Verify user status is successfully retrieved for an authenticated user

def test_get_user_status_valid(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/status",
        headers=auth_context["headers"],
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code == 200
    validate_schema(body, user_status_success_schema)

    assert body["status"] == "success"
    assert isinstance(body["data"], dict)

    
    assert "text" in body["data"]
    assert isinstance(body["data"]["text"], str)

    assert "visibility" in body["data"]
    assert isinstance(body["data"]["visibility"], str)


# Attempt to retrieve user status with an invalid token (should return unauthorized/forbidden)

def test_get_user_status_invalid_token(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/status",
        headers={
            "Authorization": "Bearer invalid",
            "Content-Type": "application/json"
        },
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [401, 403]

    if response.status_code == 401:
        validate_schema(body, error_401_schema)
    else:
        validate_schema(body, error_status_403_schema)


# Attempt to retrieve user status with a malformed token (should return unauthorized/forbidden)

def test_get_user_status_malformed_token(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/status",
        headers={
            "Authorization": "Bearer malformed.token",
            "Content-Type": "application/json"
        },
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [401, 403]

    if response.status_code == 401:
        validate_schema(body, error_401_schema)
    else:
        validate_schema(body, error_status_403_schema)