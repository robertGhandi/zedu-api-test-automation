import os

import requests
from utils.data_factory import generate_user
from utils.negative_factory import generate_unregistered_email
from dotenv import load_dotenv

load_dotenv()
# ==============================
# 🟢 EMAIL VERIFICATION REQUEST
# ==============================
base_url = os.getenv("BASE_URL")

def test_email_verification_valid(base_url):
    user = generate_user()

    requests.post(f"{base_url}/auth/register", json=user)

    response = requests.post(
        f"{base_url}/auth/email/verify",
        json={"email": user["email"]}
    )

    body = response.json()

    assert response.status_code in [200, 201]
    assert "message" in body


# ==============================
# 🔴 EMAIL VERIFICATION (UNREGISTERED)
# ==============================

def test_email_verification_unregistered(base_url):
    response = requests.post(
        f"{base_url}/auth/email/verify",
        json={"email": generate_unregistered_email()}
    )

    assert response.status_code in [400, 404]


# ==============================
# 🔴 EMAIL VERIFICATION (INVALID FORMAT)
# ==============================

def test_email_verification_invalid_format(base_url):
    response = requests.post(
        f"{base_url}/auth/email/verify",
        json={"email": "invalid-email"}
    )

    assert response.status_code in [400, 422]