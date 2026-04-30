# 🧪 Zedu API Automation Framework (Pytest)

A structured, scalable, and production-style API automation testing framework built using **Python (Pytest)** for testing the Zedu platform APIs.

This project demonstrates **authentication handling, schema validation, dynamic test data generation, and full positive/negative/edge case coverage**.

---

# 📌 Project Overview

This framework automates REST API testing for the Zedu platform:

* 🌐 Application: https://zedu.chat/
* 📘 Swagger Docs: https://api.zedu.chat/swagger/#/

It validates:

* Authentication flows
* User endpoints
* Audit logs
* Error handling
* Edge case scenarios

---

# ⚙️ Tech Stack

* Python 3.10+
* Pytest
* Requests
* python-dotenv
* Faker
* jsonschema

---

# 📁 Project Structure

project/
├── tests/
│   ├── test_auth_login.py
│   ├── test_auth_register.py
│   ├── test_users.py
│   ├── test_audit_logs.py
│   ├── test_magic_link.py
│   ├── test_password_reset.py
│   ├── test_email_verification.py
│   ├── test_onboarding.py
│   ├── test_edge_cases.py
│
├── utils/
│   ├── auth.py
│   ├── data_factory.py
│   ├── negative_factory.py
│   ├── token_factory.py
│   ├── validators.py
│
├── schemas/
│   ├── auth_schema.py
│   ├── user_schema.py
│   ├── audit_schema.py
│   ├── password_schema.py
│   ├── email_schema.py
│   ├── error_schema.py
│   ├── onboarding_schema.py
│
├── conftest.py
├── requirements.txt
├── .env
├── .env.example
└── README.md

---

# 🚀 Features

* 🔐 Dynamic authentication (no hardcoded tokens)
* 🔁 Reusable fixtures for login and headers
* 📊 JSON schema validation for all responses
* ⚠️ Extensive negative testing
* 🧪 Edge case coverage
* 🔄 Fully independent and idempotent tests
* 🎯 Dynamic test data generation (Faker + UUID)
* 🧼 Clean and modular architecture

---

# 🧪 Test Coverage

### ✅ Total Tests

* ✔ 25+ automated test cases
* ✔ 10+ negative tests
* ✔ 5+ edge cases

---

## 🔐 Authentication

* Successful login
* Invalid credentials
* Unregistered email
* Missing fields
* Empty payload

---

## 👤 Users

* Get organisations
* Get user status
* Invalid/malformed token handling

---

## 📜 Audit Logs

* Authorized access
* Unauthorized access
* Multiple login activity validation

---

## 🔗 Magic Link

* Valid email request
* Invalid email format
* Missing email
* Unregistered email

---

## 🔑 Password Reset

* Valid email reset
* Invalid email format
* Unregistered email

---

## 📧 Email Verification

* Valid email request
* Invalid format
* Unregistered email

---

## ⚡ Edge Cases

* Empty payload submission
* Long username input
* SQL injection attempt
* Invalid data formats

---

# 🛠️ Setup Instructions

## 1. Clone Repository

git clone https://github.com/robertGhandi/zedu-api-test-automation.git
cd zedu-api-test-automation

---

## 2. Create Virtual Environment

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

---

## 3. Install Dependencies

pip install -r requirements.txt

(All dependencies are pinned for reproducibility)

---

## 4. Environment Setup

Create a `.env` file in the root directory:

BASE_URL=https://api.zedu.chat/api/v1

---

## 5. Run Tests

Run full test suite:

pytest -s -v

Run a specific test file:

pytest tests/test_users.py -s -v

---

# 🔐 Authentication Flow

1. User is dynamically generated
2. User is registered via `/auth/register`
3. User logs in via `/auth/login`
4. Access token is extracted automatically
5. Token is reused across tests via fixtures

---

# 📦 Utilities

### data_factory.py

Generates valid user data dynamically using Faker.

### negative_factory.py

Generates invalid test inputs:

* Invalid emails
* Missing fields
* Unregistered users

### token_factory.py

Generates invalid and malformed tokens for negative testing.

### validators.py

Handles JSON schema validation using `jsonschema`.

---

# 🧪 Schema Validation

All API responses are validated using JSON schemas:

* Success responses
* Error responses (400, 401, 422)
* Nested and complex response structures

This ensures:

* Field presence
* Data types
* Response consistency

---

# ⚠️ Important Notes

* Ensure `BASE_URL` is correctly set in `.env`
* Run tests from the project root directory
* API must be accessible for tests to pass

---

# 🧼 Code Quality

* Modular and maintainable structure
* Reusable utilities and fixtures
* Clear naming conventions
* Separation of concerns
* Scalable design

---

# 📌 How to Extend

* Add new tests in `/tests`
* Add new schemas in `/schemas`
* Add new data generators in `/utils`
* Expand negative and edge case coverage

---

# 🏁 Summary

This framework is designed to be:

* Easy to clone
* Easy to run
* Easy to extend
* Fully reproducible
* Production-style structured

---

# 👨‍💻 Author

Robert Ghandi
HNG API Automation Stage 3 Submission
