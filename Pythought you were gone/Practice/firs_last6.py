"""
Given an array of ints, return True if 6 appears as either the first or last elements in the array.
The array will be length 1 or more
"""
def first_last6(array):
    if len(array) > 1:
        if array[0] == 6 or array[-1] == 6:
            return True
    return False