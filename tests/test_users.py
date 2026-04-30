import requests
from utils.validators import validate_schema

from schemas.user_schema import (
    user_status_success_schema,
    user_organisations_success_schema
)
from schemas.error_schema import (
    error_401_schema,
    error_status_403_schema
)


# ==============================
# 🟢 ORGANISATIONS (VALID TOKEN)
# ==============================
def test_get_organisations_valid_token(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/organisations",
        headers=auth_context["headers"],
        timeout=10
    )

    body = response.json()

    assert response.status_code == 200
    assert "data" in body
    assert isinstance(body["data"], list)

    validate_schema(body, user_organisations_success_schema)


# ==============================
# 🔴 ORGANISATIONS (NO TOKEN)
# ==============================
def test_get_organisations_no_token(base_url):
    response = requests.get(
        f"{base_url}/users/organisations",
        timeout=10
    )

    body = response.json()

    assert response.status_code in [401, 403]

    if response.status_code == 401:
        validate_schema(body, error_401_schema)
    else:
        validate_schema(body, error_status_403_schema)


# ==============================
# 🔴 ORGANISATIONS (INVALID TOKEN)
# ==============================
def test_get_organisations_invalid_token(base_url):
    response = requests.get(
        f"{base_url}/users/organisations",
        headers={"Authorization": "Bearer invalid"},
        timeout=10
    )

    body = response.json()

    assert response.status_code in [401, 403]

    if response.status_code == 401:
        validate_schema(body, error_401_schema)
    else:
        validate_schema(body, error_status_403_schema)


# ==============================
# 🟢 USER STATUS (VALID)
# ==============================
def test_get_user_status_valid(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/status",
        headers=auth_context["headers"],
        timeout=10
    )

    body = response.json()

    assert response.status_code == 200
    validate_schema(body, user_status_success_schema)

    


# ==============================
# 🔴 USER STATUS (INVALID TOKEN)
# ==============================
def test_get_user_status_invalid_token(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/status",
        headers={"Authorization": "Bearer invalid"},
        timeout=10
    )

    body = response.json()

    assert response.status_code in [401, 403]

    if response.status_code == 401:
        validate_schema(body, error_401_schema)
    else:
        validate_schema(body, error_status_403_schema)


# ==============================
# 🔴 USER STATUS (MALFORMED TOKEN)
# ==============================
def test_get_user_status_malformed_token(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/status",
        headers={"Authorization": "Bearer malformed.token"},
        timeout=10
    )

    body = response.json()

    assert response.status_code in [401, 403]

    if response.status_code == 401:
        validate_schema(body, error_401_schema)
    else:
        validate_schema(body, error_status_403_schema)