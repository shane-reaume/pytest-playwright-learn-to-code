"""
Python Control Flow Learning Module

This module covers Python's control flow concepts through practical examples:
- Conditional Statements
  * if, elif, else
  * Comparison operators
  * Logical operators
- Loops
  * for loops and iteration
  * while loops
  * break and continue
  * else clause in loops
- Match Statements (Python 3.10+)
  * Pattern matching
  * Case patterns
  * Guard clauses
- Comprehensions
  * List comprehensions
  * Conditional comprehensions
  * Nested comprehensions

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time

@describe("Interactive Python Control Flow")
class TestPythonControlFlowInteractive:
    
    @it("teaches about conditional statements")
    def test_conditionals(self):
        print_section_header("Welcome to Python Control Flow - Part 1: Conditionals")
        print_info("Let's learn about Python's conditional statements in detail.")
        time.sleep(1)

        # Question 1: Basic if statements
        print_subsection_header("Question 1: Basic If Statements")
        print_instruction("Look at these conditional statements:")
        print_code_block("""
            # Basic if statement
            age = 18
            if age >= 18:
                print("You are an adult")
            else:
                print("You are a minor")

            # Multiple conditions with elif
            score = 85
            if score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'
            elif score >= 70:
                grade = 'C'
            else:
                grade = 'F'

            # Conditional expression (ternary operator)
            status = "pass" if score >= 60 else "fail"
                         """)
        answer = get_user_input("What keyword is used for alternative conditions between if and else?")
        check_answer(
            answer,
            ['elif', 'elif keyword'],
            "The elif keyword (else if) allows you to check multiple conditions in sequence."
        )

        # Question 2: Comparison and logical operators
        print_subsection_header("Question 2: Comparison and Logical Operators")
        print_instruction("Look at these operators and compound conditions:")
        print_code_block("""
            x = 5
            y = 10
            
            # Comparison operators
            equal = x == y          # False
            not_equal = x != y      # True
            greater = x > y         # False
            less = x < y            # True
            greater_eq = x >= y     # False
            less_eq = x <= y        # True
            
            # Logical operators
            both = x < 10 and y > 5      # True (both conditions true)
            either = x < 3 or y > 8      # True (at least one true)
            opposite = not x == y        # True (opposite of False)
            
            # Chained comparisons
            in_range = 0 <= x <= 10      # True (0 <= x and x <= 10)
                         """)
        answer = get_user_input("What logical operator returns True if both conditions are True?")
        check_answer(
            answer,
            ['and', 'and operator'],
            "The and operator requires both conditions to be True. Use or if you want True when at least one condition is True."
        )

        # Question 3: Truth value testing
        print_subsection_header("Question 3: Truth Value Testing")
        print_instruction("Look at these truth value examples:")
        print_code_block("""
            # Values considered False
            if not None:               # None is False
                print("None is False")
                
            if not False:             # False is False
                print("False is False")
                
            if not 0:                 # Zero is False
                print("0 is False")
                
            if not "":               # Empty string is False
                print("Empty string is False")
                
            if not []:               # Empty list is False
                print("Empty list is False")
                
            # Values considered True
            if True:                  # True is True
                print("True is True")
                
            if 42:                   # Non-zero numbers are True
                print("42 is True")
                
            if "hello":              # Non-empty strings are True
                print("hello is True")
                
            if [1, 2, 3]:            # Non-empty lists are True
                print("[1, 2, 3] is True")
                         """)
        answer = get_user_input("What number is considered False in truth value testing?")
        check_answer(
            answer,
            ['0', 'zero'],
            "Zero (0) is considered False in truth value testing. All other numbers are considered True."
        )

    @it("teaches about loops and iteration")
    def test_loops(self):
        print_section_header("Part 2: Loops and Iteration")
        print_info("Let's learn about Python's loop structures.")
        time.sleep(1)

        # Question 1: For loops
        print_subsection_header("Question 1: For Loops")
        print_instruction("Look at these for loop examples:")
        print_code_block("""
            # Basic for loop with range
            for i in range(5):
                print(i)              # Prints 0, 1, 2, 3, 4
                
            # Looping over sequences
            fruits = ['apple', 'banana', 'cherry']
            for fruit in fruits:
                print(fruit)
                
            # Enumerate for index and value
            for index, fruit in enumerate(fruits):
                print(f"{index}: {fruit}")
                
            # Nested loops
            matrix = [[1, 2], [3, 4]]
            for row in matrix:
                for num in row:
                    print(num)
                         """)
        answer = get_user_input("What function gives you both index and value when looping over a sequence?")
        check_answer(
            answer,
            ['enumerate', 'enumerate()', '.enumerate', '.enumerate()'],
            "The enumerate() function provides both index and value, useful when you need the position in the sequence."
        )

        # Question 2: While loops
        print_subsection_header("Question 2: While Loops")
        print_instruction("Look at these while loop examples:")
        print_code_block("""
            # Basic while loop
            count = 0
            while count < 5:
                print(count)
                count += 1
                
            # Break statement
            while True:
                if count >= 10:
                    break             # Exit loop when count reaches 10
                count += 1
                
            # Continue statement
            i = 0
            while i < 5:
                i += 1
                if i == 3:
                    continue         # Skip the rest of this iteration
                print(i)             # Prints 1, 2, 4, 5
                
            # While with else
            n = 0
            while n < 3:
                print(n)
                n += 1
            else:
                print("Loop completed!")  # Runs if loop completes normally
                         """)
        answer = get_user_input("What keyword is used to immediately exit a loop?")
        check_answer(
            answer,
            ['break', 'break statement'],
            "The break statement immediately exits the loop. Use continue to skip to the next iteration."
        )

        # Question 3: Loop control
        print_subsection_header("Question 3: Loop Control")
        print_instruction("Look at these loop control examples:")
        print_code_block("""
            # Loop with else clause
            for num in range(2, 10):
                for x in range(2, num):
                    if num % x == 0:
                        print(f"{num} equals {x} * {num//x}")
                        break
                else:
                    print(f"{num} is prime")
                    
            # Nested loop with break
            found = False
            for i in range(5):
                for j in range(5):
                    if i * j == 6:
                        print(f"Found: {i} * {j} = 6")
                        found = True
                        break
                if found:
                    break
                    
            # Continue with condition
            for i in range(10):
                if i % 2 == 0:
                    continue        # Skip even numbers
                print(i)           # Print odd numbers only
                         """)
        answer = get_user_input("What happens to a loop's else clause if the loop is exited with break?")
        check_answer(
            answer,
            ['skipped', 'not executed', 'doesn\'t run', 'doesnt run', 'ignored'],
            "The else clause in a loop only runs if the loop completes normally. If break is used, the else clause is skipped."
        )

        print_success("🎉 Congratulations! You've completed the Python control flow lesson!")
        print_info("Key takeaways:")
        print_code_block("""
            # 1. Conditional Statements
            if condition:              # Basic if statement
                do_something()
            elif other_condition:      # Alternative condition
                do_other_thing()
            else:                      # Default case
                do_default()

            # 2. Loops
            for item in sequence:      # For loop
                process(item)
            
            while condition:          # While loop
                update_condition()
                if should_stop:
                    break            # Exit loop
                if should_skip:
                    continue         # Next iteration

            # 3. Loop Control
            for x in range(5):
                if condition:
                    break           # Exit immediately
                if other_condition:
                    continue        # Skip to next iteration
            else:
                print("Completed")  # Runs if no break
                         """) 