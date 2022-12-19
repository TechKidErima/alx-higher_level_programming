#!usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints the result.

    Args:
        a(int): first int
        b(int): second int for division
    Returns:
        The result of the division.
    """
    try:
        i = a/b
        return(i)
    except(ZeroDivisionError, TypeError, ValueError):
        i = None
    finally:
        print("Inside result: {}".format(i))
    return (i)

    
