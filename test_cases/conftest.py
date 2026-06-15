import pytest
import requests
import os
from typing import Dict
from datetime import datetime


BASE_URL = os.getenv("API_BASE_URL", "https://api.example.com")
TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL", "user@test.com")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD", "secret123")


# ─────────────────────────────────────────────
# Session Fixtures
# ─────────────────────────────────────────────

@pytest.fixture(scope="session")
def auth_headers() -> Dict[str, str]:
    """
    Authenticate once per test session and return authorization headers.
    
    Returns:
        Dictionary with Authorization header and Content-Type
    """
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": TEST_USER_EMAIL,
            "password": TEST_USER_PASSWORD
        }
    )
    
    assert response.status_code == 200, \
        f"Login failed: {response.status_code} - {response.text}"
    
    token = response.json().get("token", "")
    assert token, "No token received from login endpoint"
    
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


@pytest.fixture(scope="session")
def api_base_url() -> str:
    """Provide the base URL for all API calls"""
    return BASE_URL


# ─────────────────────────────────────────────
# Function Fixtures
# ─────────────────────────────────────────────

@pytest.fixture
def clean_headers(auth_headers) -> Dict[str, str]:
    """Fresh copy of headers for each test"""
    return auth_headers.copy()


@pytest.fixture
def response_data():
    """Store response data for test validation"""
    return {}


# ─────────────────────────────────────────────
# Auto-use Fixtures
# ─────────────────────────────────────────────

@pytest.fixture(autouse=True)
def log_test(request):
    """
    Automatically log test name before and after execution.
    Runs for every test automatically.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'='*60}")
    print(f"▶ {timestamp} | Running: {request.node.name}")
    print(f"{'='*60}")
    
    yield
    
    print(f"✓ {datetime.now().strftime('%H:%M:%S')} | Completed: {request.node.name}")


@pytest.fixture(autouse=True)
def handle_test_errors(request):
    """Handle and log test errors"""
    yield
    
    if request.node.rep_call.failed:
        print(f"\n⚠ Test Failed: {request.node.name}")
        if hasattr(request.node, 'rep_call'):
            print(f"Error: {request.node.rep_call.longrepr}")


# ─────────────────────────────────────────────
# Parametrize Fixtures
# ─────────────────────────────────────────────

@pytest.fixture(params=[200, 201, 400, 401, 403, 404, 500])
def status_code(request):
    """Fixture for testing different HTTP status codes"""
    return request.param


# ─────────────────────────────────────────────
# Markers
# ─────────────────────────────────────────────

def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line(
        "markers", "smoke: mark test as a smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as a regression test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "critical: mark test as critical"
    )


# ─────────────────────────────────────────────
# Hooks
# ─────────────────────────────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Make test result information available to fixtures"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test name"""
    for item in items:
        # Auto-mark tests as smoke if they contain 'smoke' in name
        if "smoke" in item.nodeid:
            item.add_marker(pytest.mark.smoke)
        # Auto-mark integration tests
        if "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)


# ─────────────────────────────────────────────
# Assertion Helpers
# ─────────────────────────────────────────────

class ResponseAssertions:
    """Helper class for common response assertions"""
    
    @staticmethod
    def assert_status_200(response):
        """Assert response status is 200"""
        assert response.status_code == 200, \
            f"Expected 200, got {response.status_code}: {response.text}"
    
    @staticmethod
    def assert_status_201(response):
        """Assert response status is 201"""
        assert response.status_code == 201, \
            f"Expected 201, got {response.status_code}: {response.text}"
    
    @staticmethod
    def assert_status_204(response):
        """Assert response status is 204"""
        assert response.status_code == 204, \
            f"Expected 204, got {response.status_code}: {response.text}"
    
    @staticmethod
    def assert_has_property(obj, prop):
        """Assert object has property"""
        assert prop in obj, f"Missing property '{prop}' in response"
    
    @staticmethod
    def assert_is_array(obj):
        """Assert object is an array"""
        assert isinstance(obj, list), "Response is not an array"
    
    @staticmethod
    def assert_response_time(response, max_ms=1000):
        """Assert response time is within threshold"""
        elapsed_ms = response.elapsed.total_seconds() * 1000
        assert elapsed_ms < max_ms, \
            f"Response took {elapsed_ms}ms, expected < {max_ms}ms"


@pytest.fixture
def assert_response():
    """Provide assertion helpers"""
    return ResponseAssertions()


# ─────────────────────────────────────────────
# Setup and Teardown
# ─────────────────────────────────────────────

@pytest.fixture(scope="session", autouse=True)
def setup_test_session():
    """Setup test session - runs once at the beginning"""
    print("\n" + "="*60)
    print("TEST SESSION STARTED")
    print(f"API Base URL: {BASE_URL}")
    print(f"Test User: {TEST_USER_EMAIL}")
    print("="*60)
    
    yield
    
    print("\n" + "="*60)
    print("TEST SESSION COMPLETED")
    print("="*60)
