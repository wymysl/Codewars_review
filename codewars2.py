# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

text = input("enter text")
duplicate_count = 0
duplicates = ""
for char in text.casefold():
    if text.casefold().count(char) > 1:
        if char not in duplicates:
            duplicates += char
            duplicate_count += 1
print(duplicate_count)


# text = input("enter text")
# duplicate_count = 0
# for char in text:
#     a = char
#     b = 0
#     for char in text:
#         if a == char:
#             b +=1
#             if b >= len(text):
#                 duplicate_count += 1
# print(duplicate_count)