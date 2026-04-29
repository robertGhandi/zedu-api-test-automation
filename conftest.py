import pytest
import requests
import os
from dotenv import load_dotenv
from utils.data_factory import generate_user

load_dotenv()


# =========================
# BASE URL FIXTURE
# =========================
@pytest.fixture
def base_url():
    url = os.getenv("BASE_URL")
    assert url is not None, "BASE_URL not set in .env"
    return url


# =========================
# USER FIXTURE (REGISTER ONLY)
# =========================
@pytest.fixture
def auth_user(base_url):
    """
    Creates a fresh user and returns credentials
    """
    user = generate_user()

    response = requests.post(
        f"{base_url}/auth/register",
        json=user
    )

    assert response.status_code == 201, f"Register failed: {response.text}"

    return user


# =========================
# AUTH CONTEXT (MAIN FIXTURE 🚀)
# =========================
@pytest.fixture
def auth_context(base_url, auth_user):
    """
    Logs in user and returns everything needed:
    - access_token
    - user_id
    - headers
    """

    response = requests.post(
        f"{base_url}/auth/login",
        json={
            "email": auth_user["email"],
            "password": auth_user["password"]
        }
    )

    body = response.json()

    assert response.status_code == 200, f"Login failed: {body}"

    access_token = body["data"]["access_token"]
    user_id = body["data"]["user"]["id"]

    return {
        "access_token": access_token,
        "userId": user_id,
        "headers": {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        "base_url": base_url
    }