audit_logs_contract_schema = {
    "type": "object",
    "required": ["status", "status_code", "message", "data"],
    "properties": {
        "status": {"type": "string"},
        "status_code": {"type": "number"},
        "message": {"type": "string"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "id",
                    "userId",
                    "access_token_id",
                    "login_at",
                    "ip_address",
                    "device",
                    "created_at"
                ],
                "properties": {
                    "id": {"type": "string"},
                    "userId": {"type": "string"},
                    "access_token_id": {"type": "string"},
                    "login_at": {"type": "string"},
                    "ip_address": {"type": "string"},
                    "location": {"type": "string"},
                    "device": {"type": "string"},
                    "created_at": {"type": "string"},
                    "is_live": {"type": "boolean"}
                },
                "additionalProperties": True
            }
        }
    }
}