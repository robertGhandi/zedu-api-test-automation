import requests
from utils.data_factory import generate_user
from utils.negative_factory import generate_unregistered_email
from utils.validators import validate_schema

from schemas.email_schema import (
    email_request_success_schema,
    email_request_400_schema,
    email_request_422_schema
)

TIMEOUT = 10


# ==============================
# 🟢 EMAIL VERIFICATION REQUEST (VALID)
# ==============================
def test_email_verification_valid(base_url):
    user = generate_user()

    # Register user first
    reg = requests.post(
        f"{base_url}/auth/register",
        json=user,
        timeout=TIMEOUT
    )
    assert reg.status_code == 201

    response = requests.post(
        f"{base_url}/auth/email-request",
        json={"email": user["email"]},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [200, 201]
    validate_schema(body, email_request_success_schema)

    # stronger validation
    assert body["status"] == "success"
    assert isinstance(body["message"], str)


# ==============================
# 🔴 EMAIL VERIFICATION (UNREGISTERED)
# ==============================
def test_email_verification_unregistered(base_url):
    response = requests.post(
        f"{base_url}/auth/email-request",
        json={"email": generate_unregistered_email()},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 404]

    if response.status_code == 400:
        validate_schema(body, email_request_400_schema)
    else:
        # fallback for 404
        assert "message" in body
        assert isinstance(body["message"], str)


# ==============================
# 🔴 EMAIL VERIFICATION (INVALID FORMAT)
# ==============================
def test_email_verification_invalid_format(base_url):
    response = requests.post(
        f"{base_url}/auth/email-request",
        json={"email": "invalid-email"},
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, email_request_400_schema)
    else:
        validate_schema(body, email_request_422_schema)