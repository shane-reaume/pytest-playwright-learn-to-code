"""
Python Basics Learning Module

This module covers fundamental Python concepts through practical test examples:
- Printing "Hello World!" and basic output
- Simple expressions and statements
- Comments (single-line and multi-line)
- Getting started with variables
- Basic operators (arithmetic, comparison, logical)
- Basic input/output operations

Each test demonstrates a specific concept with practical examples.
"""

from playwright.sync_api import Page
from tests.conftest import describe, it, lprint  # Import lprint from conftest

# ====== Basic Python Examples ======

# 1. Hello World and Basic Output
lprint("=== Hello World Examples ===")
lprint("Hello, World!")  # The traditional first program
lprint("Multiple", "arguments", "are", "separated", "by", "spaces")  # prints with spaces between args
lprint("Line 1\nLine 2")  # \n creates a new line
hw = ("H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!") # list of characters
lprint(*hw, sep="") # using *args to unpack the list and sep="" to remove the spaces

# 2. Comments
# This is a single-line comment
'''
This is a multi-line comment (string)
It can span multiple lines
And is useful for longer explanations
'''

# 3. Variables and Basic Data Types
lprint("\n=== Variables and Data Types ===")
name = "Python"  # String variable
age = 30         # Integer variable
price = 19.99    # Float variable
is_active = True # Boolean variable
lprint(f"name: {name} (type: {type(name)})")
lprint(f"age: {age} (type: {type(age)})")
lprint(f"price: {price} (type: {type(price)})")
lprint(f"is_active: {is_active} (type: {type(is_active)})")

# 4. Basic Operators
# Arithmetic operators
lprint("\n=== Arithmetic Operators ===")
x = 10 + 5  # Addition
y = 10 - 5  # Subtraction
z = 10 * 5  # Multiplication
w = 10 / 5  # Division (returns float)
p = 10 // 3 # Floor division
r = 10 % 3  # Modulus (remainder)
e = 2 ** 3  # Exponentiation
lprint(f"10 + 5 = {x}")
lprint(f"10 - 5 = {y}")
lprint(f"10 * 5 = {z}")
lprint(f"10 / 5 = {w}")
lprint(f"10 // 3 = {p}")
lprint(f"10 % 3 = {r}")
lprint(f"2 ** 3 = {e}")

# Comparison operators
lprint("\n=== Comparison Operators ===")
a = 5 > 3   # Greater than
b = 5 < 3   # Less than
c = 5 >= 5  # Greater than or equal
d = 5 <= 4  # Less than or equal
e = 5 == 5  # Equal to
f = 5 != 3  # Not equal to
lprint(f"5 > 3 is {a}")
lprint(f"5 < 3 is {b}")
lprint(f"5 >= 5 is {c}")
lprint(f"5 <= 4 is {d}")
lprint(f"5 == 5 is {e}")
lprint(f"5 != 3 is {f}")

# Logical operators
lprint("\n=== Logical Operators ===")
g = True and False  # Logical AND
h = True or False   # Logical OR
i = not True       # Logical NOT
lprint(f"True and False is {g}")
lprint(f"True or False is {h}")
lprint(f"not True is {i}")

# 5. String Operations
lprint("\n=== String Operations ===")
greeting = "Hello"
name = "Python"
full_greeting = greeting + " " + name  # String concatenation
repeated = "Ha" * 3                    # String repetition
upper_case = greeting.upper()          # String method for uppercase
lower_case = greeting.lower()          # String method for lowercase
lprint(f"Concatenation: {full_greeting}")
lprint(f"Repetition: {repeated}")
lprint(f"Uppercase: {upper_case}")
lprint(f"Lowercase: {lower_case}")

@describe("Python Basics - Output and Printing")
class TestBasicOutput:
    @it("should demonstrate basic print functionality")
    def test_basic_print(self, capsys):
        lprint("Hello, World!")
        # We're using stderr, so we check stderr instead of stdout
        captured = capsys.readouterr()
        assert "Hello, World!" in captured.err
    
    @it("should show print with multiple arguments")
    def test_print_multiple_args(self, capsys):
        lprint("Hello", "Python", "World")
        captured = capsys.readouterr()
        assert "Hello Python World" in captured.err
    
    @it("should demonstrate special characters")
    def test_special_chars(self, capsys):
        lprint("Line 1\nLine 2\tTabbed")
        captured = capsys.readouterr()
        assert "Line 1" in captured.err
        assert "Line 2" in captured.err
        assert "Tabbed" in captured.err

@describe("Python Basics - Variables and Operations")
class TestBasicOperations:
    @it("should demonstrate arithmetic operations")
    def test_arithmetic(self):
        assert 10 + 5 == 15, "Addition failed"
        assert 10 - 5 == 5, "Subtraction failed"
        assert 10 * 5 == 50, "Multiplication failed"
        assert 10 / 5 == 2.0, "Division failed"
        assert 10 // 3 == 3, "Floor division failed"
        assert 10 % 3 == 1, "Modulus failed"
        assert 2 ** 3 == 8, "Exponentiation failed"
    
    @it("should demonstrate comparison operations")
    def test_comparisons(self):
        assert 5 > 3, "Greater than failed"
        assert not (5 < 3), "Less than failed"
        assert 5 >= 5, "Greater than or equal failed"
        assert 5 <= 5, "Less than or equal failed"
        assert 5 == 5, "Equal to failed"
        assert 5 != 3, "Not equal failed"
    
    @it("should demonstrate logical operations")
    def test_logical_operators(self):
        assert True and True, "AND operation failed"
        assert True or False, "OR operation failed"
        assert not False, "NOT operation failed"
        
    @it("should demonstrate string operations")
    def test_string_operations(self):
        name = "Python"
        greeting = "Hello"
        assert greeting + " " + name == "Hello Python", "String concatenation failed"
        assert "Ha" * 3 == "HaHaHa", "String repetition failed"
        assert "hello".upper() == "HELLO", "Uppercase conversion failed"
        assert "HELLO".lower() == "hello", "Lowercase conversion failed"

@describe("Python Basics - Browser Integration Examples")
class TestBasicBrowserTests:
    @it("should demonstrate basic DOM text manipulation")
    def test_browser_text(self, page: Page):
        # Navigate to a blank page
        page.goto("about:blank")
        
        # Use evaluate to run JavaScript that creates and manipulates text
        page.evaluate("""() => {
            document.body.innerHTML = `
                <div id="test">Hello World</div>
                <div id="counter">0</div>
            `;
        }""")
        
        # Verify text content
        assert page.locator("#test").inner_text() == "Hello World"
    
    @it("should demonstrate basic arithmetic in browser context")
    def test_browser_arithmetic(self, page: Page):
        page.goto("about:blank")
        
        # Use evaluate to perform calculations in JavaScript
        result = page.evaluate("""() => {
            const x = 10;
            const y = 5;
            return {
                sum: x + y,
                difference: x - y,
                product: x * y,
                quotient: x / y
            };
        }""")
        
        # Verify calculations match Python's arithmetic
        assert result["sum"] == 15
        assert result["difference"] == 5
        assert result["product"] == 50
        assert result["quotient"] == 2
    
    @it("should demonstrate string operations in browser context")
    def test_browser_strings(self, page: Page):
        page.goto("about:blank")
        
        # Test string operations in JavaScript
        result = page.evaluate("""() => {
            const greeting = "Hello";
            const name = "Python";
            return {
                concatenated: greeting + " " + name,
                uppercase: greeting.toUpperCase(),
                lowercase: greeting.toLowerCase()
            };
        }""")
        
        assert result["concatenated"] == "Hello Python"
        assert result["uppercase"] == "HELLO"
        assert result["lowercase"] == "hello"
