import os
import requests
from utils.data_factory import generate_user
from utils.negative_factory import generate_invalid_user_email
from dotenv import load_dotenv
load_dotenv()
# ==============================
# 🟢 PASSWORD RESET (VALID EMAIL)
# ==============================
base_url = os.getenv("BASE_URL")    

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
    assert "message" in body


# ==============================
# 🔴 PASSWORD RESET (UNREGISTERED EMAIL)
# ==============================

def test_password_reset_unregistered_email(base_url):

    user = generate_invalid_user_email()

    response = requests.post(
        f"{base_url}/auth/password-reset",
        json={"email": user}
    )

    body = response.json()

    assert response.status_code in [400, 404]
    assert body["status"] == "error"


# ==============================
# 🔴 PASSWORD RESET (INVALID EMAIL)
# ==============================

def test_password_reset_invalid_email(base_url):

    user = generate_invalid_user_email()

    response = requests.post(
        f"{base_url}/auth/password-reset",
        json={"email": user}
    )

    assert response.status_code in [400, 422]