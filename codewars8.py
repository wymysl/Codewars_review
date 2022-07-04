# https://www.codewars.com/kata/58b3c2bd917a5caec0000017/train/python
# works locally, but codewars returns error:/
# not all arguments converted during string formatting (line 17 I think)

def sum_groups(arr):
    arr.append("hehe")
    batman = True
    while batman:
        init_len = str(len(arr))
        for index, x in enumerate(arr):
            if arr[index] % 2 == 0:
                if arr[index + 1] != "hehe":
                    if arr[index + 1] % 2 != 0:
                        continue
                    else:
                        while arr[index + 1] % 2 == 0:
                            arr[index] += arr[index + 1]
                            arr.pop(index + 1)
                else:
                    break
            else:
                if arr[index + 1] != "hehe":
                    while arr[index + 1] % 2 != 0:
                        arr[index] += arr[index + 1]
                        arr.pop(index + 1)
                        break
                else:
                    break
        final_len = str(len(arr))
        if init_len == final_len:
            batman = False
            arr.pop(-1)
    return len(arr)


print(sum_groups([2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]))
