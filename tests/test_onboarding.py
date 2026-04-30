import requests
from utils.validators import validate_schema

from schemas.error_schema import error_401_schema, error_status_403_schema
from schemas.onboarding_schema import onboarding_success_schema

TIMEOUT = 10


# Verify onboarding status is successfully retrieved for an authenticated user

def test_get_onboarding_status_success(base_url, auth_context):
    response = requests.get(
        f"{base_url}/auth/onboard-status",
        headers=auth_context["headers"],
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code == 200
    validate_schema(body, onboarding_success_schema)

    assert body["status"] == "success"
    assert isinstance(body["data"], dict)
    assert "status" in body["data"]
    assert isinstance(body["data"]["status"], bool)

# Attempt to retrieve onboarding status without authentication token (should return unauthorized/forbidden)

def test_get_onboarding_status_no_token(base_url):
    response = requests.get(
        f"{base_url}/auth/onboard-status",
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [401, 403]

    if response.status_code == 401:
        validate_schema(body, error_401_schema)
    else:
        validate_schema(body, error_status_403_schema)


# Attempt to retrieve onboarding status with an invalid token (should return unauthorized/forbidden)

def test_get_onboarding_status_invalid_token(base_url):
    response = requests.get(
        f"{base_url}/auth/onboard-status",
        headers={
            "Authorization": "Bearer invalid_token",
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


# Attempt to retrieve onboarding status with a malformed token (should return unauthorized/forbidden)

def test_get_onboarding_status_malformed_token(base_url):
    response = requests.get(
        f"{base_url}/auth/onboard-status",
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