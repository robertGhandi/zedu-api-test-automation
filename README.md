# 🧪 Zedu API Automation Framework (Pytest)

A structured and scalable API automation testing framework built using Python (Pytest) for testing the Zedu platform APIs.

This project demonstrates authentication handling, positive/negative/edge case testing, dynamic test data generation, clean architecture, and reusable utilities.

---

# 📌 Project Overview

This framework automates REST API testing for the Zedu platform:

- 🌐 Application: https://zedu.chat/
- 📘 Swagger Docs: https://api.zedu.chat/swagger/#/

It validates authentication, user operations, audit logs, and API error handling.

---

# ⚙️ Tech Stack

- Python 3.10+
- Pytest
- Requests
- python-dotenv
- Faker
- jsonschema

---

# 📁 Project Structure

project/  
├── tests/  
│   ├── test_auth_login.py  
│   ├── test_users.py  
│   ├── test_audit_logs.py  
│  
├── utils/  
│   ├── data_factory.py  
│   ├── negative_factory.py  
│  
├── conftest.py  
├── requirements.txt  
├── .env.example  
└── README.md  

---

# 🚀 Features

- Dynamic authentication (no hardcoded tokens)
- Reusable fixtures for login and headers
- Positive, negative, and edge test coverage
- Fully independent and idempotent tests
- Dynamic test data generation
- Schema-ready response validation
- Clean separation of test logic and utilities

---

# 🧪 Test Coverage

## Authentication
- Successful login
- Invalid credentials
- Unregistered email
- Missing fields
- Empty payload

## Users
- User profile retrieval
- Status updates
- Invalid user ID handling

## Audit Logs
- Authorized access
- Unauthorized access
- Invalid or malformed tokens

---

# 🛠️ Setup Instructions

## 1. Clone Repository
git clone <repo-url>  
cd <project-folder>  

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

---

## 4. Environment Setup

Create a `.env` file in the root directory:

BASE_URL=https://api.zedu.chat  

Do NOT commit `.env` to GitHub.

---

## 5. Run Tests

Run all tests:
pytest -s -v  

Run specific file:
pytest tests/test_auth_login.py -s -v  

---

# 🧪 Testing Principles

- Each test is independent
- Tests are idempotent (can run multiple times safely)
- No hardcoded tokens or credentials
- All test data is dynamically generated
- Clear and descriptive test naming

---

# 🔐 Authentication Flow

1. User is dynamically generated
2. User is registered via /auth/register
3. User logs in via /auth/login
4. Access token is extracted automatically
5. Token is reused via fixtures

---

# 📦 Utilities

## data_factory.py
Generates valid user data dynamically using Faker.

## negative_factory.py
Generates invalid test data such as:
- Invalid emails
- Weak passwords
- Unregistered users
- Malformed tokens

---

# ⚠️ Important Notes

- Ensure BASE_URL is correctly set in .env
- Run tests from project root directory
- API must be accessible for tests to pass

---

# 🧼 Code Quality

- Modular architecture
- Reusable components
- Clean separation of concerns
- Scalable test design
- Maintainable structure

---

# 📌 How to Extend

- Add new tests in /tests
- Add new data generators in /utils
- Add schema validation in /schemas
- Expand negative and edge coverage

---

# 🏁 Summary

This framework is designed to be:
- Easy to clone
- Easy to run
- Easy to extend
- Production-style structured

---

# 👨‍💻 Author

API Automation Project – Stage 3 Submission