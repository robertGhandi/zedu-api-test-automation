import requests
from utils.data_factory import generate_user
from utils.validators import validate_schema

from schemas.auth_schema import register_success_schema
from schemas.error_schema import error_400_schema, validation_error_schema

TIMEOUT = 10


# Verify successful user registration with valid input data

def test_register_success(base_url):
    user = generate_user()

    response = requests.post(
        f"{base_url}/auth/register",
        json=user,
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code == 201
    validate_schema(body, register_success_schema)

    
    assert body["status"] == "success"
    assert body["status_code"] == 201
    assert isinstance(body["message"], str)


# Attempt user registration with missing email field (should trigger validation error)

def test_register_missing_email(base_url):
    user = generate_user()
    user.pop("email")

    response = requests.post(
        f"{base_url}/auth/register",
        json=user,
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


# Attempt user registration with invalid email format (should fail validation)

def test_register_invalid_email(base_url):
    user = generate_user()
    user["email"] = "invalid-email"

    response = requests.post(
        f"{base_url}/auth/register",
        json=user,
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


# Attempt user registration with an already registered email (should return conflict or error)

def test_register_duplicate_email(base_url):
    user = generate_user()

    # First registration
    first = requests.post(
        f"{base_url}/auth/register",
        json=user,
        timeout=TIMEOUT
    )
    assert first.status_code == 201

    # Duplicate attempt
    response = requests.post(
        f"{base_url}/auth/register",
        json=user,
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 409]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        
        assert "message" in body
        assert isinstance(body["message"], str)


# Attempt user registration with empty request payload (edge case — should fail validation)

def test_register_empty_payload(base_url):
    response = requests.post(
        f"{base_url}/auth/register",
        json={},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)