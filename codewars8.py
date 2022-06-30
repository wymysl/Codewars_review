# https://www.codewars.com/kata/58b3c2bd917a5caec0000017/train/python
# I know the code doesn't  work as it should... yet. I will fix it later.
# def sum_groups(arr):

arr = [2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]

for index, x in enumerate(arr):
    if arr[x] % 2 == 0:
        if arr[x + 1] % 2 != 0:
            continue
        else:
            arr[x] += arr[x + 1]
            arr.pop(x + 1)

    else:
        if arr[x + 1] % 2 == 0:
            continue
        else:
            arr[x] += arr[x + 1]
            arr.pop(x + 1)


print(arr)
print(len(arr))
# items_to_sum = []
#
# for index, number in enumerate(arr)
#     if number % 2 == 0:
#         if i+1 % 2 == 0:
#             arr.pop(i)

# items_to_pop = []
# x = -1
#
# for x in arr:
#     if arr[x] % 2 == 0:
#         if arr[x - 1] % 2 != 0:
#             items_to_pop.append([x])
#         else:
#             arr[x] += arr[x - 1]
#             arr.pop(x - 1)
#     else:
#         if arr[x - 1] % 2 == 0:
#             x += 1
#         else:
#             arr[x] += arr[x - 1]
#             items_to_pop.append([x])
#
# arr.pop(items_to_pop)
#
# print(arr)

# arr_position = n = -1 # for code readability
# evens = []
# odds = []
# for x in arr:
#     n += 1
#     if arr[n] % 2 == 0:
#         evens += [n]
#     else:
#         odds += [n]
#
# print(evens)
# print(odds)


    #
    # else:
    #     if arr[n + 1] % 2 == 0:
    #         odds = arr[n]
    #
    #
    #
    #     if arr[n + 1] % 2 != 0:
    #     arr[n] += arr[arr_position + 1]
    #     del arr[n + 1]
    #     n += 1
    #
    # and arr[n + 1] % 2 == 0) or (arr[n] % 2 != 0 and arr[n + 1] % 2 != 0):
    #     arr[n] += arr[n + 1]
    #     del arr[n + 1]
    #     n += 1
    # else:
    #     n += 1

# print(arr)
#
#
# # for x in arr:
#     if arr[x] % 2 != 0:
#         if arr[x + 1] % 2 == 0:
#             arr[x] += arr[x + 1]
#         else:
#             continue
#     if arr[x] % 2 == 0:
#         if arr[x + 1] % 2 != 0:
#             arr[x] += arr[x + 1]
#         else:
#             continue
#
# print(arr)

#     if (arr[i] % 2 == 0 and arr [i + 1] % 2 == 0) or (arr[i] % 2 != 0 and arr[i + 1] % 2 != 0):
#         arr[i] += arr[i + 1]
#     else:
#         continue
#
# print(arr)