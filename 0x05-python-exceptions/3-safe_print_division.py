#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides 2 integers and prints."""
    try:
        i = a / b
    except (ZeroDivisionError, TypeError):
        i = None
    finally:
        print("Inside result: {}".format(i))
    return (i)   
