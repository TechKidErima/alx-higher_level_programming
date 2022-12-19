#!/usr/bin/python3

def safe_print_integer(value):
    """Print a formatted interger value.

    Args:
        value: the value ot be printed

    Returns:
        Return true if printed value is an interger

    """
    try:
        print("{:d}".fomart(value))
        return True
    except (ValueError, TypeError):
        return False
