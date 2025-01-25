"""
Interactive Python Basics Learning Module

This module provides an interactive learning experience for Python basics.
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

@describe("Interactive Python Basics")
class TestPythonBasicsInteractive:
    
    @it("teaches about basic output and printing")
    def test_output_basics(self):
        print_section_header("Welcome to Python Basics - Part 1: Output")
        print_info("Let's learn about printing output in Python.")
        time.sleep(1)

        # Question 1: Basic print
        print_subsection_header("Question 1: Basic Print")
        print_instruction("Look at these print examples:")
        print_code_block("""
            # Basic print statement
            print("Hello, World!")

            # Print with multiple arguments
            print("Hello", "Python", "World")

            # Print with special characters
            print("Line 1\\nLine 2\\tTabbed")
                         """)
        answer = get_user_input("What character creates a new line in Python strings? (hint: it's a special character)")
        check_answer(
            answer,
            ['\\n', 'n', 'newline', '\\n character'],
            "The \\n character creates a new line in strings. \\t creates a tab, and there are other special characters too!"
        )

        # Question 2: Comments
        print_subsection_header("Question 2: Comments")
        print_instruction("Look at these different types of comments:")
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
        answer = get_user_input("What character starts a single-line comment in Python?")
        check_answer(
            answer,
            ['#', 'hash', 'pound', 'hashtag'],
            "The # character starts a single-line comment. Everything after # on that line is ignored by Python."
        )

        # Question 3: Program Flow
        print_subsection_header("Question 3: Program Flow")
        print_instruction("Look at this simple program:")
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
        answer = get_user_input("In Python, can you call a function before it's defined (above its definition)? (yes/no)")
        check_answer(
            answer,
            ['no', 'nope', 'false'],
            "Python reads code from top to bottom. You must define functions before you can use them."
        )

        print_success("🎉 Congratulations! You've completed the Python basics lesson!")
        print_info("Key takeaways:")
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