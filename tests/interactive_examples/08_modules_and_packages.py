"""
Python Modules and Packages Module

This module covers Python's module system through practical examples:
- Module Basics
  * Import statements
  * Module search path
  * Module reloading
  * Module patterns
- Package Structure
  * __init__.py files
  * Subpackages
  * Relative imports
  * Namespace packages
- Import Mechanics
  * Import hooks
  * Lazy imports
  * Circular imports
  * Import caching
- Best Practices
  * Module organization
  * Package distribution
  * Version management
  * Documentation

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time

def get_import_examples():
    return '''
        # Basic imports
        import math
        print(math.pi)  # Using qualified name

        # Import specific names
        from datetime import datetime, timedelta
        now = datetime.now()

        # Import with alias
        import numpy as np
        array = np.array([1, 2, 3])

        # Import all names (not recommended)
        from math import *  # Imports everything

        # Conditional imports
        try:
            import json
        except ImportError:
            import simplejson as json
    '''

def get_module_patterns():
    return '''
        # module.py
        """Main module docstring."""

        # Module-level constants
        VERSION = "1.0.0"
        DEFAULT_CONFIG = {
            "timeout": 30,
            "retries": 3
        }

        # Module initialization
        def initialize():
            """Set up module resources."""
            pass

        # Public API
        def public_function():
            """Documented public function."""
            pass

        # Internal helpers
        def _internal_helper():
            """Helper function not meant for direct use."""
            pass

        # Main execution
        if __name__ == "__main__":
            initialize()
            public_function()
    '''

def get_package_structure():
    return '''
        mypackage/
        ├── __init__.py
        ├── module1.py
        ├── module2.py
        └── subpackage/
            ├── __init__.py
            └── module3.py

        # __init__.py
        """Package initialization and exports."""

        # Version and metadata
        __version__ = "1.0.0"
        __author__ = "Your Name"

        # Import key functionality
        from .module1 import function1
        from .module2 import function2

        # Define package-level variables
        package_config = {}

        # Initialize the package
        def initialize():
            pass

        # Clean up resources
        def cleanup():
            pass
    '''

def get_import_types():
    return '''
        # Absolute imports (from project root)
        from mypackage.module1 import function1
        from mypackage.subpackage.module3 import function3

        # Relative imports (from current location)
        # In mypackage/subpackage/module3.py:
        from .. import module1  # Go up one level
        from ..module2 import function2  # Go up and select
        from . import module3  # Current directory

        # Optional imports
        try:
            import optional_module
        except ImportError:
            optional_module = None

        # Lazy imports (inside function)
        def process_image():
            from PIL import Image  # Only imported when needed
            return Image.open('photo.jpg')
    '''

def get_setup_example():
    return '''
        from setuptools import setup, find_packages

        setup(
            name="mypackage",
            version="1.0.0",
            author="Your Name",
            author_email="your.email@example.com",
            description="A short description",
            long_description=open("README.md").read(),
            long_description_content_type="text/markdown",
            url="https://github.com/username/mypackage",
            packages=find_packages(),
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
            python_requires=">=3.6",
            install_requires=[
                "requests>=2.25.1",
                "pandas>=1.2.0",
            ],
            extras_require={
                "dev": ["pytest>=6.0", "black", "mypy"],
                "docs": ["sphinx", "sphinx-rtd-theme"],
            }
        )
    '''

def get_venv_examples():
    return '''
        # Creating virtual environments
        python -m venv myenv              # Create new environment
        source myenv/bin/activate         # Activate (Unix)
        myenv\\Scripts\\activate.bat       # Activate (Windows)
        deactivate                        # Deactivate current env

        # Installing packages
        pip install package_name          # Install latest version
        pip install package_name==1.2.3   # Install specific version
        pip install -r requirements.txt   # Install from file
        pip install -e .                  # Install current package

        # Managing requirements
        pip freeze > requirements.txt     # Save current packages
        pip list                         # List installed packages
        pip show package_name            # Show package details
    '''

def get_key_takeaways():
    return '''
        # 1. Module Imports
        import module                 # Basic import
        from module import name       # Import specific name
        from . import module         # Relative import
        
        # 2. Package Structure
        mypackage/
        ├── __init__.py              # Makes it a package
        └── subpackage/
            └── __init__.py          # Subpackage marker
        
        # 3. Distribution
        setup(
            name="package",
            version="1.0.0",
            packages=find_packages(),
            install_requires=[...]    # Dependencies
        )
    '''

@describe("Interactive Python Modules and Packages")
class TestPythonModulesPackagesInteractive:
    
    @it("teaches about module basics")
    def test_module_basics(self):
        print_section_header("Welcome to Python Modules - Part 1: Module Basics")
        print_info("Let's learn about Python's module system.")
        time.sleep(1)

        # Question 1: Import statements
        print_subsection_header("Question 1: Import Statements")
        print_instruction("Look at these import examples:")
        print_code_block(get_import_examples())
        answer = get_user_input("What keyword is used to rename a module when importing?")
        check_answer(
            answer,
            ['as', 'as keyword'],
            "The 'as' keyword allows you to create an alias for imported modules or names."
        )

        # Question 2: Module patterns
        print_subsection_header("Question 2: Module Patterns")
        print_instruction("Look at these module patterns:")
        print_code_block(get_module_patterns())
        answer = get_user_input("What special variable is used to detect if a module is run directly?")
        check_answer(
            answer,
            ['__name__', '__name__ variable'],
            "The __name__ variable is '__main__' when the module is run directly, and the module's name when imported."
        )

    @it("teaches about package structure")
    def test_package_structure(self):
        print_section_header("Part 2: Package Structure")
        print_info("Let's explore how Python packages are organized.")
        time.sleep(1)

        # Question 1: Package initialization
        print_subsection_header("Question 1: Package Initialization")
        print_instruction("Look at this package structure:")
        print_code_block(get_package_structure())
        answer = get_user_input("What file makes a directory a Python package?")
        check_answer(
            answer,
            ['__init__.py', 'init.py'],
            "The __init__.py file marks a directory as a Python package. It can be empty or contain initialization code."
        )

        # Question 2: Import types
        print_subsection_header("Question 2: Import Types")
        print_instruction("Look at these import examples:")
        print_code_block(get_import_types())
        answer = get_user_input("What symbol represents the current package in relative imports?")
        check_answer(
            answer,
            ['.', 'dot', 'period'],
            "A single dot (.) represents the current package, while two dots (..) go up one level."
        )

    @it("teaches about package distribution")
    def test_package_distribution(self):
        print_section_header("Part 3: Package Distribution")
        print_info("Let's learn about distributing Python packages.")
        time.sleep(1)

        # Question 1: Package metadata
        print_subsection_header("Question 1: Package Metadata")
        print_instruction("Look at this setup.py example:")
        print_code_block(get_setup_example())
        answer = get_user_input("What function automatically finds all packages in your project?")
        check_answer(
            answer,
            ['find_packages', 'find_packages()'],
            "find_packages() from setuptools automatically discovers all packages in your project directory."
        )

        # Question 2: Virtual Environments
        print_subsection_header("Question 2: Virtual Environments")
        print_instruction("Look at these virtual environment commands:")
        print_code_block(get_venv_examples())
        answer = get_user_input("What command creates a new virtual environment in Python?")
        check_answer(
            answer,
            ['python -m venv', 'venv'],
            "The command 'python -m venv' creates a new virtual environment. The venv module is included with Python 3."
        )

        print_success("🎉 Congratulations! You've completed the Python Modules and Packages lesson!")
        print_info("Key takeaways:")
        print_code_block(get_key_takeaways()) 