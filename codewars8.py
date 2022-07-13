# https://www.codewars.com/kata/58b3c2bd917a5caec0000017/train/python

def sum_groups(arr):
    while True:
        init = len(arr)
        for index, x in enumerate(arr):
            if index < len(arr) - 1:
                if arr[index] % 2 == 0 and arr[index + 1] % 2 == 0 or arr[index] % 2 != 0 and arr[index + 1] % 2 != 0:
                        arr[index] += arr[index + 1]
                        arr.pop(index + 1)
            elif index == len(arr):
                if arr[index - 1] % 2 == 0 and arr[index] == 0 or arr[index - 1] % 2 != 0 and arr[index] != 0:
                    arr[index - 1] += arr[index]
                    arr.pop(index)
        end = len(arr)
        if init == end:
            break

    return arr

print(sum_groups([2, 1, 2, 2, 6, 5, 0, 2, 0, 3, 3, 3, 9, 2]))
