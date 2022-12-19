#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x number of items of a list.

    Args:
        my_list(list): The list to print elements from.
        x (int): The specified number of items to print.

    Returns:
        The number of ite,s printd from the list
    """
    k = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i], end="")
            k++
        except IndexError:
            break

    print("")
    return (k)

