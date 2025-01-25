"""
Interactive Python Data Types Learning Module

This module provides an interactive learning experience for Python data types.
Each concept is presented with code examples and interactive questions
to test understanding.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time

@describe("Interactive Python Data Types")
class TestPythonDataTypesInteractive:
    
    @it("teaches about numeric types")
    def test_numeric_types(self):
        print_section_header("Welcome to Python Data Types - Part 1: Numbers")
        print_info("Let's learn about Python's numeric types in detail.")
        time.sleep(1)

        # Question 1: Integer operations
        print_subsection_header("Question 1: Integer Operations")
        print_instruction("Look at these integer operations:")
        print_code_block("""
            # Integer division and modulo
            x = 17
            y = 5

            quotient = x // y   # Integer division (drops decimal)
            remainder = x % y   # Modulo (remainder)
            binary = bin(x)     # Binary representation: 0b10001
            hexadecimal = hex(x)  # Hexadecimal: 0x11
            absolute = abs(-x)  # Absolute value: 17

            print(f"{x} divided by {y} is {quotient} remainder {remainder}")
            print(f"{x} in binary is {binary}")
            print(f"{x} in hexadecimal is {hexadecimal}")
                         """)
        answer = get_user_input("What operator gives you the integer division result (no decimal)?")
        check_answer(
            answer,
            ['//', 'double slash', 'floor division'],
            "The // operator performs integer division, dropping any decimal part. For example, 17 // 5 = 3 (not 3.4)."
        )

        # Question 2: Float operations
        print_subsection_header("Question 2: Float Operations")
        print_instruction("Look at these floating-point operations:")
        print_code_block("""
            import math

            # Float operations and representations
            pi = 3.14159
            e = 2.71828
            scientific = 1.23e-4  # Scientific notation: 0.000123

            # Built-in float operations
            rounded = round(pi, 2)      # Round to 2 decimal places: 3.14
            floor = math.floor(pi)      # Round down to nearest integer: 3
            ceiling = math.ceil(pi)     # Round up to nearest integer: 4

            # Precision and formatting
            print(f"π rounded: {rounded}")
            print(f"π as percentage: {pi:.2%}")  # 314.16%
            print(f"e in scientific: {e:e}")     # 2.718280e+00
                         """)
        answer = get_user_input("What function rounds a float down to the nearest integer?")
        check_answer(
            answer,
            ['floor', 'math.floor', 'floor()', 'math.floor()'],
            "math.floor() rounds down to the nearest integer. Similarly, math.ceil() rounds up."
        )

        # Question 3: Complex numbers
        print_subsection_header("Question 3: Complex Numbers")
        print_instruction("Look at these complex number operations:")
        print_code_block("""
            # Complex numbers (real + imaginary)
            z1 = 3 + 4j      # Direct definition
            z2 = complex(1, 2)  # Using complex() function

            # Complex operations
            magnitude = abs(z1)          # Length: √(3² + 4²) = 5
            conjugate = z1.conjugate()   # 3 - 4j

            # Accessing parts
            real_part = z1.real         # 3.0
            imaginary_part = z1.imag    # 4.0

            print(f"|{z1}| = {magnitude}")
            print(f"Conjugate of {z1} is {conjugate}")
                         """)
        answer = get_user_input("What letter is commonly used for the imaginary unit in Python?")
        check_answer(
            answer,
            ['j', 'j unit'],
            "Python uses 'j' for the imaginary unit (some other languages use 'i'). So 3+4j represents a complex number."
        )

        print_success("🎉 Congratulations! You've completed the numeric types lesson!")
        print_info("Key takeaways:")
        print_code_block("""
            # 1. Integer Operations
            x // y              # Integer division
            x % y               # Modulo (remainder)
            bin(x), hex(x)      # Binary and hex representations

            # 2. Float Operations
            round(3.14159, 2)   # Round to decimal places
            math.floor(3.7)     # Round down to integer
            math.ceil(3.2)      # Round up to integer

            # 3. Complex Numbers
            z = 3 + 4j          # Complex number literal
            z.real, z.imag      # Access parts
            abs(z)              # Get magnitude
                         """)

    @it("teaches about text types")
    def test_text_types(self):
        print_section_header("Part 2: Text Types (Strings)")
        print_info("Let's learn about Python's string type in detail.")
        time.sleep(1)

        # Question 1: String creation
        print_subsection_header("Question 1: String Creation")
        print_instruction("Look at these ways to create strings:")
        print_code_block("""
            # Different ways to create strings
            single = 'Single quotes'
            double = "Double quotes"
            triple = '''Multi-line
            string using
            triple quotes'''
            raw = r"Raw string: \n is not a newline"
            formatted = f"2 + 2 = {2 + 2}"

            # Escape sequences
            escaped = "Tab\\tNewline\\nQuote\\""

            # Unicode and bytes
            unicode = "Hello 🌍"  # Unicode string
            bytes_str = b"Hello"  # Bytes string
                         """)
        answer = get_user_input("What prefix creates a 'raw' string where backslashes are treated literally?")
        check_answer(
            answer,
            ['r', 'r prefix', 'raw'],
            "The 'r' prefix creates a raw string where backslashes are treated as literal characters. Useful for regex patterns!"
        )

        # Question 2: String methods
        print_subsection_header("Question 2: String Methods")
        print_instruction("Look at these string operations:")
        print_code_block("""
            text = "  Python Programming  "

            # Case methods
            upper = text.upper()           # "  PYTHON PROGRAMMING  "
            lower = text.lower()           # "  python programming  "
            title = text.title()           # "  Python Programming  "
            swapped = text.swapcase()      # "  pYTHON pROGRAMMING  "

            # Cleaning methods
            stripped = text.strip()        # "Python Programming"
            replaced = text.replace('P', 'J')  # "  Jython Jrogramming  "

            # Analysis methods
            word_count = len(text.split())  # 2
            is_alpha = text.isalpha()       # False (has spaces)
            starts_with = text.startswith('  Py')  # True

            # Finding and counting
            position = text.find('Pro')     # 8
            count = text.count('m')         # 2
                         """)
        answer = get_user_input("What method removes whitespace from both ends of a string?")
        check_answer(
            answer,
            ['strip', 'strip()', '.strip', '.strip()'],
            "The strip() method removes whitespace from both ends. Use lstrip() for left only, rstrip() for right only."
        )

    @it("teaches about boolean type")
    def test_boolean_type(self):
        print_section_header("Part 3: Boolean Type and Truth Values")
        print_info("Let's learn about Python's boolean type and truth testing.")
        time.sleep(1)

        # Question 1: Boolean operations
        print_subsection_header("Question 1: Boolean Operations")
        print_instruction("Look at these boolean operations:")
        print_code_block("""
            # Basic boolean values
            is_ready = True
            has_error = False

            # Boolean operators
            and_result = True and False    # False
            or_result = True or False      # True
            not_result = not True         # False

            # Short-circuit evaluation
            result1 = False and print("Not printed")  # False, print not executed
            result2 = True or print("Not printed")    # True, print not executed

            # Comparison operations
            x = 5
            y = 10
            is_greater = x > y             # False
            is_equal = x == y             # False
            is_not_equal = x != y         # True
                         """)
        answer = get_user_input("What happens in 'x and y' if x is False?")
        check_answer(
            answer,
            ['short circuit', 'short-circuit', 'skips y', 'y not evaluated', 'returns false', 'returns x'],
            "Python uses short-circuit evaluation. If x is False in 'x and y', it returns False without evaluating y."
        )

        # Question 2: Truth values
        print_subsection_header("Question 2: Truth Values")
        print_instruction("Look at how Python determines truth values:")
        print_code_block("""
            # Values considered False:
            bool(None)         # False
            bool(0)            # False
            bool("")           # False (empty string)
            bool([])           # False (empty list)
            bool({})           # False (empty dict)
            bool(set())        # False (empty set)

            # Values considered True:
            bool(42)           # True (non-zero numbers)
            bool("Hello")      # True (non-empty string)
            bool([1, 2, 3])    # True (non-empty list)
            bool({'a': 1})     # True (non-empty dict)

            # Common patterns
            items = []
            if not items:          # Check for empty list
                print("No items")

            name = "Alice"
            if name:               # Check for non-empty string
                print(f"Hello, {name}")
                         """)
        answer = get_user_input("What built-in function converts other types to boolean?")
        check_answer(
            answer,
            ['bool', 'bool()', 'bool function'],
            "The bool() function converts values to True or False. Empty/zero values become False, others become True."
        )

        print_success("🎉 Congratulations! You've completed the Python data types lesson!")
        print_info("Key takeaways:")
        print_code_block("""
            # 1. Boolean Operations
            and_result = True and False    # False
            or_result = True or False      # True
            not_result = not True         # False

            # 2. Truth Values
            bool(42)           # True (non-zero numbers)
            bool("Hello")      # True (non-empty string)

            # 3. Boolean Type
            valid = True        # Basic boolean
            bool("Hello")      # Truth testing
                         """) 