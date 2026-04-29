error_400_schema = {
    "type": "object",
    "required": ["status", "status_code", "message"],
    "properties": {
        "status": {"type": "string"},
        "status_code": {"type": "number"},
        "message": {"type": "string"}
    }
}

error_401_schema = {
    "type": "object",
    "required": ["status", "status_code", "message"],
    "properties": {
        "status": {"type": "string"},
        "status_code": {"type": "number"},
        "message": {"type": "string"}
    }
}

validation_error_schema = {
    "type": "object",
    "required": ["errors", "status_code", "status", "message"],
    "properties": {
        "errors": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["field"],
                "properties": {
                    "field": {"type": "string"}
                }
            }
        },
        "status_code": {"type": "number"},
        "status": {"type": "string"},
        "message": {"type": "string"}
    }
}