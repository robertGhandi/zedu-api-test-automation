import requests
import os
from utils.data_factory import generate_user
from utils.negative_factory import generate_invalid_user_email
from utils.validators import validate_schema
from schemas.auth_schema import magic_link_success_schema
from schemas.error_schema import error_400_schema, validation_error_schema
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def test_magic_link_valid_email():
    user = generate_user()

    # register first
    requests.post(f"{BASE_URL}/auth/register", json=user)

    response = requests.post(
        f"{BASE_URL}/auth/magick-link",
        json={"email": user["email"]}
    )

    body = response.json()

    assert response.status_code in [200, 201]
    validate_schema(body, magic_link_success_schema)


def test_magic_link_unregistered_email():
    response = requests.post(
        f"{BASE_URL}/auth/magick-link",
        json={"email": "nonexistentuser123@example.com"}
    )

    body = response.json()

    assert response.status_code in [400, 404]
    validate_schema(body, error_400_schema)


def test_magic_link_invalid_email_format():

    user = generate_invalid_user_email()

    response = requests.post(
        f"{BASE_URL}/auth/magick-link",
        json={"email": user}
    )

    body = response.json()

    assert response.status_code in [400, 422]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)

def test_magic_link_missing_email():
    response = requests.post(
        f"{BASE_URL}/auth/magick-link",
        json={}
    )

    body = response.json()

    assert response.status_code in [400, 422]
    assert body["status"] == "error"