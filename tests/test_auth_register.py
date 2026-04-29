import requests
import os
from dotenv import load_dotenv
from utils.data_factory import generate_user
from utils.validators import validate_schema
from schemas.auth_schema import register_success_schema
from schemas.error_schema import error_400_schema, validation_error_schema

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def test_register_success():
    user = generate_user()

    response = requests.post(
        f"{BASE_URL}/auth/register",
        json=user
    )

    body = response.json()

    assert response.status_code == 201
    
    validate_schema(body, register_success_schema)


def test_register_missing_email():
    user = generate_user()
    user.pop("email")

    response = requests.post(
        f"{BASE_URL}/auth/register",
        json=user
    )

    body = response.json()

    assert response.status_code in [400, 422]
    
    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)


def test_register_invalid_email():
    user = generate_user()
    user["email"] = "invalid-email"

    response = requests.post(
        f"{BASE_URL}/auth/register",
        json=user
    )

    body = response.json()

    assert response.status_code in [400, 422]
    
    if response.status_code == 400:
        validate_schema(body, error_400_schema)
    else:
        validate_schema(body, validation_error_schema)

def test_register_duplicate_email():
    user = generate_user()

    requests.post(f"{BASE_URL}/auth/register", json=user)
    response = requests.post(f"{BASE_URL}/auth/register", json=user)

    body = response.json()  
    assert response.status_code in [400, 409]

    if response.status_code == 400:
        validate_schema(body, error_400_schema)

