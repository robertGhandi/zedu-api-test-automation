import requests
import os
from dotenv import load_dotenv
from utils.data_factory import generate_user
from utils.negative_factory import generate_invalid_user_email, generate_empty_password_user
from utils.negative_factory import generate_unregistered_email
from schemas.auth_schema import login_response_schema
from schemas.error_schema import error_401_schema
from utils.validators import validate_schema

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


# =========================
# SUCCESS LOGIN TEST
# =========================
def test_login_success():
    user = generate_user()

    # register
    reg = requests.post(f"{BASE_URL}/auth/register", json=user)
    assert reg.status_code == 201

    # login
    login = requests.post(f"{BASE_URL}/auth/login", json={
        "email": user["email"],
        "password": user["password"]
    })

    body = login.json()

    assert login.status_code == 200
    validate_schema(body, login_response_schema)
   


# =========================
# NEGATIVE LOGIN TEST
# =========================
def test_login_invalid_credentials():

    invalid_email = generate_invalid_user_email()

    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": invalid_email,
            "password": "wrongpassword"
        }
    )

    body = response.json()

    assert response.status_code in [400, 401]
    assert body["status"] == "error"
    assert "message" in body
    assert "invalid" in body["message"].lower()

def test_login_invalid_password():
    user = generate_user()

    requests.post(f"{BASE_URL}/auth/register", json=user)

    response = requests.post(f"{BASE_URL}/auth/login", json={
        "email": user["email"],
        "password": "wrongpassword"
    })

    assert response.status_code in [400, 401]

def test_login_missing_email_field():
    user = generate_user()

    response = requests.post(f"{BASE_URL}/auth/login", json={
        "password": user["password"]
    })

    body = response.json()

    assert response.status_code in [400, 422]
    assert body["status"] == "error"


def test_login_missing_password_field():
    user = generate_user()
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "email": user["email"]
    })

    body = response.json()

    assert response.status_code in [400, 422]
    assert body["status"] == "error"