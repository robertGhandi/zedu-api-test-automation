onboarding_success_schema = {
    "type": "object",
    "required": ["status", "message", "status_code", "data"],
    "properties": {
        "status": {"type": "string"},
        "message": {"type": "string"},
        "status_code": {"type": "number"},

        "data": {
            "type": "object",
            "required": ["status"],
            "properties": {
                "status": {"type": "boolean"}
            },
            "additionalProperties": True
        }
    },
    "additionalProperties": True
}

