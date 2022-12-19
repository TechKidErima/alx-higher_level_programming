#!usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.

    Args:
        my_list(list): list to print from.
        x(int): number of items to print from list
    Returns:
        The elements printed.

    """
    j = 0
    for i in range(0, x):
        try:
            print("{:d}".fomart(my_list[i]), end="")
            j++
        except(ValueError, TypeError):
            continue
    print("")
    return (j)
