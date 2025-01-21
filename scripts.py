"""Test runner script"""
import sys
import subprocess
from pathlib import Path

def get_test_commands():
    """Get all available test commands"""
    base_cmd = ["pytest", "-v"]
    test_dir = Path("tests")
    
    commands = {
        "all": base_cmd + ["tests"],
        "learn_examples": base_cmd + ["tests/learn_examples"],
        # Individual concept tests
        "basics": base_cmd + ["tests/learn_examples/test_basics.py"],
        "data_types": base_cmd + ["tests/learn_examples/test_data_types.py"],
        "control_flow": base_cmd + ["tests/learn_examples/test_control_flow.py"],
        "functions": base_cmd + ["tests/learn_examples/test_functions.py"],
        "oop_basics": base_cmd + ["tests/learn_examples/test_oop_basics.py"],
        "advanced_oop": base_cmd + ["tests/learn_examples/test_advanced_oop.py"],
        "modules": base_cmd + ["tests/learn_examples/test_modules_and_packages.py"],
        "file_io": base_cmd + ["tests/learn_examples/test_file_io.py"],
        "exceptions": base_cmd + ["tests/learn_examples/test_exceptions_handling.py"],
        "advanced": base_cmd + ["tests/learn_examples/test_advanced_concepts.py"],
        "decorators": base_cmd + ["tests/learn_examples/test_decorators_and_context_managers.py"],
        "iterators": base_cmd + ["tests/learn_examples/test_iterators_and_generators.py"],
        "stdlib": base_cmd + ["tests/learn_examples/test_standard_library_and_third_party.py"],
        "pytest_basics": base_cmd + ["tests/learn_examples/test_pytest_basics.py"],
        "playwright": base_cmd + ["tests/learn_examples/test_playwright_integration.py"],
    }
    return commands

def run_with_options(command, headed=False, debug=False):
    """Add optional parameters to any test command"""
    if headed:
        command.append("--headed")
    if debug:
        command.extend(["--slowmo", "1000"])
    subprocess.run(command)

def print_help():
    """Print usage instructions"""
    commands = get_test_commands()
    print("\nUsage: python scripts.py run <test_name>")
    print("\nAvailable test names:")
    for name in commands.keys():
        print(f"  {name}")
    print("\nOptions:")
    print("  --headed                                 - Run in headed mode")
    print("  --debug                                  - Run in debug mode (slow)")

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