# Zedu API Automation Framework (Pytest)

![CI](https://github.com/robertGhandi/zedu-api-test-automation/actions/workflows/ci.yml/badge.svg)

A structured, scalable, and production-style API automation testing framework built using **Python (Pytest)** for testing the Zedu platform APIs.

This project demonstrates authentication handling, schema validation, dynamic test data generation, and full positive, negative, and edge case coverage.

---

## Project Overview

This framework automates REST API testing for the Zedu platform:

- Application: https://zedu.chat/  
- Swagger Docs: https://api.zedu.chat/swagger/#/  

It validates:

- Authentication flows  
- User endpoints  
- Audit logs  
- Error handling  
- Edge case scenarios  

---

## Tech Stack

- Python 3.10+  
- Pytest  
- Requests  
- python-dotenv  
- Faker  
- jsonschema  

---

## Project Structure

```
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
├── .env.example
└── README.md
```

---

## Features

- Dynamic authentication (no hardcoded tokens)  
- Reusable fixtures for login and headers  
- JSON schema validation for API responses  
- Extensive negative testing  
- Edge case coverage  
- Fully independent and idempotent tests  
- Dynamic test data generation (Faker + UUID)  
- Clean and modular architecture  

---

## Test Coverage

- 25+ automated test cases  
- 10+ negative test scenarios  
- 5+ edge case validations  

### Authentication
- Successful login  
- Invalid credentials  
- Unregistered email  
- Missing fields  
- Empty payload  

### Users
- Retrieve organisations  
- Retrieve user status  
- Invalid and malformed token handling  

### Audit Logs
- Authorized access  
- Unauthorized access  
- Multiple login activity validation  

### Magic Link
- Valid email request  
- Invalid email format  
- Missing email  
- Unregistered email  

### Password Reset
- Valid email reset  
- Invalid email format  
- Unregistered email  

### Email Verification
- Valid email request  
- Invalid format  
- Unregistered email  

### Edge Cases
- Empty payload submission  
- Long username input  
- SQL injection attempt  
- Invalid data formats  

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/robertGhandi/zedu-api-test-automation.git
cd zedu-api-test-automation
```

---

### 2. Create Virtual Environment

#### Windows (CMD / PowerShell)

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Git Bash

```bash
python -m venv venv
source venv/Scripts/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
BASE_URL=https://api.zedu.chat/api/v1
INVALID_EMAIL=invalid-email
DEFAULT_PASSWORD=Password123!
WRONG_PASSWORD=WrongPassword123!
```

---

## Environment Variables

The following environment variables are required:

- BASE_URL → API base URL  
- INVALID_EMAIL → used for negative test scenarios  
- DEFAULT_PASSWORD → used for valid login tests  
- WRONG_PASSWORD → used for invalid login scenarios  

These variables are configured locally via `.env` and recreated dynamically in the CI pipeline.

---

### 5. Run Tests

Run full test suite:

```bash
pytest -s -v
```

Run a specific test file:

```bash
pytest tests/test_users.py -s -v
```

Generate reports:

```bash
pytest -s -v --html=report.html
pytest -s -v --junitxml=report.xml
```

---

## Authentication Flow

1. A user is dynamically generated  
2. The user is registered via `/auth/register`  
3. The user logs in via `/auth/login`  
4. An access token is extracted  
5. The token is reused across tests via fixtures  

---

## Utilities

- `data_factory.py` → Generates valid user data using Faker  
- `negative_factory.py` → Generates invalid test inputs  
- `token_factory.py` → Generates invalid and malformed tokens  
- `validators.py` → Performs JSON schema validation  

---

## Schema Validation

All API responses are validated against JSON schemas to ensure:

- Field presence  
- Data type correctness  
- Response consistency  

---

## CI Pipeline

This project uses GitHub Actions to automatically run tests on every push and pull request.

### How the CI Pipeline Works

The pipeline is triggered automatically on:

- Push to any branch  
- Pull request creation or update  

For every run:

1. A clean environment is created  
2. Python is installed  
3. Dependencies are installed  
4. Environment variables are configured  
5. The full test suite is executed  
6. A test report is generated  

---

### Failure Handling

- If any test fails, the pipeline fails automatically  
- Errors are clearly visible in CI logs  
- No failures are suppressed  

---

## Test Reporting

A JUnit XML report is generated in CI:

```bash
pytest -s -v --junitxml=report.xml
```

The report is uploaded as an artifact in GitHub Actions.

---

## Code Quality

- Modular and maintainable structure  
- Reusable utilities and fixtures  
- Clear naming conventions  
- Separation of concerns  
- Scalable design  

---

## How to Extend

- Add new tests in `/tests`  
- Add new schemas in `/schemas`  
- Add new data generators in `/utils`  
- Expand negative and edge case coverage  

---

## Summary

This framework is designed to be:

- Easy to clone  
- Easy to run  
- Easy to extend  
- Fully reproducible  
- Structured like a production-grade automation project  

---

## Author

Robert Ghandi  
API Automation Project