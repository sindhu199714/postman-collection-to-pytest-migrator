Project Overview
The Postman Collection to Pytest Migrator is a web-based tool that automatically converts Postman API collections into Python Pytest test scripts. The application helps QA engineers and developers reduce manual effort by generating reusable automated test cases from existing Postman collections.
Problem Statement
API testing teams often create and maintain Postman collections for testing APIs. However, migrating these collections to automated testing frameworks such as Pytest requires significant manual effort.
This project automates the migration process by analyzing a Postman Collection JSON file and generating equivalent Pytest test scripts.
Features
Upload Postman Collection (.json) files
Parse API requests from the collection
Extract:
Request URL
HTTP Method
Headers
Request Body
Generate Pytest test cases automatically
Download generated test scripts
User-friendly web interface
Reduces manual test creation effort
Technology Stack
Frontend
HTML
CSS
JavaScript
Backend
Python
Flask
Testing Framework
Pytest
Project Architecture
