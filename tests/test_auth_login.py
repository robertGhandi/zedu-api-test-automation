import requests
from utils.data_factory import generate_user
from utils.negative_factory import generate_unregistered_email
from utils.validators import validate_schema

from schemas.auth_schema import login_response_schema
from schemas.error_schema import (
    error_400_schema,
    error_401_schema,
    validation_error_schema
)


# =========================
# ✅ SUCCESS LOGIN TEST
# =========================
def test_login_success(base_url):
    user = generate_user()

    reg = requests.post(f"{base_url}/auth/register", json=user, timeout=10)
    assert reg.status_code == 201

    response = requests.post(
        f"{base_url}/auth/login",
        json={
            "email": user["email"],
            "password": user["password"]
        }
    )

    body = response.json()

    assert response.status_code == 200
    validate_schema(body, login_response_schema)

    assert isinstance(body["data"]["access_token"], str)


# =========================
# ❌ UNREGISTERED EMAIL
# =========================
def test_login_unregistered_email(base_url):
    response = requests.post(
        f"{base_url}/auth/login",
        json={
            "email": generate_unregistered_email(),
            "password": "Password123!"
        },
        timeout=10
    )

    body = response.json()

    assert response.status_code in [400, 401, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    elif response.status_code == 401:
        validate_schema(body, error_401_schema)
    else:
        validate_schema(body, validation_error_schema)


# =========================
# ❌ WRONG PASSWORD
# =========================
def test_login_wrong_password(base_url):
    user = generate_user()
    requests.post(f"{base_url}/auth/register", json=user)

    response = requests.post(
        f"{base_url}/auth/login",
        json={
            "email": user["email"],
            "password": "WrongPassword123!"
        },
        timeout=10
    )

    body = response.json()

    assert response.status_code in [400, 401]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, error_401_schema)


# =========================
# ❌ MISSING EMAIL
# =========================
def test_login_missing_email(base_url):
    user = generate_user()

    response = requests.post(
        f"{base_url}/auth/login",
        json={
            "password": user["password"]
        },
        timeout=10
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


# =========================
# ❌ MISSING PASSWORD
# =========================
def test_login_missing_password(base_url):
    user = generate_user()

    response = requests.post(
        f"{base_url}/auth/login",
        json={
            "email": user["email"]
        },
        timeout=10
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


# =========================
# ❌ EMPTY PAYLOAD
# =========================
def test_login_empty_payload(base_url):
    response = requests.post(f"{base_url}/auth/login", json={}, timeout=10)

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)