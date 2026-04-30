import pytest
import requests
import os
from dotenv import load_dotenv

from utils.data_factory import generate_user
from utils.validators import validate_schema
from schemas.auth_schema import login_response_schema
from utils.auth import login_user

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
    user = generate_user()

    response = requests.post(
        f"{base_url}/auth/register",
        json=user,
        timeout=10
    )

    assert response.status_code == 201, f"Register failed: {response.text}"

    return user


# =========================
# AUTH CONTEXT (MAIN FIXTURE 🚀)
# =========================
@pytest.fixture
def auth_context(base_url, auth_user):
    """
    Provides authenticated user context:
    - access_token
    - user_id
    - headers
    """

    # 🔥 Use reusable login utility
    body = login_user(
        base_url,
        auth_user["email"],
        auth_user["password"]
    )

    # Schema validation
    validate_schema(body, login_response_schema)

    # Safe extraction
    assert "data" in body and "user" in body["data"]

    access_token = body["data"]["access_token"]
    user_id = body["data"]["user"]["id"]

    return {
        "access_token": access_token,
        "user_id": user_id,
        "headers": {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
    }