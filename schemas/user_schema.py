user_status_success_schema = {
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
                "text": {"type": ["string", "null"]},
                "emoji": {"type": ["string", "null"]},
                "expiry": {"type": ["number", "null"]},
                "visibility": {"type": ["string", "null"]}
            },
            "additionalProperties": True
        }
    },
    "additionalProperties": True
}

user_organisations_success_schema = {
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
                "required": ["id", "name", "owner_id"],
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "description": {"type": ["string", "null"]},
                    "email": {"type": ["string", "null"]},
                    "country": {"type": ["string", "null"]},
                    "location": {"type": ["string", "null"]},
                    "owner_id": {"type": "string"},
                    "logo_url": {"type": ["string", "null"]},
                    "channels_count": {"type": ["number", "null"]},
                    "total_messages_count": {"type": ["number", "null"]},
                    "created_at": {"type": "string"},
                    "updated_at": {"type": "string"}
                },
                "additionalProperties": True
            }
        }
    },
    "additionalProperties": True
}