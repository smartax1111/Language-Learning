"""
Return the number of even ints in the given array.
"""

def count_evens(arr):
    count = 0
    for x in range (len(arr)):
        if int(arr[x]) % 2 == 0:
            count += 1
    print(str(count))

count_evens('23743521')