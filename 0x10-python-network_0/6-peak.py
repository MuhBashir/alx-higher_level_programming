#!/usr/bin/python3
""" Finds a peak number in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integer7s(int): list of integers to find peak number in a list
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    middle = size
    midd_num = size // 2

    if size == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (midd_num < size - 1 and
                list_of_integers[midd_num] < list_of_integers[midd_num + 1]):
            if middle // 2 == 0:
                middle = 2
            midd_num = midd_num + middle // 2
        elif middle > 0 and list_of_integers[midd_num] < list_of_integers[midd_num - 1]:
            if middle // 2 == 0:
                middle = 2
            midd_num = midd_num - middle // 2
        else:
            return list_of_integers[midd_num]
