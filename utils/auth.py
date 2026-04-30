import requests


def login_user(base_url, email, password):
    """
    Logs in a user and returns the full response body.

    Args:
        base_url (str): API base URL
        email (str): User email
        password (str): User password

    Returns:
        dict: JSON response body from login endpoint
    """

    response = requests.post(
        f"{base_url}/auth/login",
        json={
            "email": email,
            "password": password
        },
        timeout=10
    )

    body = response.json()

    assert response.status_code == 200, f"Login failed: {body}"

    return body