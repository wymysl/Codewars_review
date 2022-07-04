# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr, k):
    concatenated_list = []
    concatenated_str = ""
    for index, x in enumerate(strarr):
        if strarr:
            if index <= len(strarr) - k:
                step = 0
                index_increase = 0
                while step < k:
                    concatenated_str += strarr[index + index_increase]
                    step += 1
                    index_increase += 1
                else:
                    concatenated_list.append(concatenated_str)
                    concatenated_str = ""
            else:
                break
        else:
            break
    if concatenated_list:
        return max(concatenated_list, key=len)
    else:
        return ""


print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 2))
