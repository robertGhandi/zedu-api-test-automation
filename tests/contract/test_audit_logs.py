import pytest
import requests

from utils.validators import validate_schema
from schemas.contract.audit_logs_contract_schema import (
    audit_logs_contract_schema
)


@pytest.mark.contract
def test_get_audit_logs_contract(base_url, auth_context):
    response = requests.get(
        f"{base_url}/users/{auth_context['user_id']}/login-audit",
        headers=auth_context["headers"],
        timeout=10
    )

    body = response.json()

    assert response.status_code == 200

    # STRICT CONTRACT VALIDATION
    validate_schema(body, audit_logs_contract_schema)