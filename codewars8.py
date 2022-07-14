# https://www.codewars.com/kata/58b3c2bd917a5caec0000017/train/python
# I understand now that:
# for now it only sums TWO neighboring ints in a list that are both even or both odd.

def sum_groups(arr):
    while True:
        init = len(arr)
        for index, x in enumerate(arr):
            if index < len(arr) - 1:
                if arr[index] % 2 == 0 and arr[index + 1] % 2 == 0 or arr[index] % 2 != 0 and arr[index + 1] % 2 != 0:
                        arr[index] += arr[index + 1]
                        del arr[index + 1]
            elif index == len(arr):
                if arr[index - 1] % 2 == 0 and arr[index] == 0 or arr[index - 1] % 2 != 0 and arr[index] != 0:
                    arr[index - 1] += arr[index]
                    del arr[index]
        end = len(arr)
        if init == end:
            break

    return len(arr), arr

print(sum_groups([77, 173, 115, 172, 235, 605, 635, 28, 202, 619, 881, 320, 382, 964, 361, 798, 558, 298, 907, 131, 47, 199, 9, 335, 480, 32, 123, 182, 697, 957, 294, 98, 649, 238, 251, 770, 169, 172, 923, 413]))