from faker import Faker
import uuid

fake = Faker()


def generate_user():
    return {
        "username": f"user_{uuid.uuid4().hex[:6]}",
        "email": fake.unique.email(),
        "password": "Password123!",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "phone_number": fake.msisdn()[:11]
    }

