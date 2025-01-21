# Pytest-Playwright Template

A template for setting up browser testing with Playwright in Python, using pytest as the test runner. This template provides a solid foundation for both UI testing and API testing projects.

## Features

- **Minimal Dependencies**: Only `pytest-playwright` which brings in all necessary packages
- **Ready-to-Use Test Structure**: Pre-configured with best practices and patterns
- **Custom Fixtures**: Examples of both per-test and per-class browser sessions
- **BDD-Style Tests**: Using `@describe` and `@it` decorators for readable tests

```python
from playwright.sync_api import Page
from conftest import describe, it

@describe("Feature or component being tested")
class TestSomething:
    @it("should perform specific action")
    def test_specific_action(self, page: Page):
        page.goto("https://shaneofalltrades.com")
        assert "Shane Of All Trades" in page.title()
```

- **Convenient CLI**: Simple command runner for various test scenarios
- **Example Tests**: Includes both unit tests and browser automation examples

## Using This Template

1. Click "Use this template" button on GitHub
2. Name your new repository
3. Clone your new repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_NEW_REPO.git
   cd YOUR_NEW_REPO
   ```

## Customization Steps

1. Update `conftest.py` with your own fixtures:
   - Modify the login URL and credentials
   - Add your own custom fixtures
   - Adjust browser configurations as needed

2. Modify `scripts.py` test commands:
   - Add your own test groupings
   - Customize command-line options
   - Add project-specific commands

3. Update `pytest.ini` if needed:
   - Add custom markers
   - Configure pytest options
   - Set up test discovery patterns

4. Replace example tests with your own:
   - Use `test_unit_only.py` as template for unit tests
   - Use `test_login_scope.py` as template for browser tests

## Setup Requirements

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation Steps

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install the required browsers:

   ```bash
   playwright install
   ```

## Project Structure

```
your-test-project/
├── tests/
│   ├── test_examples/          # Replace with your test categories
│   │   ├── test_unit_only.py  # Example of basic unit tests
│   │   └── test_login_scope.py # Example of browser tests
│   └── conftest.py            # Shared fixtures and configurations
├── scripts.py                 # Test runner script
├── pytest.ini                # Pytest configuration
└── requirements.txt         # Project dependencies
```

## Demo Setup

This template uses [Magento's demo site](https://magento.softwaretestingboard.com/) for example tests. To get started:

1. Create an account on the demo site:
   - Visit https://magento.softwaretestingboard.com/
   - Click "Create an Account"
   - Fill in your details and create your account
   - Save your login credentials

2. Set up your configuration:
   - Copy `config.example.py` to `config.py`
   - Update the TEST_USER dictionary with your demo site credentials:

   ```python
   TEST_USER = {
       "first_name": "Your_First_Name",
       "last_name": "Your_Last_Name",
       "email": "your_email@example.com",
       "password": "Your_Password123!"
   }
   ```

### Understanding Login Scopes

This template provides two login fixtures to demonstrate different testing approaches:

1. **Test-Level Login** (`luma_test_page`):
   - Creates a fresh login for each test
   - Ensures complete isolation between tests
   - Best for tests that modify user data or require a clean state
   - Example usage:

   ```python
   @it("should show user's account page")
   def test_account_page(self, luma_test_page):
       # Each test gets a fresh login
       page = luma_test_page
       assert "My Account" in page.title()
   ```

2. **Class-Level Login** (`luma_test_class_page`):
   - Shares one login across all tests in a class
   - More efficient for read-only operations
   - Best for test suites that just browse or verify content
   - Example usage:
 
   ```python
   @describe("Product browsing tests")
   class TestBrowsing:
       @it("should show product details")
       def test_product_details(self, luma_test_class_page):
           # Uses the same login across all tests in this class
           page = luma_test_class_page
           # Your test code here
   ```

Choose the appropriate fixture based on your test requirements:

- Use `luma_test_page` when tests modify data or require isolation
- Use `luma_test_class_page` for faster execution in read-only scenarios

## Running Tests

We provide a simple command-line interface through `scripts.py`:

### Basic Usage

```bash
python scripts.py run <test_name>
```

### Available Test Commands

- Run all tests:

  ```bash
  python scripts.py run all
  ```

- Run all tests in test_examples directory:

  ```bash
  python scripts.py run test_examples
  ```

- Run specific test files:

  ```bash
  python scripts.py run test_unit_only
  python scripts.py run login_scope
  ```

### Test Options

Add these flags to any test command:

- `--headed`: Run tests in headed mode (visible browser)

  ```bash
  python scripts.py run all --headed
  ```

- `--debug`: Run tests in debug mode (slower execution)

  ```bash
  python scripts.py run all --debug
  ```

### Help

To see all available commands and options:

```bash
python scripts.py help
```

## Writing Tests

Describe it! We use a BDD-style like syntax ( similar to Mocha or Jest) for better readability:

```python
@describe("Feature or component being tested")
class TestSomething:
    @it("should perform specific action")
    def test_specific_action(self, luma_test_page):
        # Your test code here
        pass
```

### Available Fixtures

- `luma_test_page`: Fresh login for each test
- `luma_test_class_page`: Single login shared across test class
- Add your own fixtures in `conftest.py`

## Best Practices

1. Keep tests independent and isolated
2. Use descriptive `@describe` and `@it` descriptions
3. Organize tests by feature or component
4. Utilize fixtures for common setup/teardown
5. Add comments for complex test scenarios

## Contributing

Contributions to improve this template are welcome! Please submit issues or pull requests to the template repository.

## License

This template is licensed under the MIT License - see the LICENSE file for details.

## Template Maintainers

- [Shane Reaume](https://github.com/shane-reaume) 