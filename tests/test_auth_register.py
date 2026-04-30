import requests
from utils.data_factory import generate_user
from utils.validators import validate_schema

from schemas.auth_schema import register_success_schema
from schemas.error_schema import error_400_schema, validation_error_schema


# =========================
# ✅ REGISTER SUCCESS
# =========================
def test_register_success(base_url):
    user = generate_user()

    response = requests.post(
        f"{base_url}/auth/register",
        json=user
    )

    body = response.json()

    assert response.status_code == 201
    validate_schema(body, register_success_schema)

    # Explicit field validation (meets criteria)
    assert body["status"] == "success"
    assert isinstance(body["message"], str)


# =========================
# ❌ MISSING EMAIL
# =========================
def test_register_missing_email(base_url):
    user = generate_user()
    user.pop("email")

    response = requests.post(
        f"{base_url}/auth/register",
        json=user
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


# =========================
# ❌ INVALID EMAIL FORMAT
# =========================
def test_register_invalid_email(base_url):
    user = generate_user()
    user["email"] = "invalid-email"

    response = requests.post(
        f"{base_url}/auth/register",
        json=user
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


# =========================
# ❌ DUPLICATE EMAIL
# =========================
def test_register_duplicate_email(base_url):
    user = generate_user()

    requests.post(f"{base_url}/auth/register", json=user)

    response = requests.post(
        f"{base_url}/auth/register",
        json=user
    )

    body = response.json()

    assert response.status_code in [400, 409]

    # Handle both cases safely
    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    elif response.status_code == 409:
        assert "message" in body


# =========================
# ⚠️ EDGE CASE — EMPTY PAYLOAD
# =========================
def test_register_empty_payload(base_url):
    response = requests.post(
        f"{base_url}/auth/register",
        json={}
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)