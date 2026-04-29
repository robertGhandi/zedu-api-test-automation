login_response_schema = {
    "type": "object",
    "required": ["status", "status_code", "message", "data"],
    "properties": {
        "status": {"type": "string"},
        "status_code": {"type": "number"},
        "message": {"type": "string"},

        "data": {
            "type": "object",
            "required": [
                "user",
                "access_token",
                "access_token_expires_in",
                "notification_token"
            ],
            "properties": {
                "user": {
                    "type": "object",
                    "required": [
                        "id",
                        "first_name",
                        "fullname",
                        "last_name",
                        "is_verified",
                        "is_onboarded",
                        "email",
                        "phone",
                        "username",
                        "created_at",
                        "updated_at",
                        "expires_at"
                    ],
                    "properties": {
                        "id": {"type": "string"},
                        "first_name": {"type": "string"},
                        "fullname": {"type": "string"},
                        "last_name": {"type": "string"},

                        "is_verified": {"type": "boolean"},
                        "is_onboarded": {"type": "boolean"},

                        "email": {"type": "string"},
                        "phone": {"type": "string"},
                        "username": {"type": "string"},

                        "created_at": {"type": "string", "format": "date-time"},
                        "updated_at": {"type": "string", "format": "date-time"},
                        "expires_at": {"type": "string", "format": "date-time"}
                    }
                },

                "access_token": {"type": "string"},
                "access_token_expires_in": {
                    "type": "string",
                    "format": "date-time"
                },
                "notification_token": {"type": "string"}
            }
        }
    }
}


register_request_schema = {
    "type": "object",
    "required": [
        "username",
        "email",
        "password",
        "first_name",
        "last_name",
        "phone_number"
    ],
    "properties": {
        "username": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "password": {"type": "string", "minLength": 6},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "phone_number": {"type": "string"}
    },
    "additionalProperties": False
}

# ✅ SUCCESS (201)
register_success_schema = {
    "type": "object",
    "required": ["status", "message", "status_code"],
    "properties": {
        "status": {"type": "string"},
        "message": {"type": "string"},
        "status_code": {"type": "number"}
    },
    "additionalProperties": True
}

magic_link_success_schema = {
    "type": "object",
    "required": ["status", "message", "statusCode"],
    "properties": {
        "status": {"type": "string"},
        "message": {"type": "string"},
        "statusCode": {"type": "number"}
    }
}