# https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

def solution(roman):
    arabic = 0
    roman_values = {"M": 1000, "D": 500, "C": 100, "L": 50,
                    "X": 10, "V": 5, "I": 1}
    for index, letter in enumerate(roman):
        if index < len(roman) - 1:
            if roman_values[roman[index + 1]] > roman_values[roman[index]]:
                # current character must have lesser value than the next (as in IV, IX, XC etc.)
                # next character value will be added anyway, so we first subtract the value of
                # current one.
                arabic -= roman_values[roman[index]]
            else:
                arabic += roman_values[roman[index]]
        else:
            arabic += roman_values[roman[index]]

    return arabic


print(solution("III"))
