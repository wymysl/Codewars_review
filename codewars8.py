# https://www.codewars.com/kata/58b3c2bd917a5caec0000017/train/python
# Just testing something out. I'm about to give up.

def sum_groups(arr):
    while True:
        init = len(arr)
        odds_count = 0
        for index, x in enumerate(arr):
            if index < len(arr) - 1: #  let's take care of the evens first - they're easier.
                if arr[index] % 2 == 0 and arr[index + 1] % 2 == 0:
                    arr[index] += arr[index + 1]
                    del arr[index + 1]
                if arr[index] % 2 != 0 and arr[index + 1] % 2 != 0:
                    arr[index] += arr[index + 1]
                    del arr[index + 1]
                    odds_count += 1
                    for potential_odd_index, potential_odd in enumerate(arr[index + 1:]):
                        if odds_count >= 1 and arr[potential_odd_index] % 2 != 0:
                            arr[index] += potential_odd
                            del arr[index + 1]
                            if index == len(arr) - 1 and arr[index + 1] % 2 != 0:
                                arr[index] += arr[index + 1]
                                del arr[index + 1]
                                break
                        elif arr[potential_odd_index] % 2 == 0:
                            odds_count = 0
                            break
            elif index == len(arr):
                if arr[index - 1] % 2 == 0 and arr[index] == 0:
                    arr[index - 1] += arr[index]
                    del arr[index]
        end = len(arr)
        if init == end:
            break

    return len(arr), arr

print(sum_groups([165, 75, 333, 777, 313, 682, 42, 137, 230, 922, 417, 902, 938, 106, 179, 387, 310, 870, 952, 12, 421, 619, 478, 631, 390, 881, 681, 0, 359, 654, 161, 756, 250, 508, 669, 997, 985, 97, 841, 270, 722, 885, 554, 201, 592, 670, 130, 791, 520, 784, 216, 833, 849, 104, 114, 557, 78, 646, 279, 209, 550, 41, 95, 539, 227, 123, 252, 668, 337, 116, 597, 494, 469, 775, 665]))