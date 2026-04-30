import requests
from utils.data_factory import generate_user
from utils.negative_factory import generate_unregistered_email
from utils.validators import validate_schema

from schemas.auth_schema import magic_link_success_schema
from schemas.error_schema import error_400_schema, validation_error_schema

TIMEOUT = 10


# ==============================
# 🟢 MAGIC LINK (VALID EMAIL)
# ==============================
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

    # stronger validation
    assert body["status"] == "success"
    assert isinstance(body["message"], str)


# ==============================
# 🔴 MAGIC LINK (UNREGISTERED EMAIL)
# ==============================
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
        # fallback for 404
        assert "message" in body
        assert isinstance(body["message"], str)


# ==============================
# 🔴 MAGIC LINK (INVALID EMAIL FORMAT)
# ==============================
def test_magic_link_invalid_email_format(base_url):
    response = requests.post(
        f"{base_url}/auth/magick-link",
        json={"email": "invalid-email"},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


# ==============================
# 🔴 MAGIC LINK (MISSING EMAIL)
# ==============================
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