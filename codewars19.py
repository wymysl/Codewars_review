# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

def dirReduc(arr):
    direction_values = {"NORTH": 1,
                        "SOUTH": -1,
                        "EAST": 2,
                        "WEST": -2}
    while True:
        pop_counter = 0
        for index, direction in enumerate(arr):
            if index < len(arr) - 1:
                if direction_values[arr[index + 1]] == - direction_values[arr[index]]:
                    arr.pop(index)
                    arr.pop(index)
                    pop_counter += 1
                    break
            else:
                break
        if pop_counter == 0:
            break

    return arr


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
