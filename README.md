# Python Learning and Testing with Pytest-Playwright

A project for learning Python concepts through test-driven development, using Playwright for browser automation and pytest as the test runner. This project serves as both a learning resource and a practical example of Python testing practices.

## Features

- **Python Learning Examples**: Comprehensive test examples covering Python fundamentals to advanced concepts
- **Playwright Integration**: Browser automation examples using Playwright
- **Test-Driven Learning**: Learn Python concepts through practical test cases
- **Minimal Dependencies**: Uses `pytest-playwright` for all testing needs

## Project Structure

```
pytest-playwright-learn-to-code/
├── tests/
│   ├── learn_examples/           # Python learning concept tests
│   │   ├── test_basics.py       # Basic Python concepts
│   │   ├── test_data_types.py   # Python data types
│   │   ├── test_control_flow.py # Control flow examples
│   │   ├── test_functions.py    # Function usage
│   │   ├── test_oop_basics.py   # Basic OOP concepts
│   │   └── ... more concept tests
│   └── conftest.py              # Shared fixtures and configurations
├── scripts.py                    # Test runner script
├── pytest.ini                    # Pytest configuration
└── requirements.txt              # Project dependencies
```

## Setup Requirements

### Common Requirements
- Python 3.8 or higher
- pip (Python package installer)
- Git

### OS-Specific Requirements

#### Linux (Debian/Ubuntu/Linux Mint)
1. Install Python and required system packages:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv git
   ```

2. Install additional dependencies for Playwright:
   ```bash
   sudo apt install libavif16
   ```

   Note: On some systems, you might need additional dependencies. If you encounter issues, run:
   ```bash
   sudo apt install libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 \
   libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2
   ```

#### macOS
1. Install Homebrew (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install Python:
   ```bash
   brew install python
   ```

#### Windows
1. Download and install Python from [python.org](https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"
   - Choose the option to install pip

2. Install Git from [git-scm.com](https://git-scm.com/download/win)

## Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/shane-reaume/pytest-playwright-learn-to-code.git
   cd pytest-playwright-learn-to-code
   ```

2. Create and activate a virtual environment:

   **Linux/macOS**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **Windows**:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:

   **Linux/macOS**:
   ```bash
   pip3 install -r requirements.txt
   ```

   **Windows**:
   ```cmd
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:

   **All Operating Systems**:
   ```bash
   playwright install
   ```

## Running Tests

Use the `scripts.py` command-line interface:

### Basic Usage

**Linux/macOS**:
```bash
python3 scripts.py run <test_name>
```

**Windows**:
```cmd
python scripts.py run <test_name>
```

### Available Test Commands

- Run all tests:
  ```bash
  python3 scripts.py run all  # Linux/macOS
  python scripts.py run all   # Windows
  ```

- Run all learning example tests:
  ```bash
  python3 scripts.py run learn_examples  # Linux/macOS
  python scripts.py run learn_examples   # Windows
  ```

### Test Options

Add these flags to any test command:

- `--headed`: Run tests in headed mode (visible browser)
  ```bash
  python3 scripts.py run all --headed  # Linux/macOS
  python scripts.py run all --headed   # Windows
  ```

- `--debug`: Run tests in debug mode (slower execution)
  ```bash
  python3 scripts.py run all --debug  # Linux/macOS
  python scripts.py run all --debug   # Windows
  ```

### Help

To see all available commands and options:
```bash
python3 scripts.py help  # Linux/macOS
python scripts.py help   # Windows
```

## Learning Path

The tests in the `learn_examples` directory are organized to follow a logical learning progression:

1. Python Basics (`test_basics.py`)
2. Data Types (`test_data_types.py`)
3. Control Flow (`test_control_flow.py`)
4. Functions (`test_functions.py`)
5. Object-Oriented Programming Basics (`test_oop_basics.py`)
6. Advanced OOP Concepts (`test_advanced_oop.py`)
7. Modules and Packages (`test_modules_and_packages.py`)
8. File I/O (`test_file_io.py`)
9. Exception Handling (`test_exceptions_handling.py`)
10. Advanced Concepts (`test_advanced_concepts.py`)
11. Decorators and Context Managers (`test_decorators_and_context_managers.py`)
12. Iterators and Generators (`test_iterators_and_generators.py`)
13. Standard Library and Third-Party Packages (`test_standard_library_and_third_party.py`)
14. Pytest Basics (`test_pytest_basics.py`)
15. Playwright Integration (`test_playwright_integration.py`)

Each test file contains examples and test cases that demonstrate the concepts in action.

## Troubleshooting

### Linux
- If you see "command not found: python", use `python3` instead
- If you encounter browser launch issues, make sure all system dependencies are installed
- For permission issues with `/usr/bin/env: 'python': No such file or directory`, try:
  ```bash
  sudo ln -s /usr/bin/python3 /usr/bin/python
  ```

### macOS
- If you see "command not found: python", try `python3` or reinstall Python using Homebrew
- For M1/M2 Macs, you might need Rosetta 2 for some browser features:
  ```bash
  softwareupdate --install-rosetta
  ```

### Windows
- If Python/pip is not recognized, verify that Python is added to PATH
- For permission issues, try running Command Prompt as Administrator
- If you see SSL errors, you might need to install certificates:
  ```cmd
  python -m pip install --upgrade certifi
  ```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 