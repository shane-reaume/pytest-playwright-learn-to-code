"""
Utility functions for learning examples
"""
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
    # Create a separator line for better visibility
    separator = "-" * 80
    
    # Get the sep and end parameters or use defaults
    sep = kwargs.pop('sep', ' ')
    end = kwargs.pop('end', '\n')
    
    # Print to stderr to bypass pytest capture
    print(file=sys.stderr)  # Add a blank line before output
    print(separator, file=sys.stderr)
    print(*args, sep=sep, end=end, file=sys.stderr, flush=True, **kwargs)
    print(separator, file=sys.stderr)
    print(file=sys.stderr)  # Add a blank line after output

# Alias for shorter name if preferred
lprint = learn_print 