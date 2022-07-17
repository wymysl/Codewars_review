# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):
    sentence_lst = []
    available_numbers = "123456789"
    if sentence != "":
        count = 0
        for index, x in enumerate(sentence):
            if x == " ":
                sentence_lst.append(sentence[count:index])
                count = index + 1
            elif index == len(sentence) - 1:
                sentence_lst.append(sentence[count:index + 1])
        sentence_ordered = sentence_lst.copy()
        for item in sentence_lst:
            for character in item:
                if character in available_numbers:
                    sentence_ordered[int(character) - 1] = item
    else:
        return ""
    return " ".join(sentence_ordered)

print(order("ba2ck welc1ome Pawe3eł"))