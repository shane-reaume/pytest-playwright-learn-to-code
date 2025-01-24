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
        ("basics", base_cmd + ["tests/test_examples/test_01_basics.py"]),
        ("interactive_basics", base_cmd + ["tests/interactive_examples/01_basics.py"]),
        ("data_types", base_cmd + ["tests/test_examples/test_02_data_types.py"]),
        ("interactive_data_types", base_cmd + ["tests/interactive_examples/02_data_types.py"]),
        ("data_structures", base_cmd + ["tests/test_examples/test_03_data_structures.py"]),
        ("interactive_data_structures", base_cmd + ["tests/interactive_examples/03_data_structures.py"]),
        ("control_flow", base_cmd + ["tests/test_examples/test_04_control_flow.py"]),
        ("interactive_control_flow", base_cmd + ["tests/interactive_examples/04_control_flow.py"]),
        ("functions", base_cmd + ["tests/test_examples/test_05_functions.py"]),
        ("interactive_functions", base_cmd + ["tests/interactive_examples/05_functions.py"]),
        ("oop_basics", base_cmd + ["tests/test_examples/test_06_oop_basics.py"]),
        ("interactive_oop_basics", base_cmd + ["tests/interactive_examples/06_oop_basics.py"]),
        ("advanced_oop", base_cmd + ["tests/test_examples/test_07_advanced_oop.py"]),
        ("interactive_advanced_oop", base_cmd + ["tests/interactive_examples/07_advanced_oop.py"]),
        ("modules", base_cmd + ["tests/test_examples/test_08_modules_and_packages.py"]),
        ("interactive_modules", base_cmd + ["tests/interactive_examples/08_modules_and_packages.py"]),
        ("file_io", base_cmd + ["tests/test_examples/test_09_file_io.py"]),
        ("interactive_file_io", base_cmd + ["tests/interactive_examples/09_file_io.py"]),
        ("exceptions", base_cmd + ["tests/test_examples/test_10_exceptions_handling.py"]),
        ("interactive_exceptions", base_cmd + ["tests/interactive_examples/10_exceptions_handling.py"]),
        ("iterators", base_cmd + ["tests/test_examples/test_11_iterators_and_generators.py"]),
        ("interactive_iterators", base_cmd + ["tests/interactive_examples/11_iterators_and_generators.py"]),
        ("decorators", base_cmd + ["tests/test_examples/test_12_decorators_and_context_managers.py"]),
        ("interactive_decorators", base_cmd + ["tests/interactive_examples/12_decorators_and_context_managers.py"]),
        ("advanced", base_cmd + ["tests/test_examples/test_13_advanced_concepts.py"]),
        ("interactive_advanced", base_cmd + ["tests/interactive_examples/13_advanced_concepts.py"]),
        ("stdlib", base_cmd + ["tests/test_examples/test_14_standard_library_and_third_party.py"]),
        ("interactive_stdlib", base_cmd + ["tests/interactive_examples/14_standard_library_and_third_party.py"]),
        ("pytest_basics", base_cmd + ["tests/test_examples/test_15_pytest_basics.py"]),
        ("interactive_pytest", base_cmd + ["tests/interactive_examples/15_pytest_basics.py"]),
        ("playwright", base_cmd + ["tests/test_examples/test_16_playwright_integration.py"]),
        ("interactive_playwright", base_cmd + ["tests/interactive_examples/16_playwright_integration.py"]),
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