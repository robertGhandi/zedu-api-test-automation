import os

import requests
from utils.data_factory import generate_user
from utils.negative_factory import generate_unregistered_email
from utils.validators import validate_schema
from dotenv import load_dotenv

from schemas.auth_schema import magic_link_success_schema
from schemas.error_schema import error_400_schema, validation_error_schema
load_dotenv()

TIMEOUT = 10

# Verify magic link request is successful for a registered email

def test_magic_link_valid_email(base_url):
    user = generate_user()

    # register first
    reg = requests.post(
        f"{base_url}/auth/register",
        json=user,
        timeout=TIMEOUT
    )
    assert reg.status_code == 201

    response = requests.post(
        f"{base_url}/auth/magick-link",
        json={"email": user["email"]},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [200, 201]
    validate_schema(body, magic_link_success_schema)

    assert body["status"] == "success"
    assert isinstance(body["message"], str)

# Attempt magic link request with an unregistered email (should return error response)

def test_magic_link_unregistered_email(base_url):
    response = requests.post(
        f"{base_url}/auth/magick-link",
        json={"email": generate_unregistered_email()},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 404]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        assert "message" in body
        assert isinstance(body["message"], str)


# Attempt magic link request with invalid email format (should trigger validation error)

def test_magic_link_invalid_email_format(base_url):
    response = requests.post(
        f"{base_url}/auth/magick-link",
        json={"email": os.getenv("INVALID_EMAIL")},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


# Attempt magic link request with missing email field (should fail validation)

def test_magic_link_missing_email(base_url):
    response = requests.post(
        f"{base_url}/auth/magick-link",
        json={},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)