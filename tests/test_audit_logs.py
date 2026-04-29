import requests
import os
from dotenv import load_dotenv
from utils.token_factory import generate_invalid_token, generate_malformed_token
from utils.validators import validate_schema
from schemas.audit_schema import audit_logs_schema

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


def test_get_audit_logs_success(auth_context):
    response = requests.get(
        f"{BASE_URL}/users/{auth_context['user_id']}/login-audit",
        headers=auth_context["headers"]
    )

    body = response.json()

    assert response.status_code in [200, 404]
    validate_schema(body, audit_logs_schema)


def test_get_audit_logs_no_token(auth_context):
    response = requests.get(f"{BASE_URL}/users/{auth_context['user_id']}/login-audit")

    body = response.json()

    assert response.status_code in [401, 403]
    assert body["status"] == "error"


def test_get_audit_logs_invalid_token(auth_context):

    token = generate_invalid_token()

    response = requests.get(
        f"{BASE_URL}/users/{auth_context['user_id']}/login-audit",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )

    body = response.json()

    assert response.status_code in [401, 403]
    assert body["status"] == "error"


def test_get_audit_logs_malformed_token(auth_context):

    token = generate_malformed_token()

    response = requests.get(
        f"{BASE_URL}/users/{auth_context['user_id']}/login-audit",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )

    body = response.json()

    assert response.status_code in [401, 403]
    assert body["status"] == "error"


def test_audit_logs_empty_or_list(auth_context):
    response = requests.get(
        f"{BASE_URL}/users/{auth_context['user_id']}/login-audit",
        headers=auth_context["headers"]
    )

    body = response.json()

    assert response.status_code == 200
    assert isinstance(body["data"], list)


def test_audit_logs_after_multiple_logins(auth_user, auth_context):
    # simulate activity
    for _ in range(3):
        requests.post(
            f"{BASE_URL}/auth/login",
            json={
                "email": auth_user["email"],
                "password": auth_user["password"]
            }
        )

    # login again to get token
    login = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": auth_user["email"],
            "password": auth_user["password"]
        }
    )

    token = login.json()["data"]["access_token"]

    response = requests.get(
        f"{BASE_URL}/users/{auth_context['user_id']}/login-audit",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )

    body = response.json()

    assert response.status_code == 200
    assert isinstance(body["data"], list)

    if body["data"]:
        log = body["data"][0]

        assert "id" in log
        assert "created_at" in log
        assert isinstance(log["id"], (str, int))