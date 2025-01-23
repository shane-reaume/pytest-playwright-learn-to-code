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
        ("learn_examples", base_cmd + ["tests/learn_examples"]),
        # Individual concept tests in learning order
        ("basics", base_cmd + ["tests/learn_examples/test_01_basics.py"]),
        ("data_types", base_cmd + ["tests/learn_examples/test_02_data_types.py"]),
        ("data_structures", base_cmd + ["tests/learn_examples/test_03_data_structures.py"]),
        ("control_flow", base_cmd + ["tests/learn_examples/test_04_control_flow.py"]),
        ("functions", base_cmd + ["tests/learn_examples/test_05_functions.py"]),
        ("oop_basics", base_cmd + ["tests/learn_examples/test_06_oop_basics.py"]),
        ("advanced_oop", base_cmd + ["tests/learn_examples/test_07_advanced_oop.py"]),
        ("modules", base_cmd + ["tests/learn_examples/test_08_modules_and_packages.py"]),
        ("file_io", base_cmd + ["tests/learn_examples/test_09_file_io.py"]),
        ("exceptions", base_cmd + ["tests/learn_examples/test_10_exceptions_handling.py"]),
        ("iterators", base_cmd + ["tests/learn_examples/test_11_iterators_and_generators.py"]),
        ("decorators", base_cmd + ["tests/learn_examples/test_12_decorators_and_context_managers.py"]),
        ("advanced", base_cmd + ["tests/learn_examples/test_13_advanced_concepts.py"]),
        ("stdlib", base_cmd + ["tests/learn_examples/test_14_standard_library_and_third_party.py"]),
        ("pytest_basics", base_cmd + ["tests/learn_examples/test_15_pytest_basics.py"]),
        ("playwright", base_cmd + ["tests/learn_examples/test_16_playwright_integration.py"]),
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
    """Print usage instructions"""
    commands = get_test_commands()
    print("\nUsage: python3 scripts.py run <test_name>")
    print("\nAvailable test names (in recommended learning order):")
    # Skip the first two general commands
    for i, (name, _) in enumerate(list(commands.items())[2:], 1):
        print(f"  {i:2d}. {name}")
    print("\nOther commands:")
    print("  all            - Run all tests")
    print("  learn_examples - Run all learning example tests")
    print("\nOptions:")
    print("  --headed      - Run in headed mode")
    print("  --debug       - Run in debug mode (slow)")
    print("\nNote: Make sure to activate the virtual environment first:")
    if os.name == 'nt':  # Windows
        print("  Run: .\\venv\\Scripts\\activate")
    else:  # Linux/macOS
        print("  Run: source venv/bin/activate")

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