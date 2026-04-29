import uuid

def generate_invalid_token():
    return str(uuid.uuid4())

def generate_malformed_token():
    return "invalid.token.structure"

def generate_empty_token():
    return ""