import requests
from utils.data_factory import generate_user
from utils.validators import validate_schema

from schemas.error_schema import error_400_schema, validation_error_schema

TIMEOUT = 10



# ==============================
# Attempt user registration with empty request payload (edge case — should fail validation)
# ==============================

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



# ==============================
# Attempt user registration with excessively long username (edge case — should trigger validation constraints)
# ==============================

def test_register_long_username(base_url):
    user = generate_user()
    user["username"] = "x" * 300

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



# ==============================
# Attempt login using SQL injection payload (security edge case — should be rejected by authentication system)
# ==============================

def test_login_sql_injection(base_url):
    response = requests.post(
        f"{base_url}/auth/login",
        json={
            "email": "' OR 1=1 --",
            "password": "' OR 1=1 --"
        },
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 401]

    assert "message" in body
    assert isinstance(body["message"], str)



# ==============================
# Attempt user registration with excessively long email address (edge case — should fail validation)
# ==============================

def test_register_very_long_email(base_url):
    user = generate_user()
    user["email"] = "a" * 300 + "@mail.com"

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



# ==============================
# Attempt user registration with special characters in password (edge case — validate system handling of unusual input)
# ==============================

def test_register_special_characters_password(base_url):
    user = generate_user()
    user["password"] = "@@@###$$$%%%^^^"

    response = requests.post(
        f"{base_url}/auth/register",
        json=user,
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [201, 400, 422]

    if response.status_code == 201:
        # Successful case
        assert "status" in body
        assert isinstance(body["status"], str)
    elif response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)