"""
Python Data Structures Learning Module

This module covers Python's core data structures through practical test examples:
- Lists and list operations
  * Creation and modification
  * Indexing and slicing
  * Common methods (append, extend, insert, remove, etc.)
  * List comprehensions
- Tuples and their immutability
  * Creation and usage
  * Named tuples
  * Tuple unpacking
- Sets and set operations
  * Creation and modification
  * Set operations (union, intersection, difference)
  * Set comprehensions
- Dictionaries
  * Creation and modification
  * Accessing and modifying values
  * Dictionary methods
  * Dictionary comprehensions
  * Nested dictionaries

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it, lprint
import time
from collections import namedtuple

# ANSI color codes
BLUE = "\033[94m"      # General text
GREEN = "\033[92m"     # Success messages
RED = "\033[91m"       # Error messages
YELLOW = "\033[33m"    # Questions and prompts
CYAN = "\033[96m"      # Code blocks
BOLD = "\033[1m"       # Headers
RESET = "\033[0m"      # Reset all formatting

def color_print(text, color=BLUE):
    """Print text in color"""
    lprint(f"{color}{text}{RESET}")

def print_code_block(code, indent=0):
    """Print a code block with proper indentation"""
    # Add a newline before the code block
    lprint("")
    
    # Split into lines
    lines = code.strip().split('\n')
    indent_str = " " * indent
    
    # Print each line
    for line in lines:
        if line.strip():
            # Add consistent indentation and color the entire line
            lprint(f"{indent_str}{CYAN}{line.rstrip()}{RESET}")
        else:
            lprint("")  # Print empty lines as-is
    
    # Add a newline after the code block
    lprint("")

def get_user_input(prompt):
    """Get user input with a prompt"""
    lprint("\n" + prompt)
    return input().strip().lower()

def check_answer(user_answer, correct_answers, explanation):
    """Check user answer and provide feedback"""
    if user_answer in correct_answers:
        color_print(f"\n✅ Correct! {explanation}", GREEN)
        return True
    else:
        color_print(f"\n❌ Not quite. {explanation}", RED)
        return False

@describe("Interactive Python Data Structures")
class TestPythonDataStructuresInteractive:
    
    @it("teaches about lists and list operations")
    def test_lists(self):
        color_print(f"\n{BOLD}=== Welcome to Python Data Structures - Part 1: Lists ==={RESET}", YELLOW)
        color_print("Let's learn about Python lists in detail.")
        time.sleep(1)

        # Question 1: List creation and modification
        color_print(f"\n{BOLD}Question 1: List Creation and Modification{RESET}")
        color_print("Look at these list operations:", YELLOW)
        print_code_block("""
            # Creating lists
            numbers = [1, 2, 3, 4, 5]
            mixed = [1, "hello", 3.14, True]
            nested = [1, [2, 3], [4, [5, 6]]]
            
            # List methods
            numbers.append(6)       # Add to end: [1, 2, 3, 4, 5, 6]
            numbers.insert(0, 0)    # Insert at index: [0, 1, 2, 3, 4, 5, 6]
            numbers.extend([7, 8])  # Add multiple: [0, 1, 2, 3, 4, 5, 6, 7, 8]
            
            # Removing elements
            numbers.pop()           # Remove and return last: 8
            numbers.remove(0)       # Remove first occurrence of 0
            del numbers[0]          # Delete at index
                         """)
        answer = get_user_input(f"{YELLOW}Which method adds a single element to the end of a list? {RESET}")
        check_answer(
            answer,
            ['append', 'append()', '.append', '.append()'],
            "The append() method adds a single element to the end of a list. Use extend() to add multiple elements."
        )

        # Question 2: List slicing
        color_print(f"\n{BOLD}Question 2: List Slicing{RESET}")
        color_print("Look at these list slicing operations:", YELLOW)
        print_code_block("""
            numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            
            # Basic slicing [start:end:step]
            first_three = numbers[:3]      # [0, 1, 2]
            middle = numbers[3:7]          # [3, 4, 5, 6]
            last_three = numbers[-3:]      # [7, 8, 9]
            
            # Step slicing
            every_second = numbers[::2]    # [0, 2, 4, 6, 8]
            reversed_list = numbers[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
            
            # Negative indices
            last = numbers[-1]            # 9
            except_last = numbers[:-1]    # [0, 1, 2, 3, 4, 5, 6, 7, 8]
                         """)
        answer = get_user_input(f"{YELLOW}What step value in slicing reverses a list? {RESET}")
        check_answer(
            answer,
            ['-1', 'negative 1', '-1 step'],
            "Using a step of -1 ([::-1]) reverses a list. This works for any sequence type in Python!"
        )

        # Question 3: List comprehensions
        color_print(f"\n{BOLD}Question 3: List Comprehensions{RESET}")
        color_print("Look at these list comprehension examples:", YELLOW)
        print_code_block("""
            numbers = [1, 2, 3, 4, 5]
            
            # Basic list comprehension
            squares = [x**2 for x in numbers]  # [1, 4, 9, 16, 25]
            
            # With condition
            evens = [x for x in numbers if x % 2 == 0]  # [2, 4]
            
            # Nested comprehension
            matrix = [[i+j for j in range(3)] for i in range(3)]
            # [[0,1,2],
            #  [1,2,3],
            #  [2,3,4]]
            
            # Multiple operations
            processed = [str(x) + '!' for x in numbers if x > 2]
            # ['3!', '4!', '5!']
                         """)
        answer = get_user_input(f"{YELLOW}What character surrounds a list comprehension? {RESET}")
        check_answer(
            answer,
            ['[]', 'square brackets', 'brackets'],
            "List comprehensions are surrounded by square brackets []. This creates a new list from the expression."
        )

    @it("teaches about tuples and their immutability")
    def test_tuples(self):
        color_print(f"\n{BOLD}=== Part 2: Tuples ==={RESET}")
        color_print("Let's learn about Python tuples and their special properties.")
        time.sleep(1)

        # Question 1: Tuple basics
        color_print(f"\n{BOLD}Question 1: Tuple Basics{RESET}")
        color_print("Look at these tuple operations:", YELLOW)
        print_code_block("""
            # Creating tuples
            empty = ()
            single = (1,)               # Note the comma!
            numbers = (1, 2, 3, 4, 5)
            mixed = (1, "hello", 3.14)
            
            # Tuple immutability
            try:
                numbers[0] = 10         # This raises TypeError
            except TypeError:
                print("Tuples are immutable!")
            
            # Tuple methods (only 2 methods!)
            count = numbers.count(1)    # Count occurrences: 1
            index = numbers.index(3)    # Find index: 2
                         """)
        answer = get_user_input(f"{YELLOW}What do you need to add to make a single-element tuple? {RESET}")
        check_answer(
            answer,
            ['comma', ',', 'trailing comma'],
            "A single-element tuple needs a trailing comma (1,) - without it, (1) is just a number in parentheses!"
        )

        # Question 2: Named tuples
        color_print(f"\n{BOLD}Question 2: Named Tuples{RESET}")
        color_print("Look at these named tuple examples:", YELLOW)
        print_code_block("""
            from collections import namedtuple
            
            # Creating a named tuple type
            Point = namedtuple('Point', ['x', 'y'])
            
            # Creating instances
            p1 = Point(1, 2)
            p2 = Point(x=3, y=4)
            
            # Accessing values
            print(p1.x)          # Using name: 1
            print(p1[0])         # Using index: 1
            
            # Unpacking
            x, y = p2            # x = 3, y = 4
            
            # Converting to dictionary
            point_dict = p1._asdict()  # {'x': 1, 'y': 2}
                         """)
        answer = get_user_input(f"{YELLOW}What module provides named tuples in Python? {RESET}")
        check_answer(
            answer,
            ['collections', 'collections module'],
            "The collections module provides namedtuple and many other useful data structures!"
        )

        # Question 3: Tuple unpacking
        color_print(f"\n{BOLD}Question 3: Tuple Unpacking{RESET}")
        color_print("Look at these tuple unpacking examples:", YELLOW)
        print_code_block("""
            # Basic unpacking
            coordinates = (1, 2, 3)
            x, y, z = coordinates       # x = 1, y = 2, z = 3
            
            # Using * for remaining items
            first, *rest = (1, 2, 3, 4, 5)  # first = 1, rest = [2, 3, 4, 5]
            *start, last = (1, 2, 3, 4)     # start = [1, 2, 3], last = 4
            
            # Ignoring values with _
            name, _, age = ("Alice", "Smith", 30)  # Ignore middle name
            
            # Swapping values
            a, b = 1, 2
            a, b = b, a          # Swap values using tuple unpacking
                         """)
        answer = get_user_input(f"{YELLOW}In tuple unpacking, what symbol is used to collect multiple remaining values into a list? {RESET}")
        check_answer(
            answer,
            ['*', 'asterisk'],
            "The asterisk (*) packs multiple values into a list. This is similar to how *args works in function parameters."
        )

    @it("teaches about sets and set operations")
    def test_sets(self):
        color_print(f"\n{BOLD}=== Part 3: Sets ==={RESET}")
        color_print("Let's learn about Python sets and their operations.")
        time.sleep(1)

        # Question 1: Set basics
        color_print(f"\n{BOLD}Question 1: Set Basics{RESET}")
        color_print("Look at these set operations:", YELLOW)
        print_code_block("""
            # Creating sets
            empty = set()                    # Empty set
            numbers = {1, 2, 3, 4, 5}       # Set literal
            from_list = set([1, 2, 2, 3])   # From list, duplicates removed
            
            # Basic set operations
            numbers.add(6)                   # Add single element
            numbers.update([7, 8, 9])        # Add multiple elements
            numbers.remove(1)                # Remove (raises KeyError if missing)
            numbers.discard(10)              # Remove (no error if missing)
            
            # Membership testing (very fast!)
            is_present = 5 in numbers        # True
            not_present = 10 not in numbers  # True
                         """)
        answer = get_user_input(f"{YELLOW}What method removes an element from a set without raising an error if it's missing? {RESET}")
        check_answer(
            answer,
            ['discard', 'discard()', '.discard', '.discard()'],
            "The discard() method safely removes an element from a set. remove() would raise a KeyError if the element isn't found."
        )

        # Question 2: Set operations
        color_print(f"\n{BOLD}Question 2: Set Operations{RESET}")
        color_print("Look at these set mathematical operations:", YELLOW)
        print_code_block("""
            set1 = {1, 2, 3, 4}
            set2 = {3, 4, 5, 6}
            
            # Mathematical set operations
            union = set1 | set2              # {1, 2, 3, 4, 5, 6}
            intersection = set1 & set2        # {3, 4}
            difference = set1 - set2          # {1, 2}
            symmetric_diff = set1 ^ set2      # {1, 2, 5, 6}
            
            # Method versions
            union = set1.union(set2)
            intersection = set1.intersection(set2)
            difference = set1.difference(set2)
            symmetric_diff = set1.symmetric_difference(set2)
            
            # Subset testing
            is_subset = {1, 2}.issubset(set1)      # True
            is_superset = set1.issuperset({1, 2})  # True
                         """)
        answer = get_user_input(f"{YELLOW}What operator (|) performs the union of two sets? {RESET}")
        check_answer(
            answer,
            ['|', 'pipe', 'vertical bar', 'or'],
            "The | operator (pipe) performs set union. Similarly, & is intersection, - is difference, and ^ is symmetric difference."
        )

        # Question 3: Set comprehensions
        color_print(f"\n{BOLD}Question 3: Set Comprehensions{RESET}")
        color_print("Look at these set comprehension examples:", YELLOW)
        print_code_block("""
            numbers = range(10)
            
            # Basic set comprehension
            squares = {x**2 for x in numbers}
            # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
            
            # With condition
            evens = {x for x in numbers if x % 2 == 0}
            # {0, 2, 4, 6, 8}
            
            # Multiple operations
            processed = {x*10 for x in numbers if x < 5}
            # {0, 10, 20, 30, 40}
            
            # Creating sets of tuples
            coordinates = {(x, y) for x in range(2) for y in range(2)}
            # {(0, 0), (0, 1), (1, 0), (1, 1)}
                         """)
        answer = get_user_input(f"{YELLOW}What characters surrounds a set comprehension? {RESET}")
        check_answer(
            answer,
            ['{}', 'curly braces', 'braces'],
            "Set comprehensions use curly braces {}. This is similar to list comprehensions but creates a set instead."
        )

    @it("teaches about dictionaries")
    def test_dictionaries(self):
        color_print(f"\n{BOLD}=== Part 4: Dictionaries ==={RESET}")
        color_print("Let's learn about Python dictionaries and their operations.")
        time.sleep(1)

        # Question 1: Dictionary basics
        color_print(f"\n{BOLD}Question 1: Dictionary Basics{RESET}")
        color_print("Look at these dictionary operations:", YELLOW)
        print_code_block("""
            # Creating dictionaries
            empty = {}                           # Empty dictionary
            person = {
                'name': 'Alice',
                'age': 30,
                'city': 'New York'
            }
            
            # Accessing and modifying
            name = person['name']                # Get value: 'Alice'
            person['age'] = 31                   # Modify value
            person['email'] = 'alice@email.com'  # Add new key-value
            
            # Safe access with get()
            phone = person.get('phone')          # Returns None if not found
            phone = person.get('phone', 'N/A')   # Custom default value
            
            # Removing items
            age = person.pop('age')              # Remove and return value
            last_item = person.popitem()         # Remove and return last item
                         """)
        answer = get_user_input(f"{YELLOW}What method safely gets a value from a dictionary with a default if the key isn't found? {RESET}")
        check_answer(
            answer,
            ['get', 'get()', '.get', '.get()'],
            "The get() method safely retrieves values with an optional default. Using [] would raise KeyError if the key isn't found."
        )

        # Question 2: Dictionary methods
        color_print(f"\n{BOLD}Question 2: Dictionary Methods{RESET}")
        color_print("Look at these dictionary methods:", YELLOW)
        print_code_block("""
            person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
            
            # Views of dictionary
            keys = person.keys()         # dict_keys(['name', 'age', 'city'])
            values = person.values()     # dict_values(['Alice', 30, 'New York'])
            items = person.items()       # dict_items([('name', 'Alice'), ...])
            
            # Dictionary operations
            person.update({'age': 31, 'job': 'Engineer'})  # Update multiple
            person.setdefault('country', 'USA')   # Set if key missing
            
            # Creating from sequences
            names = ['Alice', 'Bob', 'Charlie']
            ages = [30, 25, 35]
            people = dict(zip(names, ages))  # {'Alice': 30, 'Bob': 25, ...}
                         """)
        answer = get_user_input(f"{YELLOW}What method returns a view of dictionary key-value pairs as tuples? {RESET}")
        check_answer(
            answer,
            ['items', 'items()', '.items', '.items()'],
            "The items() method returns a view of key-value pairs as tuples. This is useful for iterating over dictionaries."
        )

        # Question 3: Dictionary comprehensions
        color_print(f"\n{BOLD}Question 3: Dictionary Comprehensions{RESET}")
        color_print("Look at these dictionary comprehension examples:", YELLOW)
        print_code_block("""
            numbers = range(5)
            
            # Basic dictionary comprehension
            squares = {x: x**2 for x in numbers}
            # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
            
            # With condition
            even_squares = {x: x**2 for x in numbers if x % 2 == 0}
            # {0: 0, 2: 4, 4: 16}
            
            # From two sequences
            names = ['Alice', 'Bob', 'Charlie']
            scores = [85, 92, 78]
            grade_dict = {name: score for name, score in zip(names, scores)}
            # {'Alice': 85, 'Bob': 92, 'Charlie': 78}
            
            # Nested dictionaries
            matrix = {i: {j: i*j for j in range(3)} for i in range(3)}
            # {0: {0: 0, 1: 0, 2: 0},
            #  1: {0: 0, 1: 1, 2: 2},
            #  2: {0: 0, 1: 2, 2: 4}}
                         """)
        answer = get_user_input(f"{YELLOW}What separates keys from values in a dictionary comprehension? {RESET}")
        check_answer(
            answer,
            [':', 'colon'],
            "The colon : separates keys from values in dictionary comprehensions, just like in regular dictionary literals."
        )

        color_print(f"\n{BOLD}🎉 Congratulations! You've completed the Python data structures lesson!{RESET}", GREEN)
        color_print("\nKey takeaways:", YELLOW)
        print_code_block("""
            # 1. Lists
            numbers = [1, 2, 3]         # Mutable, ordered sequence
            numbers.append(4)           # Many useful methods
            [x**2 for x in numbers]     # List comprehension

            # 2. Tuples
            point = (1, 2)              # Immutable, ordered sequence
            Point = namedtuple('Point', ['x', 'y'])  # Named tuples
            x, y = point                # Tuple unpacking

            # 3. Sets
            unique = {1, 2, 3}          # Unordered, unique elements
            a | b                       # Set operations (union, etc.)
            {x for x in range(5)}       # Set comprehension

            # 4. Dictionaries
            person = {'name': 'Alice'}   # Key-value mappings
            person.get('age', 25)        # Safe access with default
            {x: x**2 for x in range(5)}  # Dictionary comprehension
                         """) 