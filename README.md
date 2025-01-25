# Python Learning and Testing with Pytest-Playwright

🚧 **Work in Progress** 🚧

This is an evolving project that explores innovative ways to learn Python interactively, specifically targeting Python QA engineers and developers who want to learn pytest. The project combines fun interactive learning with real-world testing scenarios.

## Template repo for creating your own pytest-playwright project

- [pytest-playwright-template](https://github.com/shane-reaume/pytest-playwright-template)
- This framework is built on top of the [pytest-playwright](https://github.com/microsoft/playwright-pytest) project, recommended by Playwright.
- We customized syntax with `describe` and `it` to make it more readable and easier to understand for those coming from other JavaScript based testing frameworks.

## Features

- **Interactive Learning**: Learn Python through interactive CLI-based lessons
  * Syntax highlighting with customizable themes
  * Clear, consistent formatting for better readability
  * Immediate feedback on exercises
  * Progress tracking and key takeaways
- **Python Learning Examples**: Comprehensive test examples covering Python fundamentals to advanced concepts
- **Playwright Integration**: Browser automation examples using Playwright
- **Test-Driven Learning**: Learn Python concepts through practical test cases
- **Modern Python Setup**: Uses `pyproject.toml` for dependency management and configuration
- **Code Quality Tools**: Integrated Ruff for linting and code formatting

## Project Structure

```
pytest-playwright-learn-to-code/
├── tests/
│   ├── interactive_examples/    # Interactive learning modules
│   │   ├── 01_basics.py        # Interactive Python basics
│   │   └── ... more lessons
│   ├── test_examples/          # Real-world test examples
│   │   ├── test_01_basics.py   # Basic Python concepts
│   │   ├── test_02_data_types.py
│   │   └── ... more examples
│   └── conftest.py            # Shared fixtures and configurations
├── scripts.py                  # Test runner script
├── pyproject.toml             # Project configuration and dependencies
└── README.md                  # Project documentation
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

3. Install the project with development dependencies:

   **Linux/macOS**:
   ```bash
   pip3 install -e ".[dev]"
   ```

   **Windows**:
   ```cmd
   pip install -e ".[dev]"
   ```

4. Install Playwright browsers:
   ```bash
   playwright install
   ```

## Development Tools

### Code Quality

The project uses Ruff for linting and code formatting. Ruff is automatically installed with the development dependencies.

To run Ruff:
```bash
ruff check .     # Check for issues
ruff format .    # Format code
```

## Running Tests

Use the `scripts.py` command-line interface:

### Available Commands

- Run all tests:
  ```bash
  python3 scripts.py run all
  ```

- Run interactive lessons:
  ```bash
  python3 scripts.py run interactive
  ```

- Run test examples:
  ```bash
  python3 scripts.py run test_examples
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

## Learning Paths

### Interactive Learning (Recommended for Beginners)

Start with the interactive learning path for a hands-on experience:

```bash
# Run the interactive Python basics lesson
python3 scripts.py run interactive_basics  # Linux/macOS
python scripts.py run interactive_basics   # Windows

# Run all interactive lessons
python3 scripts.py run interactive         # Linux/macOS
python scripts.py run interactive          # Windows
```

The interactive lessons will:
- Present concepts one at a time
- Ask you questions about what you're learning
- Provide immediate feedback
- Give helpful explanations
- Show key takeaways at the end of each lesson

#### Theme Selection

When you start your first interactive lesson, you'll be prompted to choose a syntax highlighting theme. Available themes include:
- Monokai (default) - Dark theme with vibrant colors
- One Dark - Atom-inspired dark theme
- Solarized (dark/light) - Popular theme with carefully chosen colors
- Dracula - Modern dark theme
- Gruvbox (dark/light) - Retro groove theme
- Nord - Arctic-inspired dark theme
- VS - Visual Studio-inspired light theme
- Zenburn - Low contrast dark theme

Your theme choice persists across all interactive lessons in the same session, providing a consistent learning experience.

### Test Examples

The `test_examples` directory contains real-world testing scenarios that demonstrate both Python concepts and testing practices:

1. Python Basics (`test_01_basics.py`)
2. Data Types (`test_02_data_types.py`)
3. Control Flow (`test_03_control_flow.py`)
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

Each test file contains practical examples and test cases that demonstrate both Python concepts and testing best practices in action.

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