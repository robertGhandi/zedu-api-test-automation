import os

import requests
from dotenv import load_dotenv
load_dotenv()

base_url = os.getenv("BASE_URL")

# ==============================
# 🟢 ORGANISATIONS (VALID TOKEN)
# ==============================

def test_get_organisations_valid_token(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/organisations",
        headers=auth_context["headers"]
    )

    body = response.json()

    assert response.status_code == 200
    assert "data" in body
    assert isinstance(body["data"], list)


# ==============================
# 🔴 ORGANISATIONS (NO TOKEN)
# ==============================

def test_get_organisations_no_token(base_url):
    response = requests.get(f"{base_url}/users/organisations")

    body = response.json()

    assert response.status_code in [401, 403]
    assert body["status"] == "error"


# ==============================
# 🔴 ORGANISATIONS (INVALID TOKEN)
# ==============================

def test_get_organisations_invalid_token(base_url):
    headers = {"Authorization": "Bearer invalidtoken"}

    response = requests.get(
        f"{base_url}/users/organisations",
        headers=headers
    )

    body = response.json()

    assert response.status_code in [401, 403]
    assert body["status"] == "error"


# ==============================
# 🟢 USER STATUS
# ==============================

def test_get_user_status_valid(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/status",
        headers=auth_context["headers"]
    )

    body = response.json()

    assert response.status_code == 200
    assert "data" in body


# ==============================
# 🔴 USER STATUS (INVALID TOKEN)
# ==============================

def test_get_user_status_invalid_token(base_url, auth_context):
    headers = {"Authorization": "Bearer invalid"}

    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/status",
        headers=headers
    )

    assert response.status_code in [401, 403]


# ==============================
# 🔴 USER STATUS (EXPIRED TOKEN SIMULATION)
# ==============================

def test_get_user_status_expired_token(base_url, auth_context):
    headers = {"Authorization": "Bearer expired.token.here"}

    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/status",
        headers=headers
    )

    assert response.status_code in [401, 403]