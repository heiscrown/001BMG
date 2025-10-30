#!/usr/bin/env python3
"""
Simple script to provide a greeting.

This module is designed to be executable from the command line
and demonstrates adherence to standard Python code quality guidelines.
"""

import sys

def greet(name: str) -> None:
    """
    Prints a personalized greeting to the console.

    Args:
        name: The name of the person to greet.
    """
    print(f"Hello, {name}!")


def main():
    """
    Main entry point for the script.
    """
    # Use the first command-line argument as the name, or a default value.
    target_name = sys.argv[1] if len(sys.argv) > 1 else "Termux Developer"
    greet(target_name)


if __name__ == "__main__":
    main()
