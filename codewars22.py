# https://www.codewars.com/kata/53f40dff5f9d31b813000774/train/python

def generate_hashtag(s):
    if s == "" or len(s) >= 141:
        return False
    else:
        s_list = []
        start = 0
        for index, char in enumerate(s):
            if char == " ":
                s_list.append(s[start:index])
                start = index + 1
    s_list.append(s[start:])
    s_list = [word.title() for word in s_list]
    return "#" + "".join(s_list)


print(generate_hashtag("Cześć witam serdecznie elko"))
