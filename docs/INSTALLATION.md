# Installation Guide

## System Requirements

- **Python**: 3.8 or higher
- **pip**: Latest version
- **Browser**: Chrome, Firefox, Safari, or Edge (latest versions)
- **Operating System**: Windows, macOS, or Linux

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/postman-collection-to-pytest-migrator.git
cd postman-collection-to-pytest-migrator
```

### 2. Create Virtual Environment (Optional but Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python --version  # Should be 3.8+
pytest --version   # Should be installed
```

## Running the Application

### Option 1: Direct Browser Opening
Simply open `index.html` in your web browser:
```bash
# Windows
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

### Option 2: Local Development Server

**Using Python's built-in server:**
```bash
python -m http.server 8000
```
Then navigate to: `http://localhost:8000`

**Using Node.js (if installed):**
```bash
npx http-server
```

### Option 3: Live Server (VS Code)

1. Install "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

## Environment Setup

### Create `.env` File

```bash
# Create file in project root
API_BASE_URL=https://api.example.com
TEST_USER_EMAIL=user@test.com
TEST_USER_PASSWORD=secret123
```

### Load Environment Variables

**Python:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_url = os.getenv('API_BASE_URL')
```

## Troubleshooting

### Issue: "No module named 'pytest'"
**Solution:**
```bash
pip install pytest requests
```

### Issue: Port 8000 already in use
**Solution:**
```bash
# Use different port
python -m http.server 8001
```

### Issue: CORS errors in browser
**Solution:**
Run with a local server instead of `file://` protocol

## Docker Setup (Optional)

### Build Docker Image
```bash
docker build -t postman-pytest-migrator .
```

### Run Container
```bash
docker run -p 8000:8000 postman-pytest-migrator
```

## Advanced Configuration

### pytest Configuration File

Create `pytest.ini`:
```ini
[pytest]
testpaths = test_cases
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short --strict-markers
markers =
    smoke: smoke tests
    regression: regression tests
    integration: integration tests
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest test_cases/test_ecommerce_api.py

# Run with markers
pytest -m smoke

# Run with coverage
pytest --cov=test_cases

# Run in verbose mode
pytest -v
```

## Next Steps

1. ✅ Verify installation: `pytest --version`
2. ✅ Open the application: `python -m http.server 8000`
3. ✅ Upload a Postman collection
4. ✅ Generate tests
5. ✅ Review generated code
6. ✅ Run tests

## Support

If you encounter issues:
1. Check the [TROUBLESHOOTING.md](TROUBLESHOOTING.md) guide
2. Review browser console for errors (F12)
3. Check Python version compatibility
4. Ensure all dependencies are installed

---

**Happy Testing!** 🚀
