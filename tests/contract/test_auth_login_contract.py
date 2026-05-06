import pytest
import requests
import os
from dotenv import load_dotenv
from schemas.error_schema import validation_error_schema
from utils.validators import validate_schema

load_dotenv()

@pytest.mark.contract
def test_login_invalid_email_should_return_422(base_url):
    response = requests.post(
        f"{base_url}/auth/login",
        json={
            "email": os.getenv("INVALID_EMAIL"),
            "password": os.getenv("DEFAULT_PASSWORD")
        }
    )

    body = response.json()

    assert response.status_code == 422, (
        f"Expected 422 per spec, got {response.status_code}. Response: {body}"
    )

    validate_schema(body, validation_error_schema)