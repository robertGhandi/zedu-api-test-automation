import pytest
import requests
import os

from utils.data_factory import generate_user
from utils.validators import validate_schema

from schemas.error_schema import validation_error_schema

TIMEOUT = 10


# CONTRACT TEST — INVALID EMAIL FORMAT SHOULD RETURN 422

@pytest.mark.contract
def test_register_invalid_email_contract(base_url):
    user = generate_user()
    user["email"] = os.getenv("INVALID_EMAIL")

    response = requests.post(
        f"{base_url}/auth/register",
        json=user,
        timeout=TIMEOUT
    )

    body = response.json()

    assert response.status_code == 422, (
        f"Expected 422 per API specification, "
        f"but got {response.status_code}. Response: {body}"
    )

    validate_schema(body, validation_error_schema)