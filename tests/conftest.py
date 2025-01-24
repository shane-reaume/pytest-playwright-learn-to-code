import pytest
import sys
import time
from typing import Any

# Short-hand decorators for test organization
describe = pytest.mark.describe
it = pytest.mark.it
usefixture = pytest.mark.usefixtures

def learn_print(*args: Any, **kwargs: Any) -> None:
    """
    Custom print function for learning examples that ensures output is visible
    during test execution. This bypasses pytest's output capture.
    
    Args:
        *args: Variable length argument list, same as built-in print()
        **kwargs: Arbitrary keyword arguments, same as built-in print()
    """
    # Create a separator line for better visibility
    separator = "-" * 80
    
    # Get the sep and end parameters or use defaults
    sep = kwargs.pop('sep', ' ')
    end = kwargs.pop('end', ' ')
    
    # Print to stderr to bypass pytest capture
    print(file=sys.stderr)  # Add a blank line before output
    #print(separator, file=sys.stderr)
    print(*args, sep=sep, end=end, file=sys.stderr, flush=True, **kwargs)
    # print(separator, file=sys.stderr)
    print(file=sys.stderr)  # Add a blank line after output

# Alias for shorter name
lprint = learn_print

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