# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

def friend(x):
    true_friends = []
    for name in x:
        if len(name) == 4:
            true_friends.append(name)
    return true_friends

print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))
