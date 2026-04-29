import requests
import os

BASE_URL = os.getenv("BASE_URL")


def login_user(email, password):
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": email,
            "password": password
        }
    )

    body = response.json()

    assert response.status_code == 200

    return body["data"]["access_token"]