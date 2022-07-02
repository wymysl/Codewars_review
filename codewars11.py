# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(array):
    zero_count = []
    for index, x in enumerate(array):
        if x == 0:
            zero_count.append(0)

    array = [value for value in array if value != 0]
    array.extend(zero_count)

    return array

print(move_zeros([1, 0, 0, 2]))