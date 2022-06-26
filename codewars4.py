# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

# def get_count(sentence):
#     pass

vowels_count = 0

sentence = input("Please write something: ")

for char in sentence:
    if char.casefold() == "a" or char.casefold() == "e" or char.casefold() == "i" or char.casefold() == "o" or char.casefold() == "u":
        vowels_count += 1

print(vowels_count)

# code to enter into codewars terminal:
#
# def get_count(sentence):
#     vowels_count = 0
#
#     for char in sentence:
#          if char.casefold() == "a" or char.casefold() == "e" or char.casefold() == "i" or char.casefold() == "o" or char.casefold() == "u":
#             vowels_count += 1
#
#     return (vowels_count)