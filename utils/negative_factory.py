
from faker import Faker

from utils.data_factory import generate_user
fake = Faker()

def generate_invalid_user_email():
    return "invalid-email-format"


def generate_missing_email_user():
    user = generate_user()
    user.pop("email")
    return user


def generate_empty_password_user():
    user = generate_user()
    user["password"] = ""
    return user

def generate_unregistered_email():
    return fake.email()