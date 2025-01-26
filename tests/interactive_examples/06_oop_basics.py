"""
Python Object-Oriented Programming Basics Module

This module covers Python's OOP basics through practical examples:
- Classes and Objects
  * Class definition
  * Object instantiation
  * Attributes and methods
  * Constructor (__init__)
- Class Features
  * Instance methods
  * Class methods
  * Static methods
  * Properties
- Encapsulation
  * Private attributes
  * Name mangling
  * Property decorators
- Inheritance
  * Single inheritance
  * Method overriding
  * super() function
  * isinstance() and issubclass()

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time

@describe("Interactive Python OOP Basics")
class TestPythonOOPBasicsInteractive:
    
    @it("teaches about classes and objects")
    def test_classes_and_objects(self):
        print_section_header("Welcome to Python OOP - Part 1: Classes and Objects")
        print_info("Let's learn about Python's object-oriented programming basics.")
        time.sleep(1)

        # Question 1: Class definition
        print_subsection_header("Question 1: Class Definition")
        print_instruction("Look at this basic class definition:")
        print_code_block("""
            class Dog:
                # Class attribute (shared by all instances)
                species = "Canis familiaris"
                
                # Constructor method
                def __init__(self, name, age):
                    # Instance attributes (unique to each instance)
                    self.name = name
                    self.age = age
                
                # Instance method
                def bark(self):
                    return f"{self.name} says Woof!"
                
                # String representation
                def __str__(self):
                    return f"{self.name} is {self.age} years old"

            # Creating instances
            buddy = Dog("Buddy", 5)
            miles = Dog("Miles", 3)
                         """)
        answer = get_user_input("What method is called when creating a new instance of a class?")
        check_answer(
            answer,
            ['__init__', '__init__()'],
            "The __init__ method is the constructor, called when creating a new instance. It initializes the object's attributes."
        )

        # Question 2: Methods and attributes
        print_subsection_header("Question 2: Methods and Attributes")
        print_instruction("Look at these different types of methods:")
        print_code_block("""
            class Circle:
                # Class attribute
                pi = 3.14159
                
                def __init__(self, radius):
                    self.radius = radius  # Instance attribute
                
                # Instance method (uses self)
                def area(self):
                    return Circle.pi * self.radius ** 2
                
                # Class method (works with class attributes)
                @classmethod
                def from_diameter(cls, diameter):
                    return cls(diameter / 2)
                
                # Static method (doesn't use class or instance)
                @staticmethod
                def is_valid_radius(radius):
                    return radius > 0

            # Using different methods
            c1 = Circle(5)              # Regular constructor
            c2 = Circle.from_diameter(10)  # Class method
            valid = Circle.is_valid_radius(5)  # Static method
                         """)
        answer = get_user_input("What decorator is used to define a class method?")
        check_answer(
            answer,
            ['@classmethod', 'classmethod'],
            "The @classmethod decorator defines a class method, which receives the class as its first argument (cls)."
        )

        # Question 3: Special methods
        print_subsection_header("Question 3: Special Methods")
        print_instruction("Look at these special (magic) methods:")
        print_code_block("""
            class Point:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y
                
                # String representation for developers
                def __repr__(self):
                    return f"Point({self.x}, {self.y})"
                
                # String representation for users
                def __str__(self):
                    return f"Point at ({self.x}, {self.y})"
                
                # Equality comparison
                def __eq__(self, other):
                    if not isinstance(other, Point):
                        return NotImplemented
                    return self.x == other.x and self.y == other.y
                
                # Addition
                def __add__(self, other):
                    return Point(self.x + other.x, self.y + other.y)

            p1 = Point(1, 2)
            p2 = Point(3, 4)
            p3 = p1 + p2  # Uses __add__
                         """)
        answer = get_user_input("What special method provides a string representation when using print()?")
        check_answer(
            answer,
            ['__str__', '__str__()'],
            "The __str__ method provides a string representation for users (print). __repr__ is for developers/debugging."
        )

    @it("teaches about inheritance and encapsulation")
    def test_inheritance_encapsulation(self):
        print_section_header("Part 2: Inheritance and Encapsulation")
        print_info("Let's explore inheritance and encapsulation in Python.")
        time.sleep(1)

        # Question 1: Inheritance
        print_subsection_header("Question 1: Inheritance")
        print_instruction("Look at this inheritance example:")
        print_code_block("""
            class Animal:
                def __init__(self, name):
                    self.name = name
                
                def speak(self):
                    pass  # Base class method
                
                def introduce(self):
                    return f"I am {self.name}"

            class Dog(Animal):
                def speak(self):
                    return "Woof!"
                
                def introduce(self):
                    # Call parent class method
                    return super().introduce() + " and I'm a dog!"

            class Cat(Animal):
                def speak(self):
                    return "Meow!"

            # Using inheritance
            dog = Dog("Buddy")
            cat = Cat("Whiskers")
            
            # Method overriding in action
            print(dog.speak())      # "Woof!"
            print(cat.speak())      # "Meow!"
            print(dog.introduce())  # "I am Buddy and I'm a dog!"
                         """)
        answer = get_user_input("What function is used to call a method from the parent class?")
        check_answer(
            answer,
            ['super', 'super()', '.super', '.super()'],
            "The super() function allows you to call methods from the parent class, especially useful in method overriding."
        )

        # Question 2: Encapsulation
        print_subsection_header("Question 2: Encapsulation")
        print_instruction("Look at these encapsulation examples:")
        print_code_block("""
            class BankAccount:
                def __init__(self, owner, balance=0):
                    self._owner = owner          # Protected attribute
                    self.__balance = balance     # Private attribute
                
                @property
                def balance(self):
                    return self.__balance
                
                def deposit(self, amount):
                    if amount > 0:
                        self.__balance += amount
                        return True
                    return False
                
                def _validate_withdrawal(self, amount):
                    return amount > 0 and amount <= self.__balance
                
                def withdraw(self, amount):
                    if self._validate_withdrawal(amount):
                        self.__balance -= amount
                        return True
                    return False

            account = BankAccount("Alice", 1000)
            print(account.balance)        # Uses property getter
            account.deposit(500)          # Encapsulated modification
            account.withdraw(200)         # Encapsulated modification
                         """)
        answer = get_user_input("What prefix makes an attribute private in Python?")
        check_answer(
            answer,
            ['__', 'double underscore'],
            "Double underscore (__) prefix makes an attribute private through name mangling. Single underscore (_) is for protected attributes."
        )

        # Question 3: Properties
        print_subsection_header("Question 3: Properties")
        print_instruction("Look at these property examples:")
        print_code_block("""
            class Temperature:
                def __init__(self, celsius=0):
                    self._celsius = celsius
                
                @property
                def celsius(self):
                    return self._celsius
                
                @celsius.setter
                def celsius(self, value):
                    if value < -273.15:  # Absolute zero
                        raise ValueError("Temperature below absolute zero!")
                    self._celsius = value
                
                @property
                def fahrenheit(self):
                    return (self.celsius * 9/5) + 32
                
                @fahrenheit.setter
                def fahrenheit(self, value):
                    self.celsius = (value - 32) * 5/9

            # Using properties
            temp = Temperature(25)
            print(temp.celsius)     # Get celsius
            temp.fahrenheit = 100   # Set fahrenheit
            print(temp.celsius)     # Get new celsius
                         """)
        answer = get_user_input("What decorator is used to define a property getter?")
        check_answer(
            answer,
            ['@property', 'property'],
            "The @property decorator creates a property getter, allowing attribute-like access to methods."
        )

        print_success("🎉 Congratulations! You've completed the Python OOP basics lesson!")
        print_info("Key takeaways:")
        print_code_block("""
            # 1. Class Definition
            class MyClass:
                class_attr = "shared"     # Class attribute
                
                def __init__(self):       # Constructor
                    self.instance_attr = "unique"
                
                def method(self):         # Instance method
                    pass

            # 2. Inheritance
            class Child(Parent):
                def method(self):
                    super().method()      # Call parent method

            # 3. Encapsulation
            class Encapsulated:
                def __init__(self):
                    self._protected = "protected"  # Protected
                    self.__private = "private"    # Private
                
                @property
                def value(self):          # Property getter
                    return self.__private
                         """) 