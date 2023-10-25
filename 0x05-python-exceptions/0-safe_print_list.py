#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Prints elements of a list up to a certain index.

    Args:
        my_list (list): The list to print.
        Defaults to an empty list.
        x (int): The index up to which to print the list.
        Defaults to 0.

    Returns:
        int: The number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return(count)
