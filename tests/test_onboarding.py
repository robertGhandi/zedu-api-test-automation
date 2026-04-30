import requests
from utils.validators import validate_schema

from schemas.error_schema import error_401_schema
from schemas.onboarding_schema import onboarding_success_schema


# ==============================
# 🟢 ONBOARDING STATUS (SUCCESS)
# ==============================
def test_get_onboarding_status_success(base_url, auth_context):
    response = requests.get(
        f"{base_url}/auth/onboard-status",
        headers=auth_context["headers"]
    )

    body = response.json()

    assert response.status_code == 200
    validate_schema(body, onboarding_success_schema)

    


# ==============================
# 🔴 NO TOKEN
# ==============================
def test_get_onboarding_status_no_token(base_url):
    response = requests.get(f"{base_url}/auth/onboard-status")

    body = response.json()

    assert response.status_code in [401, 403]
    validate_schema(body, error_401_schema)


# ==============================
# 🔴 INVALID TOKEN
# ==============================
def test_get_onboarding_status_invalid_token(base_url):
    response = requests.get(
        f"{base_url}/auth/onboard-status",
        headers={
            "Authorization": "Bearer invalid_token",
            "Content-Type": "application/json"
        }
    )

    body = response.json()

    assert response.status_code in [401, 403]
    validate_schema(body, error_401_schema)


# ==============================
# 🔴 MALFORMED TOKEN
# ==============================
def test_get_onboarding_status_malformed_token(base_url):
    response = requests.get(
        f"{base_url}/auth/onboard-status",
        headers={
            "Authorization": "Bearer malformed.token",
            "Content-Type": "application/json"
        }
    )

    body = response.json()

    assert response.status_code in [401, 403]
    validate_schema(body, error_401_schema)