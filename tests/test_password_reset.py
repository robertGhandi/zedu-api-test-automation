import os

from dotenv import load_dotenv
import requests
from utils.data_factory import generate_user
from utils.negative_factory import generate_unregistered_email
from utils.validators import validate_schema

from schemas.password_schema import (
    password_reset_success_schema,
    password_reset_400_schema,
    password_reset_422_schema
)
load_dotenv()

TIMEOUT = 10

# Verify password reset request is successful for a registered email

def test_password_reset_valid_email(base_url):
    user = generate_user()

    # register first
    reg = requests.post(
        f"{base_url}/auth/register",
        json=user,
        timeout=TIMEOUT
    )
    assert reg.status_code == 201

    response = requests.post(
        f"{base_url}/auth/password-reset",
        json={"email": user["email"]},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [200, 201]
    validate_schema(body, password_reset_success_schema)

    assert body["status"] == "success"
    assert isinstance(body["message"], str)


# Attempt password reset request with an unregistered email (should return error response)

def test_password_reset_unregistered_email(base_url):
    response = requests.post(
        f"{base_url}/auth/password-reset",
        json={"email": generate_unregistered_email()},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 404]

    if response.status_code == 400:
        validate_schema(body, password_reset_400_schema)
    else:
        assert "message" in body
        assert isinstance(body["message"], str)


# Attempt password reset request with invalid email format (should trigger validation error)

def test_password_reset_invalid_email(base_url):
    response = requests.post(
        f"{base_url}/auth/password-reset",
        json={"email": os.getenv("INVALID_EMAIL")},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, password_reset_400_schema)
    else:
        validate_schema(body, password_reset_422_schema)