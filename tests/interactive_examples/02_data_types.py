"""
Interactive Python Data Types Learning Module

This module provides an interactive learning experience for Python data types.
Each concept is presented with code examples and interactive questions
to test understanding.
"""

from tests.conftest import describe, it, lprint
import time

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

@describe("Interactive Python Data Types")
class TestPythonDataTypesInteractive:
    
    @it("teaches about numeric types")
    def test_numeric_types(self):
        color_print(f"\n{BOLD}=== Welcome to Python Data Types - Part 1: Numbers ==={RESET}", YELLOW)
        color_print("Let's learn about Python's numeric types in detail.")
        time.sleep(1)

        # Question 1: Integer operations
        color_print(f"\n{BOLD}Question 1: Integer Operations{RESET}")
        color_print("Look at these integer operations:", YELLOW)
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
        answer = get_user_input(f"{YELLOW}What operator gives you the integer division result (no decimal)? {RESET}")
        check_answer(
            answer,
            ['//', 'double slash', 'floor division'],
            "The // operator performs integer division, dropping any decimal part. For example, 17 // 5 = 3 (not 3.4)."
        )

        # Question 2: Float operations
        color_print(f"\n{BOLD}Question 2: Float Operations{RESET}")
        color_print("Look at these floating-point operations:", YELLOW)
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
        answer = get_user_input(f"{YELLOW}What function rounds a float down to the nearest integer? {RESET}")
        check_answer(
            answer,
            ['floor', 'math.floor', 'floor()', 'math.floor()'],
            "math.floor() rounds down to the nearest integer. Similarly, math.ceil() rounds up."
        )

        # Question 3: Complex numbers
        color_print(f"\n{BOLD}Question 3: Complex Numbers{RESET}")
        color_print("Look at these complex number operations:", YELLOW)
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
        answer = get_user_input(f"{YELLOW}What letter is commonly used for the imaginary unit in Python? {RESET}")
        check_answer(
            answer,
            ['j', 'j unit'],
            "Python uses 'j' for the imaginary unit (some other languages use 'i'). So 3+4j represents a complex number."
        )

    @it("teaches about text types")
    def test_text_types(self):
        color_print(f"\n{BOLD}=== Part 2: Text Types (Strings) ==={RESET}")
        color_print("Let's learn about Python's string type in detail.")
        time.sleep(1)

        # Question 1: String creation
        color_print(f"\n{BOLD}Question 1: String Creation{RESET}")
        color_print("Look at these ways to create strings:", YELLOW)
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
        answer = get_user_input(f"{YELLOW}What prefix creates a 'raw' string where backslashes are treated literally? {RESET}")
        check_answer(
            answer,
            ['r', 'r prefix', 'raw'],
            "The 'r' prefix creates a raw string where backslashes are treated as literal characters. Useful for regex patterns!"
        )

        # Question 2: String methods
        color_print(f"\n{BOLD}Question 2: String Methods{RESET}")
        color_print("Look at these string operations:", YELLOW)
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
        answer = get_user_input(f"{YELLOW}What method removes whitespace from both ends of a string? {RESET}")
        check_answer(
            answer,
            ['strip', 'strip()', '.strip', '.strip()'],
            "The strip() method removes whitespace from both ends. Use lstrip() for left only, rstrip() for right only."
        )

    @it("teaches about boolean type")
    def test_boolean_type(self):
        color_print(f"\n{BOLD}=== Part 3: Boolean Type and Truth Values ==={RESET}")
        color_print("Let's learn about Python's boolean type and truth testing.")
        time.sleep(1)

        # Question 1: Boolean operations
        color_print(f"\n{BOLD}Question 1: Boolean Operations{RESET}")
        color_print("Look at these boolean operations:", YELLOW)
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
        answer = get_user_input(f"{YELLOW}What happens in 'x and y' if x is False? {RESET}")
        check_answer(
            answer,
            ['short circuit', 'short-circuit', 'skips y', 'y not evaluated', 'returns false', 'returns x'],
            "Python uses short-circuit evaluation. If x is False in 'x and y', it returns False without evaluating y."
        )

        # Question 2: Truth values
        color_print(f"\n{BOLD}Question 2: Truth Values{RESET}")
        color_print("Look at how Python determines truth values:", YELLOW)
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
        answer = get_user_input(f"{YELLOW}What built-in function converts other types to boolean? {RESET}")
        check_answer(
            answer,
            ['bool', 'bool()', 'bool function'],
            "The bool() function converts values to True or False. Empty/zero values become False, others become True."
        )

        color_print(f"\n{BOLD}🎉 Congratulations! You've completed the Python data types lesson!{RESET}", GREEN)
        color_print("\nKey takeaways:", YELLOW)
        print_code_block("""
            # 1. Numeric Types
            x = 42              # int: whole numbers
            y = 3.14           # float: decimal numbers
            z = 3 + 4j         # complex: real + imaginary

            # 2. Text Type (str)
            text = "Hello"      # Basic string
            f"{x} = {y}"       # f-string formatting
            text.upper()       # String methods

            # 3. Boolean Type
            valid = True        # Basic boolean
            bool("Hello")      # Truth testing
            x > y and y < z    # Boolean operations
                         """) 