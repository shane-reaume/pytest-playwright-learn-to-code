"""
Python Iterators and Generators Learning Module

This module covers Python's iteration protocols through practical test examples:
- Iterators
  * Iterator protocol (__iter__ and __next__)
  * Creating custom iterators
  * StopIteration exception
  * Infinite iterators
- Generators
  * Generator functions with yield
  * Generator expressions
  * yield from statement
  * send() and close() methods
- Generator Patterns
  * Pipeline generators
  * Coroutines
  * Sub-generators
- Memory Efficiency
  * Lazy evaluation
  * Memory usage comparison
  * Use cases for generators
- Built-in Iteration Tools
  * iter() and next()
  * enumerate()
  * zip() and itertools.zip_longest()
  * itertools module functions

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time

def get_iterator_basics():
    return '''
        # Custom Iterator Class
        class CountUp:
            def __init__(self, start, end):
                self.current = start
                self.end = end
                
            def __iter__(self):
                return self
                
            def __next__(self):
                if self.current > self.end:
                    raise StopIteration
                value = self.current
                self.current += 1
                return value

        # Using the iterator
        counter = CountUp(1, 3)
        for num in counter:
            print(num)  # Prints: 1, 2, 3

        # Manual iteration
        nums = iter([1, 2, 3])
        print(next(nums))  # 1
        print(next(nums))  # 2
        print(next(nums))  # 3
        # next(nums)  # Raises StopIteration
    '''

def get_generator_basics():
    return '''
        # Generator function
        def count_up(start, end):
            current = start
            while current <= end:
                yield current
                current += 1

        # Using the generator
        for num in count_up(1, 3):
            print(num)  # Prints: 1, 2, 3

        # Generator expression
        squares = (x * x for x in range(5))
        print(list(squares))  # [0, 1, 4, 9, 16]

        # yield from example
        def combined_gen():
            yield from range(3)     # 0, 1, 2
            yield from "ABC"        # 'A', 'B', 'C'
            yield from [7, 8, 9]    # 7, 8, 9

        print(list(combined_gen()))  # [0, 1, 2, 'A', 'B', 'C', 7, 8, 9]
    '''

def get_generator_patterns():
    return '''
        # Pipeline pattern
        def generate_numbers():
            for i in range(1, 4):
                yield i

        def square_numbers(numbers):
            for num in numbers:
                yield num * num

        def filter_even(numbers):
            for num in numbers:
                if num % 2 == 0:
                    yield num

        # Composing the pipeline
        numbers = generate_numbers()
        squared = square_numbers(numbers)
        even = filter_even(squared)
        print(list(even))  # [4]

        # Coroutine pattern
        def averager():
            total = 0
            count = 0
            average = None
            while True:
                value = yield average
                if value is None:
                    break
                total += value
                count += 1
                average = total / count

        # Using the coroutine
        avg = averager()
        next(avg)  # Prime the coroutine
        print(avg.send(10))  # 10.0
        print(avg.send(20))  # 15.0
        print(avg.send(30))  # 20.0
    '''

def get_memory_efficiency():
    return '''
        # Memory comparison
        # List comprehension (eager)
        squares_list = [x * x for x in range(1000000)]
        
        # Generator expression (lazy)
        squares_gen = (x * x for x in range(1000000))

        # Memory-efficient file reading
        def read_lines(file_path):
            with open(file_path) as f:
                for line in f:
                    yield line.strip()

        # Infinite sequence generator
        def fibonacci():
            a, b = 0, 1
            while True:
                yield a
                a, b = b, a + b

        # Taking first 5 Fibonacci numbers
        fib = fibonacci()
        for _ in range(5):
            print(next(fib))  # 0, 1, 1, 2, 3
    '''

def get_iteration_tools():
    return '''
        import itertools

        # enumerate example
        for i, char in enumerate("ABC"):
            print(f"{i}: {char}")  # "0: A", "1: B", "2: C"

        # zip and zip_longest
        names = ["Alice", "Bob"]
        ages = [25, 30, 35]
        for name, age in itertools.zip_longest(names, ages, fillvalue="Unknown"):
            print(f"{name}: {age}")

        # itertools functions
        # Count from 1, stepping by 2
        odds = itertools.count(1, 2)
        print(list(itertools.islice(odds, 3)))  # [1, 3, 5]

        # Cycle through items
        colors = itertools.cycle(["Red", "Green", "Blue"])
        print([next(colors) for _ in range(4)])  # ["Red", "Green", "Blue", "Red"]

        # Combinations and permutations
        print(list(itertools.combinations("ABC", 2)))  # [("A","B"), ("A","C"), ("B","C")]
        print(list(itertools.permutations("ABC", 2)))  # [("A","B"), ("A","C"), ("B","A"), ...]
    '''

def get_key_takeaways():
    return '''
        # 1. Iterator Protocol
        class MyIterator:
            def __iter__(self):
                return self
            def __next__(self):
                # Return next item or raise StopIteration

        # 2. Generator Functions
        def my_generator():
            yield item  # Pause here and return item
            yield from other_generator()  # Delegate to other generator

        # 3. Generator Expressions
        squares = (x*x for x in range(10))  # Memory efficient

        # 4. Built-in Tools
        enumerate(items)  # Index and item pairs
        zip(list1, list2)  # Parallel iteration
        itertools.count()  # Infinite sequences
    '''

@describe("Interactive Python Iterators and Generators")
class TestPythonIteratorsGeneratorsInteractive:
    
    @it("teaches about iterator basics")
    def test_iterator_basics(self):
        print_section_header("Welcome to Iterators and Generators - Part 1: Iterators")
        print_info("Let's explore Python's iterator protocol.")
        time.sleep(1)

        # Question 1: Iterator Protocol
        print_subsection_header("Question 1: Iterator Protocol")
        print_instruction("Look at this custom iterator example:")
        print_code_block(get_iterator_basics())
        answer = get_user_input("What are the two special methods required to make a class iterable?")
        check_answer(
            answer,
            ['__iter__ and __next__', '__iter__, __next__', '__iter__ __next__'],
            "The __iter__ and __next__ methods implement the iterator protocol."
        )

        # Question 2: StopIteration
        print_subsection_header("Question 2: StopIteration")
        answer = get_user_input("What exception is raised when an iterator is exhausted?")
        check_answer(
            answer,
            ['StopIteration', 'StopIteration exception'],
            "StopIteration is raised when there are no more items to iterate over."
        )

    @it("teaches about generators")
    def test_generators(self):
        print_section_header("Part 2: Generators")
        print_info("Let's learn about generator functions and expressions.")
        time.sleep(1)

        # Question 1: Generator Functions
        print_subsection_header("Question 1: Generator Functions")
        print_instruction("Look at these generator examples:")
        print_code_block(get_generator_basics())
        answer = get_user_input("What keyword is used to create a generator function?")
        check_answer(
            answer,
            ['yield', 'yield keyword'],
            "The yield keyword creates a generator function that can pause and resume execution."
        )

        # Question 2: Generator Delegation
        print_subsection_header("Question 2: Generator Delegation")
        answer = get_user_input("What syntax is used to delegate to another generator?")
        check_answer(
            answer,
            ['yield from', 'yield from generator'],
            "yield from delegates to another generator, yielding each of its values."
        )

    @it("teaches about generator patterns")
    def test_generator_patterns(self):
        print_section_header("Part 3: Generator Patterns")
        print_info("Let's explore common generator patterns and coroutines.")
        time.sleep(1)

        # Question 1: Pipeline Pattern
        print_subsection_header("Question 1: Pipeline Pattern")
        print_instruction("Look at these generator patterns:")
        print_code_block(get_generator_patterns())
        answer = get_user_input("What method is used to send values into a coroutine?")
        check_answer(
            answer,
            ['send', 'send()', 'send method'],
            "The send() method allows you to send values into a coroutine generator."
        )

    @it("teaches about memory efficiency")
    def test_memory_efficiency(self):
        print_section_header("Part 4: Memory Efficiency")
        print_info("Let's learn about lazy evaluation and memory usage.")
        time.sleep(1)

        # Question 1: Lazy Evaluation
        print_subsection_header("Question 1: Lazy Evaluation")
        print_instruction("Look at these memory efficiency examples:")
        print_code_block(get_memory_efficiency())
        answer = get_user_input("What syntax creates a generator expression?")
        check_answer(
            answer,
            ['parentheses', '()', 'round brackets'],
            "Generator expressions use parentheses () instead of square brackets []."
        )

    @it("teaches about iteration tools")
    def test_iteration_tools(self):
        print_section_header("Part 5: Built-in Iteration Tools")
        print_info("Let's explore Python's built-in iteration tools.")
        time.sleep(1)

        # Question 1: Built-in Functions
        print_subsection_header("Question 1: Built-in Functions")
        print_instruction("Look at these iteration tools:")
        print_code_block(get_iteration_tools())
        answer = get_user_input("What function creates pairs of indexes and values from an iterable?")
        check_answer(
            answer,
            ['enumerate', 'enumerate()', 'enumerate function'],
            "The enumerate() function creates pairs of indexes and values from an iterable."
        )

        print_success("🎉 Congratulations! You've completed the Iterators and Generators lesson!")
        print_info("Key takeaways:")
        print_code_block(get_key_takeaways()) 