#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - A peak element if found, None otherwise.
    """
    n = len(list_of_integers)
    
    if n == 0:
        return None
    
    mid = n // 2
    mid_val = list_of_integers[mid]
    
    if (mid == 0 or mid_val >= list_of_integers[mid - 1]) and \
       (mid == n - 1 or mid_val >= list_of_integers[mid + 1]):
        return mid_val
    
    if mid > 0 and list_of_integers[mid - 1] > mid_val:
        return find_peak(list_of_integers[:mid])
    
    return find_peak(list_of_integers[mid + 1:])

