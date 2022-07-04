# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
# I misunderstood the assignment and wrote code which only prints the first occurence of a character in a string.
# I will repair it later.

def unique_in_order(iterable):
    iterable_new = []
    iterable += " "
    for index, x in enumerate(iterable):
        if index in range(len(iterable) - 1):
            if iterable.count(x) > 1:
                if iterable[index + 1] == iterable[index]:
                    continue
                else:
                    iterable_new.append(x)
            else:
                iterable_new.append(x)
        else:
            break
    iterable = iterable_new
    return iterable

print(unique_in_order("AAAABBBCCDAABBB"))
