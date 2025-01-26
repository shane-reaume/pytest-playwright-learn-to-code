"""
Python Advanced OOP Concepts Module

This module covers advanced OOP concepts through practical examples:
- Multiple Inheritance
  * Method Resolution Order (MRO)
  * Diamond problem
  * Mixins and composition
- Abstract Base Classes
  * abc module
  * Abstract methods
  * Interface definition
- Metaclasses
  * Class creation
  * Class customization
  * Class registration
- Design Patterns
  * Singleton pattern
  * Factory pattern
  * Observer pattern
  * Context managers

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time
from abc import ABC, abstractmethod

def get_mro_example():
    return '''
        class A:
            def method(self):
                return "A's method"

        class B(A):
            def method(self):
                return "B's method"

        class C(A):
            def method(self):
                return "C's method"

        class D(B, C):
            pass

        # Method Resolution Order
        print(D.__mro__)  
        # (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

        d = D()
        print(d.method())  # Calls B's method (first in MRO)
    '''

def get_mixin_example():
    return '''
        class JSONMixin:
            def to_json(self):
                import json
                return json.dumps(self.__dict__)

        class LoggerMixin:
            def log(self, message):
                print(f"[{self.__class__.__name__}] {message}")

        class User(JSONMixin, LoggerMixin):
            def __init__(self, name, email):
                self.name = name
                self.email = email
                self.log(f"Created user {name}")

        # Using mixin functionality
        user = User("Alice", "alice@example.com")
        print(user.to_json())  # Uses JSONMixin
        user.log("Logged in")  # Uses LoggerMixin
    '''

def get_abstract_example():
    return '''
        from abc import ABC, abstractmethod

        class Shape(ABC):
            @abstractmethod
            def area(self):
                pass

            @abstractmethod
            def perimeter(self):
                pass

        class Rectangle(Shape):
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height

            def perimeter(self):
                return 2 * (self.width + self.height)

        # This would raise TypeError:
        # shape = Shape()  # Can't instantiate abstract class
        
        rect = Rectangle(5, 3)
        print(rect.area())      # 15
        print(rect.perimeter()) # 16
    '''

def get_metaclass_example():
    return '''
        class SingletonMeta(type):
            _instances = {}
            
            def __call__(cls, *args, **kwargs):
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
                return cls._instances[cls]

        class Database(metaclass=SingletonMeta):
            def __init__(self):
                self.connected = False
            
            def connect(self):
                self.connected = True

        # Using singleton
        db1 = Database()
        db2 = Database()
        print(db1 is db2)  # True - same instance
    '''

def get_patterns_example():
    return '''
        # Factory Pattern
        class Animal:
            def speak(self):
                pass

        class Dog(Animal):
            def speak(self):
                return "Woof!"

        class Cat(Animal):
            def speak(self):
                return "Meow!"

        class AnimalFactory:
            @staticmethod
            def create_animal(animal_type):
                if animal_type == "dog":
                    return Dog()
                elif animal_type == "cat":
                    return Cat()
                raise ValueError(f"Unknown animal type {animal_type}")

        # Context Manager Pattern
        class FileManager:
            def __init__(self, filename):
                self.filename = filename
                self.file = None

            def __enter__(self):
                self.file = open(self.filename, 'w')
                return self.file

            def __exit__(self, exc_type, exc_val, exc_tb):
                if self.file:
                    self.file.close()

        # Using patterns
        factory = AnimalFactory()
        dog = factory.create_animal("dog")
        print(dog.speak())  # "Woof!"

        with FileManager("test.txt") as file:
            file.write("Hello, World!")
    '''

def get_key_takeaways():
    return '''
        # 1. Multiple Inheritance
        class Child(Parent1, Parent2):
            def method(self):
                super().method()  # MRO determines which parent

        # 2. Abstract Base Classes
        class Interface(ABC):
            @abstractmethod
            def method(self):
                pass

        # 3. Metaclasses
        class Meta(type):
            def __new__(cls, name, bases, attrs):
                # Customize class creation
                return super().__new__(cls, name, bases, attrs)

        # 4. Design Patterns
        class Singleton(metaclass=SingletonMeta):
            pass  # Only one instance ever exists
    '''

@describe("Interactive Python Advanced OOP")
class TestPythonAdvancedOOPInteractive:
    
    @it("teaches about multiple inheritance")
    def test_multiple_inheritance(self):
        print_section_header("Welcome to Advanced OOP - Part 1: Multiple Inheritance")
        print_info("Let's explore Python's multiple inheritance and method resolution.")
        time.sleep(1)

        # Question 1: Method Resolution Order
        print_subsection_header("Question 1: Method Resolution Order")
        print_instruction("Look at this multiple inheritance example:")
        print_code_block(get_mro_example())
        answer = get_user_input("What attribute shows a class's method resolution order?")
        check_answer(
            answer,
            ['__mro__', 'mro', '__mro'],
            "The __mro__ attribute shows the Method Resolution Order - the order Python searches for methods."
        )

        # Question 2: Mixins
        print_subsection_header("Question 2: Mixins")
        print_instruction("Look at these mixin examples:")
        print_code_block(get_mixin_example())
        answer = get_user_input("What is a common naming convention for mixin classes in Python?")
        check_answer(
            answer,
            ['Mixin', 'mixin suffix', 'suffix mixin', 'ends with mixin'],
            "Mixins are commonly named with the 'Mixin' suffix (e.g., LoggerMixin) to clearly indicate their purpose."
        )

    @it("teaches about abstract base classes")
    def test_abstract_classes(self):
        print_section_header("Part 2: Abstract Base Classes")
        print_info("Let's learn about abstract classes and interfaces in Python.")
        time.sleep(1)

        # Question 1: Abstract Methods
        print_subsection_header("Question 1: Abstract Methods")
        print_instruction("Look at this abstract class example:")
        print_code_block(get_abstract_example())
        answer = get_user_input("What decorator marks a method as abstract?")
        check_answer(
            answer,
            ['@abstractmethod', 'abstractmethod'],
            "The @abstractmethod decorator marks methods that must be implemented by concrete subclasses."
        )

    @it("teaches about metaclasses and patterns")
    def test_metaclasses_patterns(self):
        print_section_header("Part 3: Metaclasses and Design Patterns")
        print_info("Let's explore metaclasses and common design patterns.")
        time.sleep(1)

        # Question 1: Metaclasses
        print_subsection_header("Question 1: Metaclasses")
        print_instruction("Look at this metaclass example:")
        print_code_block(get_metaclass_example())
        answer = get_user_input("What parameter is used to specify a class's metaclass?")
        check_answer(
            answer,
            ['metaclass', 'metaclass='],
            "The metaclass parameter in the class definition specifies which metaclass to use."
        )

        # Question 2: Design Patterns
        print_subsection_header("Question 2: Design Patterns")
        print_instruction("Look at these design pattern examples:")
        print_code_block(get_patterns_example())
        answer = get_user_input("What two special methods are required to create a context manager?")
        check_answer(
            answer,
            ['__enter__ and __exit__', '__enter__, __exit__', '__enter__ __exit__'],
            "The __enter__ and __exit__ methods are required to create a context manager for use with 'with' statements."
        )

        print_success("🎉 Congratulations! You've completed the Advanced OOP lesson!")
        print_info("Key takeaways:")
        print_code_block(get_key_takeaways()) 