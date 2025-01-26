"""
Python Exception Handling Learning Module

This module covers Python's exception handling through practical test examples:
- Basic Exception Handling
  * try and except blocks
  * Multiple except blocks
  * The else clause
  * The finally clause
- Built-in Exceptions
  * Common exceptions (ValueError, TypeError, etc.)
  * Exception hierarchy
  * Exception properties
- Raising Exceptions
  * raise statement
  * Re-raising exceptions
  * raise from statement
- Custom Exceptions
  * Creating custom exception classes
  * Exception inheritance
  * Adding custom attributes
- Context Managers and Exceptions
  * with statement
  * Exception handling in context managers
- Best Practices
  * EAFP vs LBYL
  * Catching specific exceptions
  * Clean-up actions

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time

def get_basic_exceptions():
    return '''
        # Basic try-except
        try:
            number = int("not a number")
        except ValueError as e:
            print(f"Conversion error: {e}")

        # Multiple except clauses
        try:
            file = open("nonexistent.txt")
            data = file.read()
            number = int(data)
        except FileNotFoundError:
            print("File not found")
        except ValueError:
            print("Invalid number in file")
        except Exception as e:
            print(f"Unexpected error: {e}")

        # Exception hierarchy
        try:
            result = 1 / 0
        except ArithmeticError:
            print("Math operation failed")
        except Exception:
            print("Something else went wrong")
    '''

def get_advanced_handling():
    return '''
        # Try-except-else-finally
        try:
            x = int("123")
        except ValueError:
            print("Conversion failed")
        else:
            print("Conversion succeeded")
        finally:
            print("Always executed")

        # Context manager with error handling
        class DatabaseConnection:
            def __enter__(self):
                print("Connecting to database")
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                print("Closing connection")
                if exc_type is not None:
                    print(f"Error occurred: {exc_val}")
                return False  # Don't suppress exceptions

        with DatabaseConnection() as db:
            # Database operations here
            pass
    '''

def get_custom_exceptions():
    return '''
        class ValidationError(Exception):
            """Custom exception for data validation."""
            def __init__(self, message, field=None):
                self.message = message
                self.field = field
                super().__init__(self.message)

        class User:
            def __init__(self, username, email):
                self.username = username
                self.email = email
                
            def validate(self):
                if not self.username:
                    raise ValidationError("Username is required", "username")
                if "@" not in self.email:
                    raise ValidationError("Invalid email format", "email")

        # Using custom exception
        try:
            user = User("", "invalid-email")
            user.validate()
        except ValidationError as e:
            print(f"Validation failed for {e.field}: {e.message}")
    '''

def get_exception_chaining():
    return '''
        class DatabaseError(Exception):
            pass

        def get_user_from_db(user_id):
            try:
                # Simulate database query
                if not isinstance(user_id, int):
                    raise ValueError("User ID must be an integer")
                # Database operation failed
                raise ConnectionError("Database connection failed")
            except ValueError as e:
                raise DatabaseError("Invalid user lookup") from e
            except ConnectionError as e:
                raise DatabaseError("Database error") from e

        # Using exception chaining
        try:
            get_user_from_db("invalid-id")
        except DatabaseError as e:
            print(f"Error: {e}")
            if e.__cause__:
                print(f"Caused by: {e.__cause__}")
    '''

def get_key_takeaways():
    return '''
        # 1. Basic Exception Handling
        try:
            risky_operation()
        except SpecificError:
            handle_specific_case()
        except Exception as e:
            handle_general_case(e)

        # 2. Advanced Pattern
        try:
            operation()
        except Error:
            handle_error()
        else:
            handle_success()
        finally:
            cleanup()

        # 3. Custom Exceptions
        class CustomError(Exception):
            pass  # Define specific behavior
    '''

@describe("Interactive Python Error Handling")
class TestPythonErrorHandlingInteractive:
    
    @it("teaches about basic exception handling")
    def test_basic_exceptions(self):
        print_section_header("Welcome to Error Handling - Part 1: Basic Exceptions")
        print_info("Let's explore Python's exception handling system.")
        time.sleep(1)

        # Question 1: Basic try-except
        print_subsection_header("Question 1: Try-Except Blocks")
        print_instruction("Look at these exception handling examples:")
        print_code_block(get_basic_exceptions())
        answer = get_user_input("What keyword is used to capture the exception object in Python?")
        check_answer(
            answer,
            ['as', 'as keyword'],
            "The 'as' keyword is used to capture and name the exception object in an except clause."
        )

        # Question 2: Exception Types
        print_subsection_header("Question 2: Exception Types")
        answer = get_user_input("What is the base class for all built-in exceptions in Python?")
        check_answer(
            answer,
            ['Exception', 'Exception class'],
            "Exception is the base class for all built-in exceptions (except BaseException)."
        )

    @it("teaches about advanced error handling")
    def test_advanced_handling(self):
        print_section_header("Part 2: Advanced Error Handling")
        print_info("Let's learn about advanced exception handling patterns.")
        time.sleep(1)

        # Question 1: Try-except-else-finally
        print_subsection_header("Question 1: Complete Exception Handling")
        print_instruction("Look at this advanced error handling example:")
        print_code_block(get_advanced_handling())
        answer = get_user_input("Which block is executed when no exception occurs in the try block?")
        check_answer(
            answer,
            ['else', 'else block'],
            "The else block is executed when no exception occurs in the try block."
        )

        # Question 2: Context Managers
        print_subsection_header("Question 2: Context Managers")
        answer = get_user_input("What method is called when exiting a context manager (with block)?")
        check_answer(
            answer,
            ['__exit__', '__exit__ method'],
            "The __exit__ method is called when exiting a context manager, handling any exceptions that occurred."
        )

    @it("teaches about custom exceptions and chaining")
    def test_custom_exceptions(self):
        print_section_header("Part 3: Custom Exceptions and Chaining")
        print_info("Let's explore creating custom exceptions and exception chaining.")
        time.sleep(1)

        # Question 1: Custom Exceptions
        print_subsection_header("Question 1: Custom Exceptions")
        print_instruction("Look at this custom exception example:")
        print_code_block(get_custom_exceptions())
        answer = get_user_input("What should custom exception classes inherit from?")
        check_answer(
            answer,
            ['Exception', 'Exception class'],
            "Custom exception classes should inherit from Exception or its subclasses."
        )

        # Question 2: Exception Chaining
        print_subsection_header("Question 2: Exception Chaining")
        print_instruction("Look at this exception chaining example:")
        print_code_block(get_exception_chaining())
        answer = get_user_input("What keyword is used to chain exceptions in Python?")
        check_answer(
            answer,
            ['from', 'from keyword'],
            "The 'from' keyword is used to chain exceptions, preserving the original cause."
        )

        print_success("🎉 Congratulations! You've completed the Error Handling lesson!")
        print_info("Key takeaways:")
        print_code_block(get_key_takeaways()) 