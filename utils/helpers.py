"""Helper functions and utilities for test automation"""

import os
from datetime import datetime


def create_directory_if_not_exists(directory: str):
    """Create directory if it doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)


def take_screenshot_on_failure(page, test_name: str):
    """Take screenshot when test fails"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_dir = "screenshots"
    create_directory_if_not_exists(screenshot_dir)

    screenshot_path = f"{screenshot_dir}/{test_name}_failure_{timestamp}.png"
    page.screenshot(path=screenshot_path)
    return screenshot_path
