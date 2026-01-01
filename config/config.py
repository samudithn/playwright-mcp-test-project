"""Configuration settings for the test automation framework"""

# Browser settings
BROWSER_HEADLESS = False
BROWSER_VIEWPORT_WIDTH = 1280
BROWSER_VIEWPORT_HEIGHT = 720

# Timeouts (in milliseconds)
PAGE_LOAD_TIMEOUT = 30000
ELEMENT_WAIT_TIMEOUT = 10000

# URLs
BASE_URL = "https://www.saucedemo.com"

# Test data - SauceDemo standard users
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "wrong_password"
LOCKED_USERNAME = "locked_out_user"

# Screenshots
SCREENSHOT_DIR = "screenshots"

# Reports
REPORT_DIR = "reports"

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "logs/test_execution.log"
