# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

import itertools


def get_pins(observed):
    pin_numbers = []
    answer = []
    pin_values = {"1": [1, 2, 4],
                  "2": [1, 2, 3, 5],
                  "3": [2, 3, 6],
                  "4": [1, 4, 5, 7],
                  "5": [2, 4, 5, 6, 8],
                  "6": [3, 5, 6, 9],
                  "7": [4, 7, 8],
                  "8": [5, 7, 8, 9, 0],
                  "9": [6, 8, 9],
                  "0": [8, 0]}
    for char in observed:
        pin_numbers.append(pin_values.get(char))
    # for char in observed:
    #     if char == "1":
    #         pin_numbers += "124"
    #     if char == "2":
    #         pin_numbers += "1235"
    #     if char == "3":
    #         pin_numbers += "236"
    #     if char == "4":
    #         pin_numbers += "1457"
    #     if char == "5":
    #         pin_numbers += "24568"
    #     if char == "6":
    #         pin_numbers += "3569"
    #     if char == "7":
    #         pin_numbers += "478"
    #     if char == "8":
    #         pin_numbers += "57890"
    #     if char == "9":
    #         pin_numbers += "689"
    #     if char == "0":
    #         pin_numbers += "80"
    # for x in range(0, len(pin_numbers) + 1):
    #     for subset in itertools.combinations(pin_numbers, x):
    #         for num in
    #         answer += subset

    for pos, i in enumerate(pin_numbers):
        if pos < len(pin_numbers) - 1:
            answer.append(list(itertools.product(pin_numbers[pos])))


    return answer

print(get_pins("81"))
