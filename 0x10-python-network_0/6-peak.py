#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    size = len(list_of_integers)
    search_range = size
    mid_index = size // 2

    if size == 0:
        return None

    while True:
        search_range = search_range // 2
        if (mid_index < size - 1 and
                list_of_integers[mid_index] < list_of_integers[mid_index + 1]):
            if search_range // 2 == 0:
                search_range = 2
            mid_index = mid_index + search_range // 2
        elif (search_range > 0 and
              list_of_integers[mid_index] < list_of_integers[mid_index - 1]):
            if search_range // 2 == 0:
                search_range = 2
            mid_index = mid_index - search_range // 2
        else:
            return list_of_integers[mid_index]
