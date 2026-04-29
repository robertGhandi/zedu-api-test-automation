import requests
import os

from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def test_get_onboarding_status_success(auth_context):
    response = requests.get(
        f"{BASE_URL}/auth/onboard-status",
        headers=auth_context["headers"]
    )

    body = response.json()

    assert response.status_code == 200
    assert "data" in body
    assert isinstance(body["data"], dict)


def test_get_onboarding_status_no_token():
    response = requests.get(f"{BASE_URL}/auth/onboard-status")

    body = response.json()

    assert response.status_code in [401, 403]
    assert body["status"] == "error"


def test_get_onboarding_status_invalid_token():
    response = requests.get(
        f"{BASE_URL}/auth/onboard-status",
        headers={
            "Authorization": "Bearer invalid_token",
            "Content-Type": "application/json"
        }
    )

    body = response.json()

    assert response.status_code in [401, 403]
    assert body["status"] == "error"


def test_get_onboarding_status_malformed_token():
    response = requests.get(
        f"{BASE_URL}/auth/onboard-status",
        headers={
            "Authorization": "Bearer malformed.token",
            "Content-Type": "application/json"
        }
    )

    body = response.json()

    assert response.status_code in [401, 403]
    assert body["status"] == "error"