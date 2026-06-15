Postman Collection to Pytest Migrator
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
Plain text
User Uploads Collection
          │
          ▼
Collection Parser
          │
          ▼
Extract API Details
          │
          ▼
Pytest Generator
          │
          ▼
Generate test_api.py
          │
          ▼
Download Generated File
Folder Structure
Plain text
postman-pytest-migrator/
│
├── app.py
├── collection_parser.py
├── pytest_generator.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── uploads/
│
├── generated_tests/
│
├── sample_data/
│   ├── sample_collection.json
│   └── expected_output.py
│
├── test_cases/
│   └── test_app.py
│
└── README.md
Installation
Step 1: Clone Repository
Bash
git clone https://github.com/yourusername/postman-pytest-migrator.git
Step 2: Move to Project Directory
Bash
cd postman-pytest-migrator
Step 3: Install Dependencies
Bash
pip install flask pytest
Running the Application
Start the Flask server:
Bash
python app.py
Open browser:
Plain text
http://127.0.0.1:5000
Usage
Upload Collection
Open application.
Click Upload File.
Select Postman Collection JSON file.
Click Generate Pytest.
Download Output
The application generates a Pytest script automatically.
Example Output:
Python
import requests

def test_get_users():
    response = requests.get("https://api.example.com/users")
    assert response.status_code == 200
Assumptions
Input file is a valid Postman Collection v2.x JSON.
API endpoints are accessible.
Authentication details are already included in the collection.
Generated tests focus on API request execution and status code validation.
Limitations
Complex JavaScript test scripts from Postman are not converted.
Dynamic variables may require manual adjustment.
Environment files are not currently supported.
Advanced assertions need manual enhancement.
Sample Input
JSON
{
  "info": {
    "name": "User API Collection"
  }
}
Sample Output
Python
def test_api():
    response = requests.get("https://example.com")
    assert response.status_code == 200
Test Cases
Happy Path
Valid Postman Collection uploaded
Pytest file generated successfully
Negative Cases
Invalid JSON file
Empty file upload
Unsupported file format
Run tests:
Bash
pytest
AI Usage Note
AI Assistance Used
Generated Flask boilerplate code
Helped create parser logic
Assisted in Pytest generation logic
Generated documentation
Best Prompts Used
"Convert Postman collection JSON to Pytest script."
"Create Flask application for file upload and download."
"Generate README for Postman to Pytest Migrator."
AI Limitations
Generated code required manual validation.
Some edge cases needed custom handling.
Future Enhancements
Support Postman Environment Variables
Convert Postman Assertions to Pytest Assertions
Generate Test Reports
Docker Deployment
CI/CD Integration using GitHub Actions
Team Details
Project Title: Postman Collection to Pytest Migrator
Domain: API Testing Automation
Developed For: Infinite Tech Round AI Prototype Challenge
