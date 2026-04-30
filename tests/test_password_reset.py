import requests
from utils.data_factory import generate_user
from utils.negative_factory import generate_invalid_user_email, generate_unregistered_email
from utils.validators import validate_schema

from schemas.password_schema import (
    password_reset_success_schema,
    password_reset_400_schema,
    password_reset_422_schema
)

# ==============================
# 🟢 PASSWORD RESET (VALID EMAIL)
# ==============================
def test_password_reset_valid_email(base_url):
    user = generate_user()

    # register first
    requests.post(f"{base_url}/auth/register", json=user)

    response = requests.post(
        f"{base_url}/auth/password-reset",
        json={"email": user["email"]}
    )

    body = response.json()

    assert response.status_code in [200, 201]
    validate_schema(body, password_reset_success_schema)

    # explicit check
    assert isinstance(body["message"], str)


# ==============================
# 🔴 PASSWORD RESET (UNREGISTERED EMAIL)
# ==============================
def test_password_reset_unregistered_email(base_url):
    response = requests.post(
        f"{base_url}/auth/password-reset",
        json={"email": generate_unregistered_email()}
    )

    body = response.json()

    assert response.status_code in [400, 404]

    validate_schema(body, password_reset_400_schema)

# ==============================
# 🔴 PASSWORD RESET (INVALID EMAIL)
# ==============================
def test_password_reset_invalid_email(base_url):
    response = requests.post(
        f"{base_url}/auth/password-reset",
        json={"email": generate_invalid_user_email()}
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, password_reset_400_schema)
    else:
        validate_schema(body, password_reset_422_schema)