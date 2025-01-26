"""
Python File I/O Learning Module

This module covers Python's file handling through practical test examples:
- Basic File Operations
  * Opening and closing files
  * Reading files (read, readline, readlines)
  * Writing files (write, writelines)
  * File modes (r, w, a, b, +)
- File System Operations
  * os module for file operations
  * pathlib for modern path handling
  * Directory operations
  * File metadata
- Working with Paths
  * Absolute vs relative paths
  * Path manipulation
  * Path existence and permissions
- Text vs Binary Files
  * Text file handling
  * Binary file operations
  * Encoding and decoding
- Data Serialization
  * JSON reading/writing
  * CSV handling
  * Pickle for Python objects
- Best Practices
  * Context managers for files
  * Error handling
  * Performance considerations
  * Platform independence

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time

def get_file_basics():
    return '''
        # Basic file operations
        with open('example.txt', 'r') as file:
            content = file.read()  # Read entire file
            
        with open('output.txt', 'w') as file:
            file.write("Hello, World!")  # Write string
            
        # Reading line by line
        with open('data.txt', 'r') as file:
            for line in file:
                print(line.strip())
                
        # Common file modes
        'r'  # Read (default)
        'w'  # Write (truncates)
        'a'  # Append
        'x'  # Exclusive creation
        'b'  # Binary mode
        't'  # Text mode (default)
        '+'  # Read and write
    '''

def get_advanced_operations():
    return '''
        # Binary file operations
        with open('image.png', 'rb') as file:
            header = file.read(8)  # Read first 8 bytes
            
        with open('data.bin', 'wb') as file:
            file.write(bytes([0x41, 0x42, 0x43]))
            
        # Text encoding
        with open('unicode.txt', 'w', encoding='utf-8') as file:
            file.write('Hello, 世界!')
            
        # File seeking
        with open('data.txt', 'r') as file:
            file.seek(10)      # Move to position 10
            file.seek(0, 2)    # Move to end (whence=2)
            file.tell()        # Get current position
    '''

def get_path_operations():
    return '''
        from pathlib import Path
        
        # Path manipulation
        path = Path('folder/subfolder/file.txt')
        print(path.parent)     # Parent directory
        print(path.name)       # File name
        print(path.suffix)     # File extension
        print(path.stem)       # Name without extension
        
        # Creating paths
        new_path = Path.home() / 'documents' / 'file.txt'
        
        # Directory operations
        path = Path('my_directory')
        path.mkdir(parents=True, exist_ok=True)
        
        # Iterating over files
        for file_path in Path('.').glob('*.py'):
            print(file_path)
    '''

def get_file_patterns():
    return '''
        # Common file patterns
        def process_large_file(filename):
            """Process a large file line by line."""
            with open(filename, 'r') as file:
                for line in file:
                    yield line.strip()
                    
        # CSV file handling
        import csv
        with open('data.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
                
        # JSON file handling
        import json
        with open('config.json', 'r') as file:
            data = json.load(file)
            
        with open('output.json', 'w') as file:
            json.dump(data, file, indent=4)
    '''

def get_key_takeaways():
    return '''
        # 1. Basic File Operations
        with open(file, mode) as f:
            content = f.read()     # Read
            f.write(data)          # Write
            
        # 2. Path Operations
        from pathlib import Path
        path = Path('file.txt')
        path.exists()
        path.mkdir()
        
        # 3. Common Patterns
        for line in file:          # Line by line
        json.load(file)            # JSON
        csv.DictReader(file)       # CSV
    '''

@describe("Interactive Python File Operations")
class TestPythonFileOperationsInteractive:
    
    @it("teaches about basic file operations")
    def test_file_basics(self):
        print_section_header("Welcome to File Operations - Part 1: File Basics")
        print_info("Let's explore Python's file handling system.")
        time.sleep(1)

        # Question 1: File Modes
        print_subsection_header("Question 1: File Modes")
        print_instruction("Look at these file operation examples:")
        print_code_block(get_file_basics())
        answer = get_user_input("What mode opens a file for writing and truncates it if it exists?")
        check_answer(
            answer,
            ['w', 'write', 'w mode'],
            "The 'w' mode opens a file for writing and truncates (empties) it if it exists."
        )

        # Question 2: Context Managers
        print_subsection_header("Question 2: Context Managers")
        answer = get_user_input("What statement is used for automatic file closing in Python?")
        check_answer(
            answer,
            ['with', 'with statement'],
            "The 'with' statement is used as a context manager to automatically close files."
        )

    @it("teaches about advanced file operations")
    def test_advanced_operations(self):
        print_section_header("Part 2: Advanced File Operations")
        print_info("Let's learn about advanced file handling techniques.")
        time.sleep(1)

        # Question 1: Binary Files
        print_subsection_header("Question 1: Binary Files")
        print_instruction("Look at these advanced file operations:")
        print_code_block(get_advanced_operations())
        answer = get_user_input("What mode suffix is used to open a file in binary mode?")
        check_answer(
            answer,
            ['b', 'binary', 'b mode'],
            "The 'b' suffix (e.g., 'rb', 'wb') is used to open files in binary mode."
        )

        # Question 2: File Position
        print_subsection_header("Question 2: File Position")
        answer = get_user_input("What method is used to move the file cursor to a specific position?")
        check_answer(
            answer,
            ['seek', 'seek()', 'file.seek'],
            "The seek() method is used to move the file cursor to a specific position."
        )

    @it("teaches about file system operations")
    def test_file_system_operations(self):
        print_section_header("Part 3: File System Operations")
        print_info("Let's explore file system operations using pathlib.")
        time.sleep(1)

        # Question 1: Path Operations
        print_subsection_header("Question 1: Path Operations")
        print_instruction("Look at these path operation examples:")
        print_code_block(get_path_operations())
        answer = get_user_input("What class from pathlib is used for path manipulation in Python 3?")
        check_answer(
            answer,
            ['Path', 'Path class'],
            "The Path class from pathlib provides an object-oriented interface to filesystem paths."
        )

        # Question 2: File Patterns
        print_subsection_header("Question 2: File Patterns")
        print_instruction("Look at these common file patterns:")
        print_code_block(get_file_patterns())
        answer = get_user_input("What parameter in open() ensures consistent newline handling across platforms?")
        check_answer(
            answer,
            ['newline', 'newline parameter'],
            "The newline='' parameter ensures consistent newline handling across different platforms."
        )

        print_success("🎉 Congratulations! You've completed the File Operations lesson!")
        print_info("Key takeaways:")
        print_code_block(get_key_takeaways()) 