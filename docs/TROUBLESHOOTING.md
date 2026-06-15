# Troubleshooting Guide

## Common Issues & Solutions

### 1. File Upload Issues

#### Issue: "Invalid JSON file" error
**Symptoms:** Cannot upload Postman collection
**Causes:**
- File is not valid JSON
- File format is not JSON
- Corrupted file

**Solutions:**
```bash
# Validate JSON using jsonlint
npm install -g jsonlint
jsonlint your_collection.json

# Or use Python to validate
python -c "import json; json.load(open('collection.json'))"
```

#### Issue: Collection file not found
**Symptoms:** File picker shows no files
**Causes:**
- Browser permissions issue
- File in unsupported location

**Solutions:**
- Allow browser file access
- Move file to Desktop or Documents
- Try different browser

---

### 2. Test Generation Issues

#### Issue: No tests generated
**Symptoms:** Empty test file after generation
**Causes:**
- Collection has no items
- No valid request objects
- Parsing error

**Solutions:**
```json
// Verify collection structure
{
  "item": [           // Must have "item" array
    {
      "name": "Test",
      "request": {    // Must have "request" object
        "method": "GET",
        "url": "https://api.example.com"
      }
    }
  ]
}
```

#### Issue: Generated code has syntax errors
**Symptoms:** Python errors when running tests
**Causes:**
- Special characters in variable names
- Invalid JSON in request bodies
- Malformed URLs

**Solutions:**
```python
# Sanitize variable names
# Bad: def test_Get-Users(headers):  # Hyphen not allowed
# Good: def test_get_users(headers):

# Validate request body JSON
# Escape special characters properly
payload = {"name": "John \"Doe\""}  # Escape quotes
```

---

### 3. Test Execution Issues

#### Issue: "Connection refused" error
**Symptoms:** Tests fail to connect to API
**Causes:**
- API server not running
- Wrong BASE_URL
- Network issues

**Solutions:**
```bash
# Check if server is running
ping api.example.com

# Verify correct URL in conftest.py
BASE_URL = "https://api.example.com"  # Check protocol, domain

# Test connectivity
curl https://api.example.com/health
```

#### Issue: Authentication failures (401 errors)
**Symptoms:** All tests fail with 401 Unauthorized
**Causes:**
- Invalid credentials
- Token expired
- Wrong header format

**Solutions:**
```python
# Check credentials in conftest.py
TEST_USER_EMAIL = "user@test.com"
TEST_USER_PASSWORD = "correct_password"

# Verify token is included
headers = {
    "Authorization": "Bearer your_token_here",
    "Content-Type": "application/json"
}

# Test login manually
response = requests.post(
    "https://api.example.com/auth/login",
    json={"email": email, "password": password}
)
print(response.json())
```

#### Issue: Tests timeout
**Symptoms:** "Timeout waiting for response"
**Causes:**
- API is slow
- Network latency
- Timeout value too low

**Solutions:**
```bash
# Increase timeout in pytest.ini
[pytest]
timeout = 60

# Or in test
@pytest.mark.timeout(30)
def test_slow_endpoint(auth_headers):
    pass
```

#### Issue: "AssertionError: Expected 200, got 500"
**Symptoms:** API returns error status
**Causes:**
- Server error
- Invalid request
- Data validation issue

**Solutions:**
```bash
# Check server logs
tail -f /var/log/app.log

# Test endpoint manually
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John"}'

# Check response
print(response.text)
print(response.headers)
```

---

### 4. Browser Issues

#### Issue: Page doesn't load
**Symptoms:** Blank page or "Cannot GET"
**Causes:**
- Server not running
- Wrong port
- JavaScript error

**Solutions:**
```bash
# Start server correctly
python -m http.server 8000

# Check different port
python -m http.server 8001

# Check browser console (F12) for errors
# Look for JavaScript errors or CORS issues
```

#### Issue: CORS errors in browser console
**Symptoms:** "Cross-Origin Request Blocked"
**Causes:**
- API doesn't allow cross-origin requests
- Using file:// protocol instead of http://

**Solutions:**
```bash
# Always use local server, not file://
python -m http.server 8000
# Then go to http://localhost:8000/index.html

# If API needs CORS headers, configure server
# This is not an issue with test runner
```

#### Issue: File upload drag & drop not working
**Symptoms:** Cannot drop files on upload zone
**Causes:**
- Browser doesn't support drag & drop
- JavaScript disabled
- Browser restrictions

**Solutions:**
- Use "Click to browse" button instead
- Enable JavaScript
- Try different browser
- Update browser to latest version

---

### 5. Code Generation Issues

#### Issue: Variables have confusing names
**Symptoms:** test_test_test_test_1 or similar
**Causes:**
- Repeated names in collection
- Special characters in names

**Solutions:**
```python
# Rename tests in conftest.py after generation
# Or edit Postman collection before export with better names
```

#### Issue: Missing test assertions
**Symptoms:** Generated tests don't have assertions
**Causes:**
- Postman collection has no test scripts
- Test scripts not in correct format

**Solutions:**
```javascript
// In Postman, add tests like this:
pm.test('Status is 200', function() {
    pm.response.to.have.status(200);
});

pm.test('Has token', function() {
    pm.expect(pm.response.json()).to.have.property('token');
});
```

---

### 6. Report Generation Issues

#### Issue: Report is empty
**Symptoms:** No data in reports page
**Causes:**
- No tests have been run
- Tests generated but not executed

**Solutions:**
```bash
# Generate tests first
1. Click "Code Generator" tab
2. Click "Generate Tests"

# Then run tests
1. Click "Test Runner" tab
2. Click "Run pytest"

# Then view reports
1. Click "Reports" tab
```

#### Issue: Report download fails
**Symptoms:** Download doesn't start
**Causes:**
- Browser blocks downloads
- No report data to download

**Solutions:**
- Check browser download settings
- Disable ad blockers
- Allow popups if needed
- Ensure tests have been run

---

### 7. Performance Issues

#### Issue: Page is slow
**Symptoms:** Lag when clicking buttons
**Causes:**
- Large collection (1000+ APIs)
- Browser memory issues
- Slow computer

**Solutions:**
```javascript
// Split large collections into smaller ones
// Instead of one collection with 1000 APIs,
// create 10 collections with 100 APIs each

// Close other browser tabs
// Restart browser
// Use Chrome instead of other browsers
```

#### Issue: Test execution is slow
**Symptoms:** Tests take very long to run
**Causes:**
- Network latency
- Server is slow
- Too many sequential requests

**Solutions:**
```bash
# Run tests in parallel (requires pytest-xdist)
pip install pytest-xdist
pytest -n auto

# Reduce number of tests
# Use markers to run only critical tests
pytest -m smoke

# Optimize test fixtures
# Run once per session instead of per test
@pytest.fixture(scope="session")
def auth_headers():
    pass
```

---

### 8. Environment Issues

#### Issue: "Command not found: python"
**Symptoms:** Python command not recognized
**Causes:**
- Python not installed
- Not in PATH

**Solutions:**
```bash
# Check if installed
python --version
python3 --version

# Add to PATH (Windows)
# Or use full path: C:\Python39\python.exe

# Install Python from python.org
```

#### Issue: "No module named pytest"
**Symptoms:** Import error when running tests
**Causes:**
- pytest not installed
- Wrong Python environment

**Solutions:**
```bash
# Install dependencies
pip install -r requirements.txt

# Or specific package
pip install pytest requests

# Check installation
pip show pytest
```

#### Issue: Virtual environment issues
**Symptoms:** Packages installed but not found
**Causes:**
- Virtual environment not activated
- Different Python interpreters

**Solutions:**
```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Verify activation (should show venv prefix)
```

---

### 9. Data & Payload Issues

#### Issue: "JSON decode error"
**Symptoms:** Cannot parse response body
**Causes:**
- Response is not JSON
- Empty response
- HTML error page returned

**Solutions:**
```python
# Check response content type
print(response.headers['content-type'])

# Check response text
print(response.text)

# Use optional parsing
try:
    data = response.json()
except json.JSONDecodeError:
    print(f"Response not JSON: {response.text}")
```

#### Issue: Request body not formatted correctly
**Symptoms:** "Invalid JSON" or "Bad request"
**Causes:**
- Quotes not escaped
- Invalid data types
- Missing required fields

**Solutions:**
```python
# Use correct JSON format
payload = {
    "name": "John",           # String in quotes
    "age": 30,                # Number without quotes
    "active": True,           # Boolean (capitalize)
    "tags": ["python", "api"] # Array
}

# Validate before sending
import json
json_str = json.dumps(payload)
print(json_str)
```

---

### 10. Getting Help

If issue not listed above:

1. **Check browser console** (F12)
   - Look for JavaScript errors
   - Check network tab for API calls

2. **Check pytest output**
   ```bash
   pytest -vv -s
   ```

3. **Enable debug logging**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

4. **Review collection structure**
   - Ensure valid JSON
   - Check all required fields

5. **Isolate the problem**
   - Test with demo collection first
   - Test single API at a time
   - Test with simple request

6. **Check documentation**
   - [README.md](../README.md)
   - [USAGE_GUIDE.md](USAGE_GUIDE.md)
   - [INSTALLATION.md](INSTALLATION.md)

---

## Still Need Help?

- 📧 Email: support@example.com
- 💬 GitHub Issues: [Create an issue](https://github.com/yourusername/issues)
- 📚 Documentation: [Full docs](https://github.com/yourusername/wiki)

---

**Last Updated:** June 2024
