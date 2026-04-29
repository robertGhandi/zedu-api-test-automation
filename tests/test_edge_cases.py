import requests
import os
from utils.data_factory import generate_user
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def test_register_empty_payload():
    response = requests.post(f"{BASE_URL}/auth/register", json={})

    body = response.json()

    assert response.status_code in [400, 422]
    assert body["status"] == "error"


def test_register_long_username():
    user = generate_user()
    user["username"] = "x" * 300

    response = requests.post(f"{BASE_URL}/auth/register", json=user)

    assert response.status_code in [400, 422]


def test_login_sql_injection():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": "' OR 1=1 --",
            "password": "' OR 1=1 --"
        }
    )

    body = response.json()

    assert response.status_code in [400, 401]
    assert body["status"] == "error"