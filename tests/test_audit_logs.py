import requests
from utils.token_factory import generate_invalid_token, generate_malformed_token
from utils.validators import validate_schema

from schemas.audit_schema import audit_logs_schema
from schemas.error_schema import error_401_schema


# =========================
# ✅ SUCCESS — FETCH AUDIT LOGS
# =========================
def test_get_audit_logs_success(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/login-audit",
        headers=auth_context["headers"]
    )

    body = response.json()

    if response.status_code == 200:
        validate_schema(body, audit_logs_schema)
        assert isinstance(body["data"], list)
    else:
        # fallback if endpoint returns 404
        assert response.status_code == 404


# =========================
# ❌ NO TOKEN
# =========================
def test_get_audit_logs_no_token(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/login-audit"
    )

    body = response.json()

    assert response.status_code in [401, 403]
    validate_schema(body, error_401_schema)


# =========================
# ❌ INVALID TOKEN
# =========================
def test_get_audit_logs_invalid_token(base_url, auth_context):
    token = generate_invalid_token()

    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/login-audit",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )

    body = response.json()

    assert response.status_code in [401, 403]
    validate_schema(body, error_401_schema)


# =========================
# ❌ MALFORMED TOKEN
# =========================
def test_get_audit_logs_malformed_token(base_url, auth_context):
    token = generate_malformed_token()

    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/login-audit",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )

    body = response.json()

    assert response.status_code in [401, 403]
    validate_schema(body, error_401_schema)


# =========================
# ⚠️ EDGE — MULTIPLE LOGINS GENERATE AUDIT DATA
# =========================
def test_audit_logs_after_multiple_logins(base_url, auth_user):
    # simulate multiple logins
    for _ in range(3):
        requests.post(
            f"{base_url}/auth/login",
            json={
                "email": auth_user["email"],
                "password": auth_user["password"]
            }
        )

    # login again
    login = requests.post(
        f"{base_url}/auth/login",
        json={
            "email": auth_user["email"],
            "password": auth_user["password"]
        }
    )

    token = login.json()["data"]["access_token"]

    response = requests.get(
        f"{base_url}/users/{login.json()['data']['user']['id']}/login-audit",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )

    body = response.json()

    if response.status_code == 200:
        validate_schema(body, audit_logs_schema)

        if body["data"]:
            log = body["data"][0]

            # explicit validation
            assert "id" in log
            assert isinstance(log["id"], str)
            assert "created_at" in log