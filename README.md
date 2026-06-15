# Postman to Pytest Migrator 🚀

[![GitHub](https://img.shields.io/badge/GitHub-postman--pytest--migrator-blue?logo=github)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](https://github.com)

**Convert Postman API Collections into Automated Pytest Test Suites** - Transform your API documentation into production-ready test code with a single click.

## 🎯 Overview

The **Postman to Pytest Migrator** is an intelligent tool that automatically converts Postman Collection JSON files into comprehensive pytest test suites. This eliminates manual test creation, reduces human error, and enables teams to maintain consistent API test coverage.

### Key Features ✨

- 📥 **Seamless Import** - Upload Postman v2.0/v2.1 collection files
- 🎯 **Automatic Test Generation** - Convert API requests to pytest code instantly
- 📊 **Test Execution** - Run generated tests directly from the UI
- 📈 **Comprehensive Reports** - View test results, coverage metrics, and API breakdowns
- 🎨 **Beautiful Dashboard** - Modern, responsive interface with real-time analytics
- 💾 **Export Support** - Download generated test files and reports
- 🔍 **API Viewer** - Browse and filter all extracted APIs by method
- ⚡ **Live Preview** - See generated code before downloading

---

## 🚀 Quick Start

### Installation & Setup

#### Prerequisites
- Python 3.8 or higher
- A web browser (Chrome, Firefox, Safari, Edge)
- Postman Collection JSON file (exported from Postman)

#### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/postman-pytest-migrator.git
   cd postman-collection-to-pytest-migrator
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Open the Application**
   - Open `index.html` in your web browser
   - Or use a local server:
   ```bash
   python -m http.server 8000
   # Then navigate to http://localhost:8000
   ```

4. **Upload Your Postman Collection**
   - Click "Upload Collection" tab
   - Drop your `.json` file or click to browse
   - View all extracted APIs

5. **Generate Tests**
   - Go to "Code Generator" tab
   - Click "Generate Tests"
   - Review the generated pytest code
   - Download `test_api.py`

6. **Run Tests**
   - Navigate to "Test Runner" tab
   - Click "Run pytest"
   - View detailed test results and reports

---

## 📁 Project Structure

```
postman-collection-to-pytest-migrator/
├── index.html                          # Main UI application
├── README.md                           # This file
├── AI USAGE NOTE.md                    # AI assistance documentation
├── DEMO_VIDEO_LINK.md                  # Demo video reference
├── requirements.txt                    # Python dependencies
│
├── sample_data/                        # Sample Postman collections
│   ├── ecommerce-api.json
│   ├── user-management-api.json
│   └── weather-api.json
│
├── test_cases/                         # Generated test samples
│   ├── test_api.py
│   ├── conftest.py
│   └── test_results/
│
├── docs/                               # Documentation
│   ├── INSTALLATION.md
│   ├── USAGE_GUIDE.md
│   ├── API_REFERENCE.md
│   └── TROUBLESHOOTING.md
│
└── assets/                             # Icons, images, resources
    ├── logo.png
    └── screenshots/
```

---

## 💡 How It Works

### 1. Collection Upload
```
Postman JSON
    ↓
Parse Collection Structure
    ↓
Extract API Details
```

### 2. Test Generation
```
API Details (Method, URL, Headers, Body, Tests)
    ↓
Generate Pytest Functions
    ↓
Create conftest.py Fixtures
```

### 3. Execution & Reporting
```
Run Generated Tests
    ↓
Collect Results
    ↓
Generate Reports with Metrics
```

---

## 📊 Features Explained

### Dashboard
- **Total APIs** - Count of all extracted endpoints
- **Tests Generated** - Number of test functions created
- **Tests Passed** - Successful test executions
- **Coverage** - Percentage of passing tests
- **Recent Activity** - Quick view of latest imports
- **API Methods Breakdown** - Visual distribution of HTTP methods

### Upload Page
- Drop zone for easy file upload
- Supported format: Postman Collection JSON (v2.0 & v2.1)
- Demo collection for quick testing

### API Viewer
- Filterable table of all extracted APIs
- Filter by HTTP method (GET, POST, PUT, DELETE)
- View request details: URL, headers, body, assertions
- Badge showing number of test assertions per API

### Code Generator
- **Preview** - Live preview of generated pytest code
- **conftest.py** - Shared fixtures and configurations
- **Download** - Export generated files

### Test Runner
- Execute generated tests in real-time
- View pass/fail status for each test
- Performance metrics (execution time)
- Console output with detailed logs

### Reports
- **Coverage Chart** - Pass/fail/pending breakdown
- **API Methods Chart** - Distribution of HTTP methods
- **Summary Statistics** - Comprehensive metrics
- **Export Reports** - Download as text files

---

## 🔧 Configuration

### Sample Environment Variables
Create a `.env` file in the project root:

```env
# API Server
API_BASE_URL=https://api.example.com
API_TIMEOUT=30

# Authentication
AUTH_TOKEN=your_api_token
AUTH_TYPE=bearer

# Pytest Configuration
PYTEST_MARKERS=smoke,regression
PYTEST_TIMEOUT=60
```

---

## 📝 Sample Postman Collection

### Example Structure
```json
{
  "info": {
    "name": "E-Commerce API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Login",
      "request": {
        "method": "POST",
        "url": "https://api.example.com/auth/login",
        "header": [{"key": "Content-Type", "value": "application/json"}],
        "body": {"mode": "raw", "raw": "{\"email\": \"user@test.com\"}"}
      },
      "event": [
        {
          "listen": "test",
          "script": {
            "exec": [
              "pm.test('Status is 200', function() { pm.response.to.have.status(200); })"
            ]
          }
        }
      ]
    }
  ]
}
```

---

## 🧪 Generated Test Example

### Generated test_api.py
```python
import pytest
import requests

BASE_URL = "https://api.example.com"

def test_login(auth_headers):
    """Login — POST https://api.example.com/auth/login"""
    payload = {"email": "user@test.com", "password": "secret123"}
    response = requests.post(
        BASE_URL + "/auth/login",
        json=payload,
        headers=auth_headers
    )
    
    assert response.status_code == 201, \
        f"Expected 201, got {response.status_code}"
    assert "token" in response.json(), "Response missing 'token' field"

def test_get_users(auth_headers):
    """Get Users — GET https://api.example.com/users"""
    response = requests.get(
        BASE_URL + "/users",
        headers=auth_headers
    )
    
    assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}"
    assert isinstance(response.json(), list), "Response must be an array"
```

### Generated conftest.py
```python
import pytest
import requests

BASE_URL = "https://api.example.com"

@pytest.fixture(scope="session")
def auth_headers():
    """Authenticate once per test session and return headers."""
    response = requests.post(
        BASE_URL + "/auth/login",
        json={"email": "user@test.com", "password": "secret123"}
    )
    assert response.status_code == 200, "Login failed during setup"
    token = response.json().get("token", "")
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

@pytest.fixture(autouse=True)
def log_test(request):
    """Log test name before each test."""
    print(f"\n▶ Running: {request.node.name}")
    yield
    print(f"  ✓ Done: {request.node.name}")
```

---

## 📚 Usage Guide

### Basic Workflow

1. **Export Postman Collection**
   - Open Postman
   - Right-click collection → Export
   - Choose JSON format → Save file

2. **Upload to Migrator**
   - Open the application
   - Go to Upload tab
   - Drop or select your JSON file

3. **Preview APIs**
   - Switch to API Viewer tab
   - Filter by method if needed
   - Verify all endpoints extracted

4. **Generate Tests**
   - Go to Code Generator
   - Click "Generate Tests"
   - Preview code in tabs

5. **Run Tests**
   - Navigate to Test Runner
   - Click "Run pytest"
   - View results and metrics

6. **Export Results**
   - Download test files
   - Download test report
   - Share with team

---

## 🎓 Advanced Features

### Custom Fixtures
Modify `conftest.py` to add custom fixtures:

```python
@pytest.fixture
def admin_headers():
    """Admin authentication fixture"""
    return {
        "Authorization": "Bearer admin_token",
        "Content-Type": "application/json"
    }
```

### Parametrized Tests
Enhance generated tests with parameterization:

```python
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user(auth_headers, user_id):
    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        headers=auth_headers
    )
    assert response.status_code == 200
```

### Retry Logic
Add automatic retries for flaky tests:

```python
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_api_endpoint(auth_headers):
    # Test code
    pass
```

---

## 🐛 Troubleshooting

### Issue: Collection not uploading
**Solution:**
- Verify JSON file is valid (use JSONLint)
- Ensure file is Postman v2.0 or v2.1 format
- Check browser console for errors

### Issue: Tests fail with authentication errors
**Solution:**
- Update `BASE_URL` in generated code
- Verify credentials in `conftest.py`
- Check API server is running

### Issue: Generated code has syntax errors
**Solution:**
- Review request body format (should be valid JSON)
- Check for special characters in URLs
- Verify Postman tests use valid JavaScript

### Issue: Page doesn't load
**Solution:**
- Clear browser cache (Ctrl+Shift+Delete)
- Disable browser extensions
- Try in different browser
- Check console for JavaScript errors

---

## 🔒 Security

### Best Practices
- ✅ Never commit sensitive credentials to repository
- ✅ Use environment variables for API tokens
- ✅ Sanitize request bodies before sharing
- ✅ Review generated code for exposed secrets
- ✅ Use HTTPS for all API endpoints

### Credential Management
Store credentials in environment variables:

```bash
export API_TOKEN="your_secure_token"
export API_BASE_URL="https://api.example.com"
```

Access in Python:

```python
import os
api_token = os.getenv("API_TOKEN")
base_url = os.getenv("API_BASE_URL")
```

---

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/postman-pytest-migrator.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Keep code clean and well-commented
   - Follow PEP 8 style guide
   - Add tests for new features

4. **Commit & Push**
   ```bash
   git commit -m "Add: your feature description"
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Describe changes clearly
   - Reference any related issues
   - Include screenshots if UI changes

---

## 📋 Roadmap

### Upcoming Features 🔮
- [ ] Support for Postman Collections v2.2
- [ ] GraphQL API support
- [ ] OpenAPI/Swagger import
- [ ] Docker containerization
- [ ] CI/CD integration templates
- [ ] Collaborative test editing
- [ ] Test scheduling & automation
- [ ] API mocking server
- [ ] Performance testing metrics
- [ ] Custom assertion templates

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team

**QA-09 Team Members:**
- Sudha Rani - Project Lead
- Pavi - UI/UX Developer
- Sindhu Priya - Backend Developer
- Racha - QA Engineer

---

## 📞 Support & Contact

- **Issues & Bugs** - [GitHub Issues](https://github.com/yourusername/issues)
- **Discussions** - [GitHub Discussions](https://github.com/yourusername/discussions)
- **Email** - support@example.com
- **Documentation** - See [docs/](docs/) folder

---

## 🎥 Demo & Resources

- **Demo Video** - [Watch on Loom](https://www.loom.com/share/e7ed349221264aeda75522d3685af9fb)
- **Sample Collections** - See [sample_data/](sample_data/) folder
- **Test Examples** - See [test_cases/](test_cases/) folder

---

## 🙏 Acknowledgments

- Thanks to the Postman team for excellent API documentation
- pytest community for robust testing framework
- Chart.js for beautiful data visualization
- FontAwesome for clean icons

---

## ⭐ Show Your Support

If you find this tool useful, please consider:
- ⭐ Starring the repository
- 📢 Sharing with your team
- 💬 Leaving feedback or suggestions
- 🐛 Reporting bugs
- 🔧 Contributing improvements

---

**Happy Testing! 🚀**

---

*Last Updated: June 2024*
*Version: 1.0.0*
*Status: Production Ready*

Demo Link :- https://www.loom.com/share/8f249a2048e14aa7b719abebfa0386bc

