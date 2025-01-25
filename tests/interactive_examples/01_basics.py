"""
Interactive Python Basics Learning Module

This module provides an interactive learning experience for Python basics.
Each concept is presented with code examples and interactive questions
to test understanding.
"""

# import pytest
from tests.conftest import describe, it, lprint
# import sys
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

@describe("Interactive Python Basics")
class TestPythonBasicsInteractive:
    
    @it("teaches about basic output and printing")
    def test_output_basics(self):
        color_print(f"\n{BOLD}=== Welcome to Python Basics - Part 1: Output ==={RESET}")
        color_print("Let's learn about printing output in Python.")
        time.sleep(1)

        # Question 1: Basic print
        color_print(f"\n{BOLD}Question 1: Basic Print{RESET}")
        color_print("Look at these print examples:", YELLOW)
        print_code_block("""
            # Basic print statement
            print("Hello, World!")

            # Print with multiple arguments
            print("Hello", "Python", "World")

            # Print with special characters
            print("Line 1\\nLine 2\\tTabbed")
                         """)
        answer = get_user_input(f"{YELLOW}What character creates a new line in Python strings? (hint: it's a special character): {RESET}")
        check_answer(
            answer,
            ['\\n', 'n', 'newline', '\\n character'],
            "The \\n character creates a new line in strings. \\t creates a tab, and there are other special characters too!"
        )

    @it("teaches about comments and documentation")
    def test_comments(self):
        color_print(f"\n{BOLD}=== Part 2: Comments and Documentation ==={RESET}")
        color_print("Let's learn about writing comments in Python.")
        time.sleep(1)

        # Question 1: Single-line comments
        color_print(f"\n{BOLD}Question 1: Comments{RESET}")
        color_print("Look at these different types of comments:", YELLOW)
        print_code_block("""
            # This is a single-line comment
            print("Hello")  # This is an end-of-line comment

            # Multiple single-line comments
            # can be used to create
            # longer explanations

            '''
            This is a multi-line comment (string)
            It can span multiple lines
            And is useful for longer explanations
            '''

            def greet(name):
                '''
                This is a docstring - it documents what a function does
                Args:
                    name: The name to greet
                Returns:
                    A greeting message
                '''
                return f"Hello, {name}!"
                         """)
        answer = get_user_input(f"{YELLOW}What character starts a single-line comment in Python? {RESET}")
        check_answer(
            answer,
            ['#', 'hash', 'pound', 'hashtag'],
            "The # character starts a single-line comment. Everything after # on that line is ignored by Python."
        )

    @it("teaches about basic program flow")
    def test_program_flow(self):
        color_print(f"\n{BOLD}=== Part 3: Program Flow ==={RESET}")
        color_print("Let's learn about how Python executes code.")
        time.sleep(1)

        # Question 1: Code execution
        color_print(f"\n{BOLD}Question 1: Code Execution{RESET}")
        color_print("Look at this simple program:", YELLOW)
        print_code_block("""
            # Program starts here
            print("Starting program...")

            # Variables are created when assigned
            message = "Hello from Python!"
            print(message)

            # Functions must be defined before use
            def say_goodbye():
                print("Goodbye!")

            # Function calls execute the function
            say_goodbye()

            print("Program finished.")
                         """)
        answer = get_user_input(f"{YELLOW}In Python, can you call a function before it's defined (above its definition)? (yes/no): {RESET}")
        check_answer(
            answer,
            ['no', 'nope', 'false'],
            "Python reads code from top to bottom. You must define functions before you can use them."
        )

        # Question 2: Indentation
        color_print(f"\n{BOLD}Question 2: Indentation{RESET}")
        color_print("Look at how Python uses indentation:", YELLOW)
        print_code_block("""
            def greet(time_of_day):
                # This is indented - it's part of the function
                print(f"Good {time_of_day}!")
                if time_of_day == "morning":
                    # This is indented twice - it's inside the if statement
                    print("Would you like some coffee?")
                # Back to function level
                print("Have a great day!")

            # Not indented - outside the function
            print("Program starting...")
            greet("morning")
                         """)
        answer = get_user_input(f"{YELLOW}What does Python use to define code blocks? (hint: it's not curly braces) {RESET}")
        check_answer(
            answer,
            ['indentation', 'indent', 'spaces', 'space', 'whitespace'],
            "Python uses indentation to define code blocks. This makes code more readable and enforces consistent formatting."
        )

        color_print(f"\n{BOLD}🎉 Congratulations! You've completed the Python basics lesson!{RESET}", GREEN)
        color_print("\nKey takeaways:", YELLOW)
        print_code_block("""
            # 1. Printing Output
            print("Hello, World!")              # Basic printing
            print("Line 1\\nLine 2")            # Special characters

            # 2. Comments
            # Single-line comments start with #
            '''
            Multi-line comments use
            triple quotes
            '''

            # 3. Program Flow
            def my_function():                  # Function definition
                print("Indented code")          # Code blocks use indentation
                if True:                        # Control structures
                    print("More indentation")   # Nested code blocks
                         """) 