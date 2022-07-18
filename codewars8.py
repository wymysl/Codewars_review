# https://www.codewars.com/kata/58b3c2bd917a5caec0000017/train/python
# I gave up and used groupby.

from itertools import groupby
def sum_groups(arr):
    while True:
        start = len(arr)
        arr = [sum((list(g))) for k, g in groupby(arr, lambda x: x % 2 == 0)]
        stop = len(arr)
        if start == stop:
            break
    return len(arr)


print(sum_groups([2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]))
