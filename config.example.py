# Test Environment Configuration
BASE_URL = "https://magento.softwaretestingboard.com/"

# Test User Credentials
TEST_USER = {
    "first_name": "Test",
    "last_name": "User",
    "email": "test@example.com",
    "password": "YourPassword123!"
}

# Browser Configuration
BROWSER_CONFIG = {
    "slowMo": 0,  # Slow down execution by X milliseconds
    "headless": True,  # Set to False to see the browser UI
    "viewport": {
        "width": 1920,
        "height": 1080
    }
}

# Test Data
DEFAULT_TIMEOUT = 30000  # milliseconds
SCREENSHOT_DIR = "test-results/screenshots" 