user_status_schema = {
    "type": "object",
    "required": ["status", "status_code", "message", "data"],
    "properties": {
        "status": {"type": "string"},
        "status_code": {"type": "number"},
        "message": {"type": "string"},
        "data": {
            "type": "object",
            "required": ["text", "emoji", "expiry", "visibility"],
            "properties": {
                "text": {"type": "string"},
                "emoji": {"type": "string"},
                "expiry": {"type": "number"},
                "visibility": {"type": "string"}
            }
        }
    }
}