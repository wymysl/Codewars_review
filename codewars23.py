# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python

def zeros(n):
    if n >= 5:
        five_power = 1
    else:
        five_power = 0
    x = n // 5
    while True:  # this loop finds the highest power of 5 in range 1 to n.
        # I know there must be an easier way to do this.
        if x // 5 >= 1:
            five_power += 1
            x = x // 5
        else:
            break
    y = 0
    while True:
        if five_power >= 2:
            y += n // 5 ** five_power
            five_power -= 1
        else:
            break
    return (n // 5) + y


print(zeros(125))
