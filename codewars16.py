# https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/python

def arrange(s):
    if s:
        t = []
        count = 0
        while len(t) < len(s):
            if count % 2 == 0:
                t.append(s[count])
                if (count < (len(s) // 2)):
                    t.append(s[-(count + 1)])
                    count += 1
            else:
                     t.append(s[-(count + 1)])
                     if (count < (len(s) // 2)):
                         t.append(s[count])
                         count += 1
    else:
        return []

    return t


print(arrange([1, 2, 3]))
