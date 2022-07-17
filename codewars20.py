# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):
    lst_text = list(text)
    chars = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    output_text = ""
    for index, x in enumerate(lst_text):
        if x.casefold() not in chars:
            if lst_text[index - 1].casefold() not in chars:
                count = index + 1
                output_text += text[index]
            else:
                output_text += text[(count + 1):index] + text[count] + "ay" + text[index]
                count = index + 1
        elif index == len(lst_text) - 1:
            output_text += text[(count + 1):(index + 1)] + text[count] + "ay"
    return output_text


print(pig_it("O tempora o mores !"))
