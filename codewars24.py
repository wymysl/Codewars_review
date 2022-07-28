# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    x_coordinate = 0
    y_coordinate = 0
    for direction in walk:
        if direction == "n":
            x_coordinate += 1
        elif direction == "s":
            x_coordinate -= 1
        elif direction == "e":
            y_coordinate += 1
        elif direction == "w":
            y_coordinate -= 1
        else:
            return False
    if len(walk) == 10 and x_coordinate == 0 and y_coordinate == 0:
        return True
    else:
        return False


print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
