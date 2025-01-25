"""
Interactive Learning Utilities

This module provides utilities for interactive learning modules including:
- Color formatting
- Syntax highlighting with themes
- Input/output helpers
"""

from pygments import highlight, styles
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter
from pygments.styles import get_style_by_name
import sys
from typing import Any

def learn_print(*args: Any, **kwargs: Any) -> None:
    """
    Custom print function for learning examples that ensures output is visible
    during test execution. This bypasses pytest's output capture.
    
    Args:
        *args: Variable length argument list, same as built-in print()
        **kwargs: Arbitrary keyword arguments, same as built-in print()
    """
    # Get the sep and end parameters or use defaults
    sep = kwargs.pop('sep', ' ')
    end = kwargs.pop('end', ' ')
    
    # Print to stderr to bypass pytest capture
    print(file=sys.stderr)  # Add a blank line before output
    print(*args, sep=sep, end=end, file=sys.stderr, flush=True, **kwargs)
    print(file=sys.stderr)  # Add a blank line after output

# Alias for shorter name
lprint = learn_print

# ANSI color codes
BLUE = "\033[94m"      # General text
GREEN = "\033[92m"     # Success messages
RED = "\033[91m"       # Error messages
YELLOW = "\033[33m"    # Questions and prompts
BOLD = "\033[1m"       # Headers
RESET = "\033[0m"      # Reset all formatting

# Available themes with descriptions
THEMES = {
    'monokai': 'Dark theme with vibrant colors (like Sublime Text)',
    'one-dark': 'Atom-inspired dark theme with subtle colors',
    'solarized-dark': 'Popular dark theme with carefully chosen colors',
    'solarized-light': 'Light version of the Solarized theme',
    'dracula': 'Dark theme with modern colors',
    'gruvbox-dark': 'Retro groove dark theme',
    'gruvbox-light': 'Retro groove light theme',
    'nord': 'Arctic-inspired dark theme',
    'vs': 'Light theme inspired by Visual Studio',
    'zenburn': 'Low contrast dark theme easy on the eyes'
}

# Global theme setting
CURRENT_THEME = 'monokai'

def set_theme(theme_name: str) -> bool:
    """Set the current syntax highlighting theme"""
    global CURRENT_THEME
    if theme_name in THEMES:
        CURRENT_THEME = theme_name
        return True
    return False

def list_themes() -> None:
    """Print available themes with descriptions"""
    color_print(f"\n{BOLD}Available Themes:{RESET}")
    for theme, description in THEMES.items():
        # Show current theme with an indicator
        current = "→ " if theme == CURRENT_THEME else "  "
        color_print(f"{current}{theme}: {description}")

def select_theme() -> None:
    """Interactive theme selection"""
    list_themes()
    while True:
        theme = get_user_input(f"{YELLOW}Enter theme name (or 'cancel' to keep current theme): {RESET}")
        if theme == 'cancel':
            break
        if set_theme(theme):
            color_print(f"\n✅ Theme changed to {theme}!", GREEN)
            # Show a sample to preview the theme
            print_code_block("""
                def example_function(name: str) -> str:
                    \"\"\"Example function to showcase theme.\"\"\"
                    message = f"Hello, {name}!"
                    numbers = [1, 2, 3]  # A simple list
                    return message  # Return greeting
                """)
            if not get_user_input(f"{YELLOW}Keep this theme? (yes/no): {RESET}").startswith('y'):
                set_theme(CURRENT_THEME)  # Revert if user doesn't like it
                continue
            break
        else:
            color_print(f"\n❌ Invalid theme name. Please choose from the list.", RED)

def color_print(text: str, color: str = BLUE) -> None:
    """Print text in color"""
    lprint(f"{color}{text}{RESET}")

def print_code_block(code: str, indent: int = 0) -> None:
    """Print a code block with syntax highlighting using the current theme"""
    # Add a newline before the code block
    lprint("")
    
    # Remove common leading whitespace while preserving relative indentation
    lines = code.strip().split('\n')
    if lines:
        # Find minimum indentation (excluding empty lines)
        min_indent = min(len(line) - len(line.lstrip()) 
                        for line in lines if line.strip())
        # Remove that amount from each line
        lines = [line[min_indent:] if line.strip() else '' for line in lines]
    
    # Add requested indentation
    indent_str = " " * indent
    code = '\n'.join(indent_str + line for line in lines)
    
    try:
        # Apply syntax highlighting using current theme
        highlighted = highlight(
            code,
            PythonLexer(),
            Terminal256Formatter(style=CURRENT_THEME)
        )
        
        # Print the highlighted code
        lprint(highlighted)
    except Exception as e:
        # Fallback to simple formatting if theme fails
        color_print(f"Theme error: {e}. Falling back to basic formatting.", RED)
        for line in code.split('\n'):
            lprint(f"{indent_str}{line}")
    
    # Add a newline after the code block
    lprint("")

def print_section_header(text: str) -> None:
    """Print a main section header (e.g., module or major topic introduction)"""
    color_print(f"\n{BOLD}=== {text} ==={RESET}", YELLOW)

def print_subsection_header(text: str) -> None:
    """Print a subsection header (e.g., for a specific concept or question)"""
    color_print(f"\n{BOLD}{text}{RESET}")

def print_instruction(text: str) -> None:
    """Print an instruction or action prompt for the user"""
    color_print(text, YELLOW)

def print_success(text: str) -> None:
    """Print a success message"""
    color_print(f"\n✅ {text}", GREEN)

def print_error(text: str) -> None:
    """Print an error message"""
    color_print(f"\n❌ {text}", RED)

def print_info(text: str) -> None:
    """Print general information"""
    color_print(text, BLUE)

def get_user_input(prompt: str) -> str:
    """
    Get user input with a formatted prompt.
    The prompt is automatically colored and reset.
    """
    color_print(f"\n{YELLOW}{prompt}{RESET}")
    return input().strip().lower()

def check_answer(user_answer: str, correct_answers: list[str], explanation: str) -> bool:
    """Check user answer and provide feedback with consistent formatting"""
    if user_answer in correct_answers:
        print_success(f"Correct! {explanation}")
        return True
    else:
        print_error(f"Not quite. {explanation}")
        return False 