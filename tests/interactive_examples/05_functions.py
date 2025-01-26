"""
Python Functions Learning Module

This module covers Python's function concepts through practical examples:
- Function Basics
  * Function definition and calls
  * Parameters and arguments
  * Return values
  * Default arguments
- Advanced Function Features
  * *args and **kwargs
  * Lambda functions
  * Function annotations
  * Docstrings
- Scope and Closures
  * Local vs global scope
  * Nonlocal variables
  * Closures and factories
- Functional Programming
  * map, filter, reduce
  * Decorators
  * Higher-order functions

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time

@describe("Interactive Python Functions")
class TestPythonFunctionsInteractive:
    
    @it("teaches about function basics")
    def test_function_basics(self):
        print_section_header("Welcome to Python Functions - Part 1: Function Basics")
        print_info("Let's learn about Python functions in detail.")
        time.sleep(1)

        # Question 1: Function definition and calls
        print_subsection_header("Question 1: Function Definition")
        print_instruction("Look at these function definitions:")
        print_code_block("""
            # Basic function definition
            def greet(name):
                return f"Hello, {name}!"

            # Function with multiple parameters
            def calculate_total(items, tax_rate=0.1):
                subtotal = sum(items)
                tax = subtotal * tax_rate
                return subtotal + tax

            # Function with docstring
            def get_area(length, width):
                '''Calculate the area of a rectangle.
                
                Args:
                    length (float): The length of the rectangle
                    width (float): The width of the rectangle
                
                Returns:
                    float: The area of the rectangle
                '''
                return length * width
                         """)
        answer = get_user_input("What keyword is used to define a function in Python?")
        check_answer(
            answer,
            ['def', 'def keyword'],
            "The def keyword is used to define functions in Python. It's followed by the function name and parameters."
        )

        # Question 2: Parameters and arguments
        print_subsection_header("Question 2: Parameters and Arguments")
        print_instruction("Look at these parameter types:")
        print_code_block("""
            # Positional and keyword arguments
            def create_user(name, age, city="Unknown"):
                return {"name": name, "age": age, "city": city}

            # Different ways to call
            user1 = create_user("Alice", 30, "New York")  # Positional
            user2 = create_user(age=25, name="Bob")       # Keyword args
            user3 = create_user("Charlie", city="London", age=35)  # Mixed

            # Variable number of arguments
            def print_all(*args, **kwargs):
                print("Positional:", args)    # Tuple of positional args
                print("Keyword:", kwargs)     # Dict of keyword args

            print_all(1, 2, x=3, y=4)  # Positional: (1, 2), Keyword: {'x': 3, 'y': 4}
                         """)
        answer = get_user_input("What symbol is used to collect variable keyword arguments into a dictionary?")
        check_answer(
            answer,
            ['**', 'double asterisk', 'double star'],
            "The ** (double asterisk) collects keyword arguments into a dictionary. Single * collects positional args into a tuple."
        )

        # Question 3: Return values
        print_subsection_header("Question 3: Return Values")
        print_instruction("Look at these return value examples:")
        print_code_block("""
            # Multiple return values
            def get_stats(numbers):
                return min(numbers), max(numbers), sum(numbers)/len(numbers)

            # Unpacking return values
            minimum, maximum, average = get_stats([1, 2, 3, 4, 5])

            # Early returns
            def is_valid_username(username):
                if len(username) < 3:
                    return False
                if not username.isalnum():
                    return False
                return True

            # Default return value
            def greet_user(name):
                print(f"Hello, {name}")
                # No return statement = returns None
                         """)
        answer = get_user_input("What value is returned when a function has no return statement?")
        check_answer(
            answer,
            ['None', 'none'],
            "When a function has no return statement (or just 'return' with no value), it returns None by default."
        )

    @it("teaches about advanced function features")
    def test_advanced_functions(self):
        print_section_header("Part 2: Advanced Function Features")
        print_info("Let's explore some advanced function concepts in Python.")
        time.sleep(1)

        # Question 1: Lambda functions
        print_subsection_header("Question 1: Lambda Functions")
        print_instruction("Look at these lambda function examples:")
        print_code_block("""
            # Basic lambda function
            square = lambda x: x**2

            # Lambda with multiple arguments
            multiply = lambda x, y: x * y

            # Lambda in higher-order functions
            numbers = [1, 2, 3, 4, 5]
            squares = list(map(lambda x: x**2, numbers))
            evens = list(filter(lambda x: x % 2 == 0, numbers))

            # Lambda in sorting
            pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
            sorted_pairs = sorted(pairs, key=lambda pair: pair[1])  # Sort by string
                         """)
        answer = get_user_input("What keyword creates an anonymous function in Python?")
        check_answer(
            answer,
            ['lambda', 'lambda keyword'],
            "The lambda keyword creates anonymous functions. They're useful for short functions used as arguments."
        )

        # Question 2: Function annotations
        print_subsection_header("Question 2: Function Annotations")
        print_instruction("Look at these function annotation examples:")
        print_code_block("""
            # Type hints for parameters and return
            def calculate_bmi(weight: float, height: float) -> float:
                return weight / (height ** 2)

            # Complex type hints
            from typing import List, Dict, Optional

            def process_users(users: List[Dict[str, str]],
                            sort_key: Optional[str] = None) -> List[Dict[str, str]]:
                if sort_key:
                    return sorted(users, key=lambda u: u[sort_key])
                return users

            # Variable type annotations
            count: int = 0
            names: List[str] = []
            settings: Dict[str, bool] = {'debug': True}
                         """)
        answer = get_user_input("What character is used to specify a return type annotation?")
        check_answer(
            answer,
            ['->', 'arrow'],
            "The -> (arrow) specifies the return type annotation. It comes after the parameters and before the colon."
        )

        # Question 3: Decorators
        print_subsection_header("Question 3: Decorators")
        print_instruction("Look at these decorator examples:")
        print_code_block("""
            # Basic decorator
            def log_calls(func):
                def wrapper(*args, **kwargs):
                    print(f"Calling {func.__name__}")
                    result = func(*args, **kwargs)
                    print(f"Finished {func.__name__}")
                    return result
                return wrapper

            @log_calls
            def greet(name):
                return f"Hello, {name}!"

            # Decorator with arguments
            def repeat(times):
                def decorator(func):
                    def wrapper(*args, **kwargs):
                        for _ in range(times):
                            result = func(*args, **kwargs)
                        return result
                    return wrapper
                return decorator

            @repeat(times=3)
            def print_message(msg):
                print(msg)
                         """)
        answer = get_user_input("What symbol is used to apply a decorator to a function?")
        check_answer(
            answer,
            ['@', 'at sign', 'at symbol'],
            "The @ symbol (at sign) is used to apply decorators. It's a shorthand for function = decorator(function)."
        )

        print_success("🎉 Congratulations! You've completed the Python functions lesson!")
        print_info("Key takeaways:")
        print_code_block("""
            # 1. Function Basics
            def function_name(param1, param2="default"):
                '''Docstring for documentation'''
                return result

            # 2. Advanced Arguments
            def flexible_function(*args, **kwargs):
                # args is a tuple of positional arguments
                # kwargs is a dict of keyword arguments
                pass

            # 3. Lambda Functions
            lambda x: x**2  # Anonymous function

            # 4. Decorators
            @decorator
            def function():
                pass  # Function is wrapped by decorator
                         """) 