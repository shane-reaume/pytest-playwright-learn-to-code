"""Test runner script"""
import sys
import subprocess
from pathlib import Path
import os
from collections import OrderedDict

def get_test_commands():
    """Get all available test commands"""
    # Get the path to pytest in the virtual environment
    if os.name == 'nt':  # Windows
        pytest_path = str(Path('venv/Scripts/pytest'))
    else:  # Linux/macOS
        pytest_path = str(Path('venv/bin/pytest'))
    
    # Add -s flag to show print statements
    base_cmd = [pytest_path, "-v", "-s"]
    test_dir = Path("tests")
    
    # Use OrderedDict to maintain the logical learning order
    commands = OrderedDict([
        ("all", base_cmd + ["tests"]),
        ("interactive", base_cmd + ["tests/interactive_examples"]),
        ("test_examples", base_cmd + ["tests/test_examples"]),
        
        # Individual concept tests in learning order
        ("01", base_cmd + ["tests/interactive_examples/01_basics.py"]),
        ("02", base_cmd + ["tests/interactive_examples/02_data_types.py"]),
        ("03", base_cmd + ["tests/interactive_examples/03_data_structures.py"]),
        ("04", base_cmd + ["tests/interactive_examples/04_control_flow.py"]),
        ("05", base_cmd + ["tests/interactive_examples/05_functions.py"]),
        ("06", base_cmd + ["tests/interactive_examples/06_oop_basics.py"]),
        ("07", base_cmd + ["tests/interactive_examples/07_advanced_oop.py"]),
        ("08", base_cmd + ["tests/interactive_examples/08_modules_and_packages.py"]),
        ("09", base_cmd + ["tests/interactive_examples/09_file_io.py"]),
        ("10", base_cmd + ["tests/interactive_examples/10_exceptions_handling.py"]),
        ("11", base_cmd + ["tests/interactive_examples/11_iterators_and_generators.py"]),
        ("12", base_cmd + ["tests/interactive_examples/12_decorators_and_context_managers.py"]),
        ("13", base_cmd + ["tests/interactive_examples/13_advanced_concepts.py"]),
        ("14", base_cmd + ["tests/interactive_examples/14_standard_library_and_third_party.py"]),
        ("15", base_cmd + ["tests/interactive_examples/15_pytest_basics.py"]),
        ("16", base_cmd + ["tests/interactive_examples/16_playwright_integration.py"]),
    ])
    return commands

def run_with_options(command, headed=False, debug=False):
    """Add optional parameters to any test command"""
    if headed:
        command.append("--headed")
    if debug:
        command.extend(["--slowmo", "1000"])
    try:
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print("Error: pytest not found. Make sure you have activated the virtual environment:")
        if os.name == 'nt':  # Windows
            print("  Run: .\\venv\\Scripts\\activate")
        else:  # Linux/macOS
            print("  Run: source venv/bin/activate")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running tests: {e}")
        sys.exit(1)

def print_help():
    """Print help message."""
    print("\nAvailable commands:")
    print("  run <test>      - Run specified test")
    print("  help           - Show this help message")
    print("\nAvailable tests:")
    print("  all            - Run all tests")
    print("  interactive    - Run all interactive learning tests")
    print("  test_examples  - Run all test examples")
    print("  basics         - Run basic Python concepts test")
    print("  data_types     - Run data types test")
    print("  ... and more individual tests")
    print("\nOptions:")
    print("  --headed       - Run in headed mode")
    print("  --debug        - Run in debug mode")

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if not args or args[0] == "help":
        print_help()
        sys.exit()

    # Parse options
    headed = "--headed" in args
    debug = "--debug" in args
    # Remove option flags from args
    args = [arg for arg in args if arg not in ["--headed", "--debug"]]

    if len(args) >= 2 and args[0] == "run":
        commands = get_test_commands()
        test_name = args[1]
        
        if test_name in commands:
            run_with_options(commands[test_name], headed, debug)
        else:
            print(f"Test '{test_name}' not found.")
            print(f"Available tests: {', '.join(commands.keys())}")
    else:
        print("Invalid command.")
        print_help()