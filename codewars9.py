# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
# I misunderstood the assignment and wrote code which only prints the first occurence of a character in a string.
# I will repair it later.
# def unique_in_order(iterable):

iterable = 'AAAABBBCCDAABBB'
iterable_new = []
for index, x in enumerate(iterable):
    if index in range (len(iterable)):
        if iterable.count(x) > 1:
            if iterable[index + 1] == '{}'.format(x):
                iterable = iterable.replace(iterable[index + 1], '')
                break
        else:
            iterable_new += x
            iterable = iterable.replace(iterable[index], '')
    else:
        break


print(iterable_new)


# iterable = 'AAAABBBCCDAABBB'
# iterable_new = []
# for y in iterable:
#     for x in iterable:
#         if iterable.count(x) > 1:
#
#             iterable_new += x
#             iterable = iterable.replace(x, '')
#             break
#
#         else:
#             iterable_new += x
#             iterable = iterable.replace(x, '')
#
#
# print(iterable_new)