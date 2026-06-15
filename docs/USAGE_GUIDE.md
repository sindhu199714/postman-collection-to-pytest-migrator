# Usage Guide

## Quick Start Workflow

### 1. Launch the Application

```bash
python -m http.server 8000
```

Open: `http://localhost:8000/index.html`

### 2. Dashboard Overview

The Dashboard shows:
- **Total APIs** - Number of endpoints in collection
- **Tests Generated** - Number of test functions created
- **Tests Passed** - Successful test executions
- **Coverage** - Percentage of passing tests
- **Recent Activity** - List of latest imports
- **API Methods Breakdown** - Chart of HTTP methods distribution

### 3. Upload a Postman Collection

**Step 1:** Go to **Upload** tab
```
Navigation: Upload → Import Postman Collection JSON
```

**Step 2:** Choose file method
- **Drag & Drop**: Drop your `collection.json` file
- **Click to Browse**: Select file from computer

**Step 3:** Supported formats
- Postman v2.0 format
- Postman v2.1 format
- Valid JSON structure

**Step 4:** Verify import
- Success message shows number of APIs found
- Navigate to API Viewer to verify

### 4. View Extracted APIs

**Step 1:** Go to **API Viewer** tab

**Step 2:** Filter by HTTP method
```
Available filters: ALL | GET | POST | PUT | DELETE
```

**Step 3:** Review API details
```
Table columns:
- # - Sequential number
- Name - API endpoint name
- Method - HTTP method (GET, POST, etc.)
- URL - Endpoint URL
- Assertions - Number of test assertions
- Headers - Number of custom headers
```

**Example:**
```
# | Name          | Method | URL                        | Assertions | Headers
1 | Login         | POST   | /auth/login               | 2          | 1
2 | Get Users     | GET    | /users                    | 2          | 1
3 | Create User   | POST   | /users                    | 2          | 1
```

### 5. Generate Test Code

**Step 1:** Go to **Code Generator** tab

**Step 2:** Click **Generate Tests** button
- Processing takes ~1-2 seconds
- Shows loading spinner during generation

**Step 3:** Review generated code
Two tabs available:
- **Preview** - Main test file (`test_api.py`)
- **conftest.py** - Shared fixtures and configurations

**Step 4:** Verify test structure
```python
# Generated test example
def test_auth_login(auth_headers):
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
```

**Step 5:** Download files
- Click **Download test_api.py** to save main test file
- `conftest.py` contains fixtures

### 6. Run Tests

**Step 1:** Go to **Test Runner** tab

**Step 2:** Click **Run pytest** button
- Tests execute with real-time progress
- Shows progress bar

**Step 3:** Monitor execution
```
Metrics displayed:
- Total - Number of tests
- Passed - Successful tests (green)
- Failed - Failed tests (red)
```

**Step 4:** View detailed results
```
Each test shows:
✓ Status (pass/fail icon)
  Test name (function name)
  Method (HTTP method)
  Duration (ms)
```

**Step 5:** Check console output
```
Console section shows:
- Platform and Python version
- Number of collected items
- Individual test results
- Summary statistics
```

### 7. Generate Reports

**Step 1:** Go to **Reports** tab

**Step 2:** View charts
- **Test Coverage** (Doughnut chart)
  - Passed tests (green)
  - Failed tests (red)
  - Pending tests (gray)

- **API Methods** (Bar chart)
  - Distribution of GET, POST, PUT, DELETE, PATCH

**Step 3:** Review summary
```
Summary includes:
- Total APIs
- Number Passed
- Coverage Percentage
- Failed and Pending counts
- Progress bar visualization
```

**Step 4:** Download report
```
Click "Download Report" to get text file:
QA-09 — Postman → Pytest Migration Report

Summary:
  Total APIs    : 5
  Tests Generated: 5
  Passed         : 4
  Failed         : 1
  Coverage       : 80%

API List:
  [PASS] POST /auth/login — Login
  [PASS] GET /users — Get Users
  [PASS] POST /users — Create User
  [PASS] PUT /users/1 — Update User
  [FAIL] DELETE /users/1 — Delete User
```

---

## Advanced Usage

### Using Demo Collection

For quick testing without uploading your own collection:

**Step 1:** Go to **Upload** tab

**Step 2:** Click **Load Demo Collection** button

**Step 3:** Demo includes 5 sample APIs:
- Login (POST)
- Get Users (GET)
- Create User (POST)
- Update Profile (PUT)
- Delete User (DELETE)

### Custom Test Modification

After downloading `test_api.py`, customize:

```python
# Add custom fixtures
@pytest.fixture
def admin_headers():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "admin@test.com", "password": "admin123"}
    )
    token = response.json()["token"]
    return {"Authorization": f"Bearer {token}"}

# Add parametrized tests
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user_by_id(auth_headers, user_id):
    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        headers=auth_headers
    )
    assert response.status_code == 200

# Add retry logic
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_flaky_endpoint(auth_headers):
    response = requests.get(
        f"{BASE_URL}/users",
        headers=auth_headers
    )
    assert response.status_code == 200
```

### Running Tests Locally

```bash
# Navigate to test directory
cd test_cases

# Run all tests
pytest

# Run specific test
pytest test_ecommerce_api.py::test_auth_login -v

# Run with markers
pytest -m smoke -v

# Generate coverage report
pytest --cov=. --cov-report=html

# Run with custom output
pytest -v --tb=short --html=report.html
```

### Environment Variables

Create `.env` file:
```env
API_BASE_URL=https://api.example.com
TEST_USER_EMAIL=user@test.com
TEST_USER_PASSWORD=password123
PYTEST_TIMEOUT=30
```

### Filtering Tests

```python
# Mark tests
@pytest.mark.smoke
def test_login(auth_headers):
    pass

@pytest.mark.regression
def test_get_users(auth_headers):
    pass

@pytest.mark.critical
def test_create_user(auth_headers):
    pass

# Run marked tests
pytest -m smoke           # Smoke tests only
pytest -m "not slow"      # All except slow
pytest -m "smoke or regression"  # Smoke or regression
```

---

## Tips & Tricks

### 1. Organize Large Collections
- Use folders in Postman
- Group related endpoints
- Apply consistent naming

### 2. Optimize Test Generation
- Remove unnecessary assertions
- Keep API request bodies simple
- Use meaningful test names

### 3. Improve Test Performance
- Minimize API calls
- Use session-scoped fixtures
- Cache authentication tokens

### 4. Better Error Messages
```python
# Clear assertion messages
assert response.status_code == 200, \
    f"Expected 200, got {response.status_code}\nResponse: {response.text}"
```

### 5. Debugging Failed Tests
```bash
# Verbose output
pytest -vv

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Show local variables on failure
pytest -l
```

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Collection not uploading | Ensure valid JSON format |
| Tests failing with 401 | Check authentication token |
| Timeout errors | Increase API timeout value |
| Missing properties | Verify API response structure |
| Port 8000 in use | Change to different port |

---

## Performance Optimization

### Test Execution Speed
```python
# Use session fixture for auth
@pytest.fixture(scope="session")
def auth_headers():
    # Runs only once per session
    pass

# Parallel execution (requires pytest-xdist)
pytest -n auto
```

### Memory Usage
```python
# Use generators for large data sets
def generate_test_data():
    for i in range(1000):
        yield {"id": i}

# Clean up after tests
@pytest.fixture
def cleanup():
    yield
    # Cleanup code here
```

---

## Integration with CI/CD

### GitHub Actions
```yaml
name: Test Suite
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - run: pip install -r requirements.txt
      - run: pytest
```

### Jenkins
```groovy
pipeline {
    stages {
        stage('Test') {
            steps {
                sh 'pytest --junitxml=results.xml'
            }
        }
    }
}
```

---

**Need more help?** Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
