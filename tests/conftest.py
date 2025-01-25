import pytest
import sys
import time
from typing import Any
from .utils import (
    color_print, get_user_input, select_theme, 
    BOLD, YELLOW, RESET, lprint
)

# Short-hand decorators for test organization
describe = pytest.mark.describe
it = pytest.mark.it
usefixture = pytest.mark.usefixtures

# Global flag to track if theme selection has been offered
_theme_selection_done = False

@pytest.fixture(scope="session", autouse=True)
def interactive_theme():
    """
    Session-wide fixture that handles theme selection for interactive tests.
    This runs once at the start of the test session.
    """
    global _theme_selection_done
    if not _theme_selection_done:
        color_print(f"\n{BOLD}=== Welcome to Interactive Python Learning ==={RESET}", YELLOW)
        color_print("Would you like to choose a syntax highlighting theme for code examples?")
        if get_user_input(f"{YELLOW}Choose theme? (yes/no): {RESET}").startswith('y'):
            select_theme()
        _theme_selection_done = True
    yield

@pytest.fixture
def luma_test_page(page):
    """
    Logs into Magento before each test function, and logs out after.
    This gives a fresh session per test.
    """
    page.goto("https://magento.softwaretestingboard.com/customer/account/login")
    page.fill("#email", "shane@shaneofalltrades.com")
    page.fill("#pass", "Valentine9115!")
    page.click("#send2")
    # Optionally wait for successful login (e.g., page.wait_for_selector("selector-after-login"))
    
    yield page
    
    # Optional: Log out or clean up
    page.goto("https://magento.softwaretestingboard.com/customer/account/logout/")

@pytest.fixture(scope="class")
def luma_test_class_page(request, browser_type_launch_args):
    """
    Logs into Magento once for the entire test class, reusing the same browser context.
    Good if you don't want to re-login in each test, but be aware that
    any state changes in one test can affect the others.
    """
    # Launch the browser with the arguments that pytest-playwright normally uses
    browser = request.getfixturevalue("browser_type").launch(**browser_type_launch_args)
    
    # Create a fresh context so multiple classes can run in parallel without clashing
    context = browser.new_context()
    page = context.new_page()

    # Perform login
    page.goto("https://magento.softwaretestingboard.com/customer/account/login")
    page.fill("#email", "shane@shaneofalltrades.com")
    page.fill("#pass", "Valentine9115!")
    page.click("#send2")
    # Optionally wait for successful login here as well
    
    yield page
    
    # Teardown once all tests in the class are done
    context.close()
    browser.close()