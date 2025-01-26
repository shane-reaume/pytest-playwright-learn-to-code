"""
Pytest Basics Learning Module

This module covers pytest fundamentals through practical test examples:
- Basic Testing Concepts
  * Test functions
  * Test classes
  * Assertions
  * Test discovery
- Fixtures
  * Basic fixtures
  * Fixture scope
  * Fixture factories
  * Parametrized fixtures
- Markers
  * Built-in markers
  * Custom markers
  * Skip and xfail
  * Parametrize
- Test Organization
  * Test files
  * Test classes
  * Test packages
  * conftest.py
- Advanced Features
  * Capture of stdout/stderr
  * Temporary directories
  * Monkey patching
  * Plugin system basics
- Best Practices
  * Test naming
  * Test isolation
  * Test coverage
  * Test documentation

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time
import pytest

def get_basic_test_examples():
    return '''
        # Basic test function
        def test_addition():
            result = 1 + 1
            assert result == 2
            assert result > 0
            assert isinstance(result, int)

        # Test class
        class TestCalculator:
            def test_multiplication(self):
                assert 2 * 3 == 6
            
            def test_division(self):
                assert 6 / 2 == 3
                with pytest.raises(ZeroDivisionError):
                    1 / 0

        # Using our describe/it pattern (from this project)
        @describe("Calculator functionality")
        class TestCalculatorBDD:
            @it("multiplies two numbers")
            def test_multiplication(self):
                assert 2 * 3 == 6
            
            @it("divides two numbers")
            def test_division(self):
                assert 6 / 2 == 3
    '''

def get_fixture_examples():
    return '''
        import pytest
        from typing import List

        # Basic fixture
        @pytest.fixture
        def numbers() -> List[int]:
            return [1, 2, 3, 4, 5]

        def test_sum(numbers):
            assert sum(numbers) == 15

        # Fixture with scope
        @pytest.fixture(scope="module")
        def database_connection():
            print("Connecting to database...")
            yield "connection"
            print("Closing database connection...")

        # Fixture factory
        @pytest.fixture
        def make_user():
            def _make_user(name: str, age: int = 30):
                return {"name": name, "age": age}
            return _make_user

        def test_user_factory(make_user):
            user = make_user("Alice", 25)
            assert user["name"] == "Alice"
            assert user["age"] == 25

        # Parametrized fixture
        @pytest.fixture(params=[1, 2, 3])
        def test_data(request):
            return request.param

        def test_multiplication(test_data):
            result = test_data * 2
            assert result == test_data + test_data
    '''

def get_marker_examples():
    return '''
        import pytest
        import sys

        # Skip marker
        @pytest.mark.skip(reason="Not implemented yet")
        def test_future_feature():
            # This test will be skipped
            assert False

        # Conditional skip
        @pytest.mark.skipif(sys.version_info < (3, 9),
                          reason="Requires Python 3.9+")
        def test_new_feature():
            assert True

        # Expected failure
        @pytest.mark.xfail(reason="Known bug #123")
        def test_known_bug():
            assert 1/0 == 1  # This will fail but won't fail the test run

        # Custom marker
        pytest.mark.integration = pytest.mark.mark("integration")

        @pytest.mark.integration
        def test_database_integration():
            # This test will only run when integration tests are requested
            assert True

        # Parametrize
        @pytest.mark.parametrize("input,expected", [
            (2, 4),
            (3, 9),
            (4, 16),
        ])
        def test_square(input, expected):
            assert input * input == expected
    '''

def get_organization_examples():
    return '''
        # test_module.py
        """
        Tests should be in files starting with test_
        Classes should start with Test
        Functions/methods should start with test_
        """

        # Directory structure example
        """
        tests/
        ├── conftest.py          # Shared fixtures
        ├── unit/
        │   ├── test_models.py
        │   └── test_utils.py
        ├── integration/
        │   └── test_api.py
        └── e2e/
            └── test_workflow.py
        """

        # conftest.py example (like our project uses)
        """
        import pytest

        @pytest.fixture(scope="session")
        def interactive_theme():
            # Our theme selection fixture
            theme = "monokai"  # Default theme
            yield theme

        def describe(description):
            # Our test organization decorator
            def decorator(cls):
                cls.description = description
                return cls
            return decorator

        def it(behavior):
            # Our test behavior decorator
            def decorator(func):
                func.behavior = behavior
                return func
            return decorator
        """
    '''

def get_advanced_features():
    return '''
        import pytest
        import os
        from unittest.mock import patch

        # Capturing output
        def test_print_capture(capsys):
            print("Hello")
            captured = capsys.readouterr()
            assert captured.out == "Hello\\n"

        # Temporary directory
        def test_file_handling(tmp_path):
            data_file = tmp_path / "test.txt"
            data_file.write_text("Hello")
            assert data_file.read_text() == "Hello"

        # Monkey patching
        def test_environment(monkeypatch):
            monkeypatch.setenv("API_KEY", "secret")
            assert os.environ["API_KEY"] == "secret"

        # Using unittest.mock
        def get_data():
            return {"status": "success"}

        def test_mock_function():
            with patch("module.get_data") as mock_get:
                mock_get.return_value = {"status": "error"}
                result = get_data()
                assert result["status"] == "error"
    '''

def get_best_practices():
    return '''
        # Test naming
        def test_should_add_two_numbers():
            assert 1 + 1 == 2

        # Test isolation
        @pytest.fixture(autouse=True)
        def clean_environment():
            # Setup
            original_env = dict(os.environ)
            yield
            # Teardown
            os.environ.clear()
            os.environ.update(original_env)

        # Test coverage example
        """
        # Run tests with coverage
        pytest --cov=myproject tests/
        
        # Generate HTML report
        pytest --cov=myproject --cov-report=html tests/
        """

        # Test documentation
        def test_user_registration():
            """
            Test user registration process.
            
            Steps:
            1. Create user data
            2. Call registration endpoint
            3. Verify user is created
            4. Check welcome email is sent
            
            Expected:
            - User should be created in database
            - Welcome email should be sent
            - Return 201 status code
            """
            assert True  # Actual test implementation
    '''

def get_key_takeaways():
    return '''
        # 1. Basic Structure
        def test_something():        # Test function
        class TestSomething:        # Test class
        assert expression          # Assertion

        # 2. Fixtures
        @pytest.fixture            # Define fixture
        @pytest.fixture(scope="")  # Set scope
        def fixture(request):      # Access request

        # 3. Markers
        @pytest.mark.skip          # Skip test
        @pytest.mark.parametrize   # Multiple inputs
        @pytest.mark.custom       # Custom markers

        # 4. Organization
        tests/                    # Test root
        conftest.py              # Shared fixtures
        test_*.py               # Test files
    '''

@describe("Interactive Pytest Basics")
class TestPytestBasicsInteractive:
    
    @it("teaches about basic testing concepts")
    def test_basics(self):
        print_section_header("Welcome to Pytest Basics - Part 1: Basic Testing")
        print_info("Let's explore pytest's fundamental concepts.")
        time.sleep(1)

        # Question 1: Basic Testing
        print_subsection_header("Question 1: Test Structure")
        print_instruction("Look at these basic test examples:")
        print_code_block(get_basic_test_examples())
        answer = get_user_input("What assertion statement is used to verify exceptions?")
        check_answer(
            answer,
            ['pytest.raises', 'raises', 'with pytest.raises'],
            "pytest.raises() is used to verify that code raises an expected exception."
        )

    @it("teaches about fixtures")
    def test_fixtures(self):
        print_section_header("Part 2: Fixtures")
        print_info("Let's learn about pytest fixtures.")
        time.sleep(1)

        # Question 1: Fixture Scopes
        print_subsection_header("Question 1: Fixture Scopes")
        print_instruction("Look at these fixture examples:")
        print_code_block(get_fixture_examples())
        answer = get_user_input("What fixture scope is used for setup/teardown that should run once for an entire test module?")
        check_answer(
            answer,
            ['module', 'module scope'],
            "The 'module' scope runs a fixture once per test module."
        )

    @it("teaches about markers")
    def test_markers(self):
        print_section_header("Part 3: Markers")
        print_info("Let's explore pytest markers.")
        time.sleep(1)

        # Question 1: Built-in Markers
        print_subsection_header("Question 1: Skip and Xfail")
        print_instruction("Look at these marker examples:")
        print_code_block(get_marker_examples())
        answer = get_user_input("What marker is used to mark a test as expected to fail?")
        check_answer(
            answer,
            ['xfail', '@pytest.mark.xfail'],
            "The @pytest.mark.xfail marker indicates that a test is expected to fail."
        )

    @it("teaches about test organization")
    def test_organization(self):
        print_section_header("Part 4: Test Organization")
        print_info("Let's learn about organizing pytest tests.")
        time.sleep(1)

        # Question 1: Test Discovery
        print_subsection_header("Question 1: Test Discovery")
        print_instruction("Look at these organization examples:")
        print_code_block(get_organization_examples())
        answer = get_user_input("What prefix should test files have to be discovered by pytest?")
        check_answer(
            answer,
            ['test_', 'test'],
            "Test files should start with 'test_' to be discovered by pytest."
        )

    @it("teaches about advanced features")
    def test_advanced(self):
        print_section_header("Part 5: Advanced Features")
        print_info("Let's explore pytest's advanced features.")
        time.sleep(1)

        # Question 1: Output Capture
        print_subsection_header("Question 1: Output Capture")
        print_instruction("Look at these advanced feature examples:")
        print_code_block(get_advanced_features())
        answer = get_user_input("What fixture is used to capture stdout and stderr in tests?")
        check_answer(
            answer,
            ['capsys', 'capsys fixture'],
            "The capsys fixture is used to capture stdout and stderr output in tests."
        )

    @it("teaches about best practices")
    def test_best_practices(self):
        print_section_header("Part 6: Best Practices")
        print_info("Let's learn about pytest best practices.")
        time.sleep(1)

        # Question 1: Test Isolation
        print_subsection_header("Question 1: Test Isolation")
        print_instruction("Look at these best practice examples:")
        print_code_block(get_best_practices())
        answer = get_user_input("What command-line option is used to measure test coverage?")
        check_answer(
            answer,
            ['--cov', '--cov=', 'pytest --cov'],
            "The --cov option is used to measure test coverage when running pytest."
        )

        print_success("🎉 Congratulations! You've completed the Pytest Basics lesson!")
        print_info("Key takeaways:")
        print_code_block(get_key_takeaways()) 