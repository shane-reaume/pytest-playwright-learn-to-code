"""
Python Decorators and Context Managers Learning Module

This module covers Python's decorators and context managers through practical test examples:
- Function Decorators
  * Basic decorator syntax
  * Decorators with arguments
  * Multiple decorators
  * functools.wraps
- Class Decorators
  * Decorating classes
  * Class factory patterns
  * Singleton pattern
- Context Managers
  * with statement
  * __enter__ and __exit__ methods
  * contextlib.contextmanager
  * Multiple context managers
- Built-in Context Managers
  * File handling
  * Lock management
  * Decimal contexts
- Custom Context Managers
  * Creating context managers
  * Error handling
  * Resource management
- Practical Applications
  * Timing code execution
  * Logging
  * Transaction management
  * Resource cleanup

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time
from functools import wraps
import contextlib
import threading

def get_basic_decorators():
    return '''
        # Basic function decorator
        def log_calls(func):
            @wraps(func)  # Preserves function metadata
            def wrapper(*args, **kwargs):
                print(f"Calling {func.__name__}")
                result = func(*args, **kwargs)
                print(f"Finished {func.__name__}")
                return result
            return wrapper

        @log_calls
        def greet(name):
            """Greet someone."""
            return f"Hello, {name}!"

        # Using the decorated function
        print(greet("Alice"))
        print(greet.__name__)    # 'greet' (preserved by wraps)
        print(greet.__doc__)     # Original docstring preserved
    '''

def get_decorator_arguments():
    return '''
        # Decorator with arguments
        def repeat(times):
            def decorator(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    results = []
                    for _ in range(times):
                        results.append(func(*args, **kwargs))
                    return results
                return wrapper
            return decorator

        @repeat(times=3)
        def say_hello():
            return "Hello!"

        # Multiple decorators
        @log_calls
        @repeat(times=2)
        def say_hi():
            return "Hi!"

        print(say_hello())  # ['Hello!', 'Hello!', 'Hello!']
        print(say_hi())     # Logs once, repeats twice
    '''

def get_class_decorators():
    return '''
        # Class decorator
        def singleton(cls):
            instances = {}
            def get_instance(*args, **kwargs):
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
                return instances[cls]
            return get_instance

        @singleton
        class Database:
            def __init__(self):
                self.connected = False
            
            def connect(self):
                if not self.connected:
                    print("Connecting to database...")
                    self.connected = True

        # Both variables reference the same instance
        db1 = Database()
        db2 = Database()
        print(db1 is db2)  # True
    '''

def get_context_managers():
    return '''
        # Basic context manager
        class Timer:
            def __enter__(self):
                self.start = time.time()
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                self.end = time.time()
                self.duration = self.end - self.start
                print(f"Time taken: {self.duration:.2f} seconds")
                return False  # Don't suppress exceptions

        # Using the context manager
        with Timer():
            time.sleep(1)  # Do something time-consuming

        # Context manager decorator
        @contextlib.contextmanager
        def temporary_attribute(obj, name, value):
            original = getattr(obj, name, None)
            setattr(obj, name, value)
            try:
                yield
            finally:
                if original is None:
                    delattr(obj, name)
                else:
                    setattr(obj, name, original)
    '''

def get_practical_examples():
    return '''
        # Resource management
        class DatabaseConnection:
            def __init__(self, host):
                self.host = host
                self.connected = False
            
            def __enter__(self):
                print(f"Connecting to {self.host}")
                self.connected = True
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                print("Closing connection")
                self.connected = False
                if exc_type is not None:
                    print(f"Error occurred: {exc_val}")
                return False

        # Thread-safe counter using context manager
        class Counter:
            def __init__(self):
                self.count = 0
                self._lock = threading.Lock()
            
            @contextlib.contextmanager
            def increment(self):
                with self._lock:
                    self.count += 1
                    yield self.count
                    if self.count > 100:
                        self.count = 0

        # Using multiple context managers
        with DatabaseConnection("localhost") as db, Timer() as timer:
            # Operations are timed and use the database connection
            time.sleep(0.5)
    '''

def get_key_takeaways():
    return '''
        # 1. Function Decorators
        @decorator
        def function():
            pass

        # 2. Decorator with Arguments
        @decorator(arg)
        def function():
            pass

        # 3. Context Manager Class
        class MyContext:
            def __enter__(self):
                # Setup
                return self
            def __exit__(self, exc_type, exc_val, exc_tb):
                # Cleanup
                return False  # Don't suppress exceptions

        # 4. Context Manager Decorator
        @contextmanager
        def my_context():
            # Setup
            yield
            # Cleanup
    '''

@describe("Interactive Python Decorators and Context Managers")
class TestPythonDecoratorsContextManagersInteractive:
    
    @it("teaches about basic decorators")
    def test_basic_decorators(self):
        print_section_header("Welcome to Decorators and Context Managers - Part 1: Basic Decorators")
        print_info("Let's explore Python's decorator syntax.")
        time.sleep(1)

        # Question 1: Basic Decorator
        print_subsection_header("Question 1: Basic Decorators")
        print_instruction("Look at this basic decorator example:")
        print_code_block(get_basic_decorators())
        answer = get_user_input("What decorator preserves a function's metadata (like __name__ and __doc__)?")
        check_answer(
            answer,
            ['@wraps', 'wraps', '@functools.wraps', 'functools.wraps'],
            "@wraps from functools preserves the decorated function's metadata."
        )

        # Question 2: Decorator Arguments
        print_subsection_header("Question 2: Decorator Arguments")
        print_instruction("Look at these decorator argument examples:")
        print_code_block(get_decorator_arguments())
        answer = get_user_input("How many levels of functions are needed for a decorator with arguments?")
        check_answer(
            answer,
            ['3', 'three'],
            "A decorator with arguments needs three levels: outer function (args), decorator, and wrapper."
        )

    @it("teaches about class decorators")
    def test_class_decorators(self):
        print_section_header("Part 2: Class Decorators")
        print_info("Let's learn about decorating classes.")
        time.sleep(1)

        # Question 1: Class Decorators
        print_subsection_header("Question 1: Class Decorators")
        print_instruction("Look at this class decorator example:")
        print_code_block(get_class_decorators())
        answer = get_user_input("What design pattern is implemented by the @singleton decorator?")
        check_answer(
            answer,
            ['singleton', 'singleton pattern'],
            "The singleton pattern ensures only one instance of a class exists."
        )

    @it("teaches about context managers")
    def test_context_managers(self):
        print_section_header("Part 3: Context Managers")
        print_info("Let's explore context managers and the with statement.")
        time.sleep(1)

        # Question 1: Context Manager Methods
        print_subsection_header("Question 1: Context Manager Protocol")
        print_instruction("Look at these context manager examples:")
        print_code_block(get_context_managers())
        answer = get_user_input("What are the two special methods required for a context manager class?")
        check_answer(
            answer,
            ['__enter__ and __exit__', '__enter__, __exit__', '__enter__ __exit__'],
            "The __enter__ and __exit__ methods define a context manager."
        )

        # Question 2: Context Manager Decorator
        print_subsection_header("Question 2: Context Manager Decorator")
        answer = get_user_input("What decorator can turn a generator function into a context manager?")
        check_answer(
            answer,
            ['@contextmanager', 'contextmanager'],
            "The @contextmanager decorator from contextlib turns a generator into a context manager."
        )

    @it("teaches about practical applications")
    def test_practical_applications(self):
        print_section_header("Part 4: Practical Applications")
        print_info("Let's see practical examples of decorators and context managers.")
        time.sleep(1)

        # Question 1: Resource Management
        print_subsection_header("Question 1: Resource Management")
        print_instruction("Look at these practical examples:")
        print_code_block(get_practical_examples())
        answer = get_user_input("What statement allows using multiple context managers in a single line?")
        check_answer(
            answer,
            ['with', 'with statement'],
            "The with statement can manage multiple context managers using commas."
        )

        print_success("🎉 Congratulations! You've completed the Decorators and Context Managers lesson!")
        print_info("Key takeaways:")
        print_code_block(get_key_takeaways()) 