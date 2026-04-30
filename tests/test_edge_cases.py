import requests
from utils.data_factory import generate_user
from utils.validators import validate_schema

from schemas.error_schema import error_400_schema, validation_error_schema


# =========================
# ⚠️ EDGE — EMPTY PAYLOAD (REGISTER)
# =========================
def test_register_empty_payload(base_url):
    response = requests.post(f"{base_url}/auth/register", json={})

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


# =========================
# ⚠️ EDGE — VERY LONG USERNAME
# =========================
def test_register_long_username(base_url):
    user = generate_user()
    user["username"] = "x" * 300

    response = requests.post(f"{base_url}/auth/register", json=user)

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


# =========================
# ⚠️ EDGE — SQL INJECTION LOGIN
# =========================
def test_login_sql_injection(base_url):
    response = requests.post(
        f"{base_url}/auth/login",
        json={
            "email": "' OR 1=1 --",
            "password": "' OR 1=1 --"
        }
    )

    body = response.json()

    assert response.status_code in [400, 401]

    # Login error schema
    assert "message" in body


# =========================
# ⚠️ EDGE — VERY LONG EMAIL
# =========================
def test_register_very_long_email(base_url):
    user = generate_user()
    user["email"] = "a" * 300 + "@mail.com"

    response = requests.post(f"{base_url}/auth/register", json=user)

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


# =========================
# ⚠️ EDGE — SPECIAL CHARACTERS IN PASSWORD
# =========================
def test_register_special_characters_password(base_url):
    user = generate_user()
    user["password"] = "@@@###$$$%%%^^^"

    response = requests.post(f"{base_url}/auth/register", json=user)

    body = response.json()

    assert response.status_code in [400, 422, 201]

    # Some APIs allow it — handle safely
    if response.status_code == 201:
        assert "status" in body
    elif response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)