"""
Python Standard Library and Third-Party Packages Learning Module

This module covers Python's standard library and package management through practical test examples:
- Standard Library Highlights
  * collections module
  * datetime and time
  * functools
  * itertools
  * re (regular expressions)
  * json and csv
- Package Management
  * pip usage
  * requirements.txt
  * setup.py
  * Virtual environments
- Popular Third-Party Packages
  * requests for HTTP
  * pytest for testing
  * numpy basics
  * pandas introduction
- Environment Management
  * venv module
  * Environment variables
  * Configuration management
  * Dependencies
- Best Practices
  * Package versioning
  * Dependency management
  * Security considerations
  * Documentation standards

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time
from collections import defaultdict, Counter, namedtuple
from datetime import datetime, timedelta
from functools import partial, reduce
import itertools
import re
import json
import csv
import os
import subprocess

def get_collections_examples():
    return '''
        from collections import defaultdict, Counter, namedtuple

        # defaultdict example
        word_lengths = defaultdict(int)
        for word in ["hello", "world", "python"]:
            word_lengths[len(word)] += 1
        print(word_lengths)  # defaultdict(<class 'int'>, {5: 2, 6: 1})

        # Counter example
        colors = ["red", "blue", "red", "green", "blue", "blue"]
        color_count = Counter(colors)
        print(color_count)  # Counter({'blue': 3, 'red': 2, 'green': 1})
        print(color_count.most_common(2))  # [('blue', 3), ('red', 2)]

        # namedtuple example
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(11, y=22)
        print(p.x, p.y)  # 11 22
        print(p._replace(x=33))  # Point(x=33, y=22)
    '''

def get_datetime_examples():
    return '''
        from datetime import datetime, timedelta

        # Current date and time
        now = datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))

        # Date arithmetic
        tomorrow = now + timedelta(days=1)
        print(f"Tomorrow: {tomorrow.date()}")

        # Parsing dates
        date_str = "2024-03-15 14:30:00"
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        print(f"Parsed: {parsed_date}")

        # Time zones
        from datetime import timezone
        utc_now = datetime.now(timezone.utc)
        print(f"UTC: {utc_now}")
    '''

def get_itertools_examples():
    return '''
        import itertools

        # Infinite iterators
        counter = itertools.count(start=1, step=2)
        print(list(itertools.islice(counter, 5)))  # [1, 3, 5, 7, 9]

        # Combinatoric iterators
        letters = ['A', 'B', 'C']
        print(list(itertools.permutations(letters, 2)))
        print(list(itertools.combinations(letters, 2)))

        # Chain multiple iterables
        numbers = [1, 2, 3]
        letters = ['a', 'b', 'c']
        combined = itertools.chain(numbers, letters)
        print(list(combined))  # [1, 2, 3, 'a', 'b', 'c']

        # Grouping
        data = [("A", 1), ("A", 2), ("B", 1), ("B", 2)]
        for key, group in itertools.groupby(data, lambda x: x[0]):
            print(f"{key}: {list(group)}")
    '''

def get_regex_examples():
    return '''
        import re

        # Pattern matching
        text = "The year is 2024, the month is 03"
        pattern = r'\\d+'
        numbers = re.findall(pattern, text)
        print(numbers)  # ['2024', '03']

        # Email validation
        email_pattern = r'^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$'
        emails = ['user@example.com', 'invalid.email@', 'another@domain.co.uk']
        for email in emails:
            is_valid = bool(re.match(email_pattern, email))
            print(f"{email}: {is_valid}")

        # String substitution
        text = "Hello #name#! How are you?"
        replaced = re.sub(r'#name#', 'Alice', text)
        print(replaced)  # "Hello Alice! How are you?"

        # Groups and capturing
        log = "2024-03-15 14:30:45 - ERROR: Database connection failed"
        pattern = r'(\\d{4}-\\d{2}-\\d{2}) (\\d{2}:\\d{2}:\\d{2}) - (\\w+): (.+)'
        match = re.match(pattern, log)
        if match:
            date, time, level, message = match.groups()
            print(f"Date: {date}, Level: {level}")
    '''

def get_json_csv_examples():
    return '''
        import json
        import csv

        # JSON handling
        data = {
            'name': 'Alice',
            'age': 30,
            'skills': ['Python', 'SQL', 'Git']
        }
        
        # Writing JSON
        json_str = json.dumps(data, indent=2)
        print(json_str)
        
        # Reading JSON
        parsed_data = json.loads(json_str)
        print(parsed_data['skills'])

        # CSV handling
        csv_data = [
            ['Name', 'Age', 'City'],
            ['Alice', '30', 'New York'],
            ['Bob', '25', 'London']
        ]
        
        # Writing CSV
        with open('example.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)
        
        # Reading CSV
        with open('example.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
    '''

def get_package_management():
    return '''
        # requirements.txt example
        """
        requests==2.31.0
        pytest>=7.0.0
        numpy~=1.24.0
        """

        # setup.py example
        """
        from setuptools import setup, find_packages

        setup(
            name="myproject",
            version="0.1.0",
            packages=find_packages(),
            install_requires=[
                'requests>=2.31.0',
                'pytest>=7.0.0',
            ],
        )
        """

        # Virtual environment commands
        """
        # Creating a virtual environment
        python -m venv myenv

        # Activating (Unix/macOS)
        source myenv/bin/activate

        # Activating (Windows)
        myenv\\Scripts\\activate

        # Installing packages
        pip install -r requirements.txt

        # Freezing dependencies
        pip freeze > requirements.txt
        """
    '''

def get_third_party_examples():
    return '''
        # requests example
        import requests

        response = requests.get('https://api.github.com')
        if response.status_code == 200:
            data = response.json()
            print(f"GitHub API version: {data['current_user_url']}")

        # pytest example
        def test_addition():
            assert 1 + 1 == 2
            assert sum([1, 2, 3]) == 6

        # numpy example
        import numpy as np

        arr = np.array([1, 2, 3, 4, 5])
        print(f"Mean: {arr.mean()}")
        print(f"Standard deviation: {arr.std()}")

        # pandas example
        import pandas as pd

        df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'London', 'Paris']
        })
        print(df.describe())
    '''

def get_environment_management():
    return '''
        import os
        from pathlib import Path
        import configparser

        # Environment variables
        os.environ['APP_ENV'] = 'development'
        debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'

        # Configuration management
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'DatabaseHost': 'localhost',
            'DatabasePort': '5432'
        }

        # Path handling
        base_dir = Path(__file__).parent
        config_file = base_dir / 'config.ini'
        
        # Virtual environment detection
        in_venv = sys.prefix != sys.base_prefix
    '''

def get_key_takeaways():
    return '''
        # 1. Collections
        defaultdict(type)              # Auto-initializing dict
        Counter(iterable)              # Count occurrences
        namedtuple('Name', fields)     # Lightweight object

        # 2. Date and Time
        datetime.now()                 # Current time
        timedelta(days=1)             # Time arithmetic

        # 3. Regular Expressions
        re.match(pattern, string)      # Match at start
        re.findall(pattern, string)    # Find all matches

        # 4. Package Management
        pip install package            # Install package
        python -m venv env            # Create virtual env
        requirements.txt              # Dependency list
    '''

@describe("Interactive Python Standard Library and Third-Party Packages")
class TestPythonStandardLibraryInteractive:
    
    @it("teaches about collections module")
    def test_collections(self):
        print_section_header("Welcome to Standard Library - Part 1: Collections")
        print_info("Let's explore Python's collections module.")
        time.sleep(1)

        # Question 1: Collections
        print_subsection_header("Question 1: Collections Types")
        print_instruction("Look at these collections examples:")
        print_code_block(get_collections_examples())
        answer = get_user_input("Which collection type automatically initializes new keys with a default value?")
        check_answer(
            answer,
            ['defaultdict', 'collections.defaultdict'],
            "defaultdict automatically initializes new keys with the specified default type."
        )

    @it("teaches about datetime and time")
    def test_datetime(self):
        print_section_header("Part 2: Date and Time")
        print_info("Let's learn about handling dates and times.")
        time.sleep(1)

        # Question 1: Date Formatting
        print_subsection_header("Question 1: Date Formatting")
        print_instruction("Look at these datetime examples:")
        print_code_block(get_datetime_examples())
        answer = get_user_input("What class is used for date/time arithmetic in Python?")
        check_answer(
            answer,
            ['timedelta', 'datetime.timedelta'],
            "timedelta is used for performing arithmetic operations with dates and times."
        )

    @it("teaches about itertools")
    def test_itertools(self):
        print_section_header("Part 3: Itertools")
        print_info("Let's explore Python's itertools module.")
        time.sleep(1)

        # Question 1: Itertools Functions
        print_subsection_header("Question 1: Itertools Functions")
        print_instruction("Look at these itertools examples:")
        print_code_block(get_itertools_examples())
        answer = get_user_input("Which itertools function combines multiple iterables into one?")
        check_answer(
            answer,
            ['chain', 'itertools.chain'],
            "chain() combines multiple iterables into a single iterator."
        )

    @it("teaches about regular expressions")
    def test_regex(self):
        print_section_header("Part 4: Regular Expressions")
        print_info("Let's learn about pattern matching with regex.")
        time.sleep(1)

        # Question 1: Regex Patterns
        print_subsection_header("Question 1: Regex Patterns")
        print_instruction("Look at these regex examples:")
        print_code_block(get_regex_examples())
        answer = get_user_input("Which regex function finds all non-overlapping matches in a string?")
        check_answer(
            answer,
            ['findall', 're.findall'],
            "re.findall() finds all non-overlapping matches of a pattern in a string."
        )

    @it("teaches about JSON and CSV")
    def test_json_csv(self):
        print_section_header("Part 5: JSON and CSV")
        print_info("Let's explore handling structured data formats.")
        time.sleep(1)

        # Question 1: JSON Operations
        print_subsection_header("Question 1: JSON Operations")
        print_instruction("Look at these JSON and CSV examples:")
        print_code_block(get_json_csv_examples())
        answer = get_user_input("What function converts a Python object to a JSON string?")
        check_answer(
            answer,
            ['dumps', 'json.dumps'],
            "json.dumps() converts a Python object to a JSON-formatted string."
        )

    @it("teaches about package management")
    def test_package_management(self):
        print_section_header("Part 6: Package Management")
        print_info("Let's learn about Python package management.")
        time.sleep(1)

        # Question 1: Virtual Environments
        print_subsection_header("Question 1: Virtual Environments")
        print_instruction("Look at these package management examples:")
        print_code_block(get_package_management())
        answer = get_user_input("What command creates a new virtual environment?")
        check_answer(
            answer,
            ['python -m venv', 'python -m venv .', 'python -m venv myenv'],
            "python -m venv creates a new virtual environment."
        )

        print_success("🎉 Congratulations! You've completed the Standard Library and Package Management lesson!")
        print_info("Key takeaways:")
        print_code_block(get_key_takeaways()) 