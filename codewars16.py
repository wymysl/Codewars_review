# https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/python

def arrange(s):
    if s:
        t = []
        u = s.copy()
        while len(t) < len(s):
            if len(u) == 1:
                t.append(u[0])
                break
            t.append(u[0])
            t.append(u[-1])
            u.reverse()
            u.pop(0)
            u.pop(-1)
    else:
        return []

    return t


print(arrange([1, 2, 3]))
