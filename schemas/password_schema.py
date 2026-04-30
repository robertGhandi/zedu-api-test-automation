password_reset_success_schema = {
    "type": "object",
    "required": ["status", "message", "status_code"],
    "properties": {
        "status": {"type": "string"},
        "message": {"type": "string"},
        "status_code": {"type": "number"},
        "data": {"type": ["string", "object", "null"]}
    },
    "additionalProperties": True
}

password_reset_400_schema = {
    "type": "object",
    "required": ["status", "status_code", "message"],
    "properties": {
        "status": {"type": "string"},
        "status_code": {"type": "number"},
        "message": {"type": "string"}
    },
    "additionalProperties": True
}

password_reset_422_schema = {
    "type": "object",
    "required": ["status", "status_code", "message", "error"],
    "properties": {
        "status": {"type": "string"},
        "status_code": {"type": "number"},
        "message": {"type": "string"},
        "error": {
            "type": "object",
            "additionalProperties": {"type": "string"}
        }
    },
    "additionalProperties": True
}