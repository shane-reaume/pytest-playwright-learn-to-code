"""
Python Advanced Concepts Learning Module

This module covers advanced Python features through practical test examples:
- Concurrency
  * Threading basics
  * Multiprocessing
  * asyncio and coroutines
  * Concurrent.futures
- Comprehensions
  * List comprehensions
  * Set comprehensions
  * Dictionary comprehensions
  * Nested comprehensions
- Type Hints
  * Basic type annotations
  * Generic types
  * Type aliases
  * Optional and Union types
  * Protocol classes
- Advanced Functions
  * Partial functions
  * Closures
  * Decorators with state
  * Function attributes
- Memory Management
  * Garbage collection
  * Weak references
  * Memory profiling
  * Object lifecycle
- Performance Optimization
  * Profiling code
  * Caching and memoization
  * C extensions basics
  * Performance patterns

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time
import threading
import multiprocessing
import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import TypeVar, Generic, Optional, Union, Protocol
from functools import partial, lru_cache
import weakref
import gc

def get_concurrency_examples():
    return '''
        # Threading example
        def worker(name):
            for i in range(3):
                print(f"{name}: {i}")
                time.sleep(0.1)

        threads = [
            threading.Thread(target=worker, args=(f"Thread-{i}",))
            for i in range(2)
        ]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        # Multiprocessing example
        def process_worker(name):
            print(f"Process {name}: {multiprocessing.current_process().pid}")

        with multiprocessing.Pool(2) as pool:
            pool.map(process_worker, ["A", "B"])

        # Async/await example
        async def async_task(name):
            print(f"Start {name}")
            await asyncio.sleep(0.1)
            print(f"End {name}")
            return f"{name} done"

        async def main():
            tasks = [async_task(f"Task-{i}") for i in range(2)]
            results = await asyncio.gather(*tasks)
            print(results)

        # Run in asyncio event loop
        # asyncio.run(main())
    '''

def get_comprehension_examples():
    return '''
        # List comprehension
        numbers = [1, 2, 3, 4, 5]
        squares = [x * x for x in numbers if x % 2 == 0]
        print(squares)  # [4, 16]

        # Set comprehension
        chars = {c.lower() for c in "Hello World"}
        print(chars)  # {'h', 'e', 'l', 'o', 'w', 'r', 'd', ' '}

        # Dictionary comprehension
        word = "hello"
        char_positions = {char: idx for idx, char in enumerate(word)}
        print(char_positions)  # {'h': 0, 'e': 1, 'l': 2, 'o': 4}

        # Nested comprehension
        matrix = [[1, 2, 3], [4, 5, 6]]
        transposed = [[row[i] for row in matrix] for i in range(3)]
        print(transposed)  # [[1, 4], [2, 5], [3, 6]]
    '''

def get_type_hints_examples():
    return '''
        from typing import TypeVar, Generic, Optional, Union, Protocol

        # Basic type hints
        def greet(name: str) -> str:
            return f"Hello, {name}!"

        # Generic types
        T = TypeVar('T')
        class Stack(Generic[T]):
            def __init__(self) -> None:
                self.items: list[T] = []
            
            def push(self, item: T) -> None:
                self.items.append(item)
            
            def pop(self) -> Optional[T]:
                return self.items.pop() if self.items else None

        # Protocol class (structural subtyping)
        class Drawable(Protocol):
            def draw(self) -> None: ...

        class Circle:
            def draw(self) -> None:
                print("Drawing circle")

        def render(shape: Drawable) -> None:
            shape.draw()

        # Union types and type aliases
        Number = Union[int, float]
        def process_number(n: Number) -> Number:
            return n * 2
    '''

def get_advanced_functions():
    return '''
        from functools import partial, lru_cache

        # Partial functions
        def power(base, exponent):
            return base ** exponent

        square = partial(power, exponent=2)
        cube = partial(power, exponent=3)
        print(square(4))  # 16
        print(cube(4))    # 64

        # Closures
        def counter_factory(start=0):
            count = start
            def increment():
                nonlocal count
                count += 1
                return count
            return increment

        counter = counter_factory(10)
        print(counter())  # 11
        print(counter())  # 12

        # Decorator with state
        def count_calls(func):
            func.calls = 0
            def wrapper(*args, **kwargs):
                func.calls += 1
                return func(*args, **kwargs)
            return wrapper

        @count_calls
        def hello():
            return "Hello!"

        print(hello())        # "Hello!"
        print(hello.calls)    # 1
    '''

def get_memory_management():
    return '''
        import gc
        import weakref

        # Reference counting
        class Example:
            def __init__(self, name):
                self.name = name
            def __del__(self):
                print(f"{self.name} is being deleted")

        # Weak references
        class Cache:
            def __init__(self):
                self._cache = weakref.WeakKeyDictionary()
            
            def get_data(self, key, default=None):
                return self._cache.get(key, default)
            
            def set_data(self, key, value):
                self._cache[key] = value

        # Garbage collection
        gc.collect()  # Force garbage collection
        print(gc.get_count())  # Get collection counts
        
        # Object lifecycle
        obj = Example("test")
        ref = weakref.ref(obj)
        print(ref())  # Prints the object
        del obj
        print(ref())  # Prints None
    '''

def get_performance_optimization():
    return '''
        from functools import lru_cache
        import time

        # Memoization with lru_cache
        @lru_cache(maxsize=None)
        def fibonacci(n):
            if n < 2:
                return n
            return fibonacci(n-1) + fibonacci(n-2)

        # Time measurement
        def measure_time(func):
            def wrapper(*args, **kwargs):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                print(f"{func.__name__} took {end - start:.2f} seconds")
                return result
            return wrapper

        @measure_time
        def slow_function():
            time.sleep(1)
            return "Done"

        # Generator-based iteration
        def process_large_data():
            for i in range(1000000):
                yield i * i

        # Using next() with default
        iterator = process_large_data()
        first = next(iterator, None)
    '''

def get_key_takeaways():
    return '''
        # 1. Concurrency
        threading.Thread(target=func)  # Threads
        multiprocessing.Pool()         # Processes
        async/await                    # Coroutines

        # 2. Type Hints
        def func(x: int) -> str: ...  # Type annotations
        Optional[Type]                 # Maybe None
        Union[Type1, Type2]           # Multiple types

        # 3. Memory Management
        weakref.ref(obj)              # Weak references
        gc.collect()                  # Manual collection

        # 4. Performance
        @lru_cache                    # Memoization
        generator vs list             # Memory efficiency
    '''

@describe("Interactive Python Advanced Concepts")
class TestPythonAdvancedConceptsInteractive:
    
    @it("teaches about concurrency")
    def test_concurrency(self):
        print_section_header("Welcome to Advanced Concepts - Part 1: Concurrency")
        print_info("Let's explore Python's concurrency options.")
        time.sleep(1)

        # Question 1: Threading vs Multiprocessing
        print_subsection_header("Question 1: Concurrency Models")
        print_instruction("Look at these concurrency examples:")
        print_code_block(get_concurrency_examples())
        answer = get_user_input("What Python feature is best for I/O-bound tasks?")
        check_answer(
            answer,
            ['threading', 'threads', 'threading module'],
            "Threading is best for I/O-bound tasks because of the Global Interpreter Lock (GIL)."
        )

    @it("teaches about comprehensions")
    def test_comprehensions(self):
        print_section_header("Part 2: Comprehensions")
        print_info("Let's learn about Python's comprehension syntax.")
        time.sleep(1)

        # Question 1: Comprehension Types
        print_subsection_header("Question 1: Comprehension Types")
        print_instruction("Look at these comprehension examples:")
        print_code_block(get_comprehension_examples())
        answer = get_user_input("What type of brackets are used for dictionary comprehensions?")
        check_answer(
            answer,
            ['curly', 'curly brackets', '{}', 'braces'],
            "Dictionary comprehensions use curly brackets {} with key:value pairs."
        )

    @it("teaches about type hints")
    def test_type_hints(self):
        print_section_header("Part 3: Type Hints")
        print_info("Let's explore Python's type hinting system.")
        time.sleep(1)

        # Question 1: Type Annotations
        print_subsection_header("Question 1: Type Annotations")
        print_instruction("Look at these type hint examples:")
        print_code_block(get_type_hints_examples())
        answer = get_user_input("What type hint indicates a value that might be None?")
        check_answer(
            answer,
            ['Optional', 'Optional[]', 'typing.Optional'],
            "Optional[T] indicates that a value might be of type T or None."
        )

    @it("teaches about advanced functions")
    def test_advanced_functions(self):
        print_section_header("Part 4: Advanced Functions")
        print_info("Let's learn about advanced function features.")
        time.sleep(1)

        # Question 1: Partial Functions
        print_subsection_header("Question 1: Partial Functions")
        print_instruction("Look at these advanced function examples:")
        print_code_block(get_advanced_functions())
        answer = get_user_input("What function creates a new function with pre-filled arguments?")
        check_answer(
            answer,
            ['partial', 'partial()', 'functools.partial'],
            "partial() from functools creates a new function with some arguments pre-filled."
        )

    @it("teaches about memory management")
    def test_memory_management(self):
        print_section_header("Part 5: Memory Management")
        print_info("Let's explore Python's memory management.")
        time.sleep(1)

        # Question 1: Weak References
        print_subsection_header("Question 1: Weak References")
        print_instruction("Look at these memory management examples:")
        print_code_block(get_memory_management())
        answer = get_user_input("What type of reference doesn't prevent garbage collection?")
        check_answer(
            answer,
            ['weak', 'weak reference', 'weakref'],
            "Weak references don't prevent an object from being garbage collected."
        )

    @it("teaches about performance optimization")
    def test_performance(self):
        print_section_header("Part 6: Performance Optimization")
        print_info("Let's learn about performance optimization techniques.")
        time.sleep(1)

        # Question 1: Caching
        print_subsection_header("Question 1: Caching")
        print_instruction("Look at these performance optimization examples:")
        print_code_block(get_performance_optimization())
        answer = get_user_input("What decorator implements function result caching?")
        check_answer(
            answer,
            ['@lru_cache', 'lru_cache', '@functools.lru_cache'],
            "@lru_cache implements Least Recently Used caching for function results."
        )

        print_success("🎉 Congratulations! You've completed the Advanced Python Concepts lesson!")
        print_info("Key takeaways:")
        print_code_block(get_key_takeaways()) 