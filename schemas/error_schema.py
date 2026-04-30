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

error_status_403_schema = {
    "type": "object",
    "required": ["status", "status_code", "message"],
    "properties": {
        "status": {"type": "string"},
        "status_code": {"type": "number"},
        "message": {"type": "string"}
    },
    "additionalProperties": True
}



