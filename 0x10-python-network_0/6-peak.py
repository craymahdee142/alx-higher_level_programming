#!/usr/bin/python3
"""ind the peak in a unsorted integers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers (int): list of integers to find peak
    Returns: peak of list of integers or None
    """
    size = len(list_of_integers)
    if size == 0:
        return None
    left, right = 0, size - 1
    # use while until left is less right
    while left <= right:
        mid = left + (right - left) // 2
        list_mid = list_of_integers[mid]
        list_mid_1 = list_of_integers[mid + 1]
        # compare current element with the next element
        if mid < size - 1 and list_mid < list_mid_1:
            left = mid + 1
        else:
            right = mid - 1
    return list_of_integers[left] if left < size else None
