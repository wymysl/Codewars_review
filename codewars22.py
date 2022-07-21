# https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    if s == "" or len(s) >= 141:
        return False
    else:
        hash_string = "#"
        start = 0
        for index, char in enumerate(s):
            if char == " ":
                hash_string += s[start:index].capitalize()
                start = index + 1
    hash_string += s[start:].capitalize()
    return hash_string


print(generate_hashtag("Cześć witam serdecznie elko"))
