# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

def to_camel_case(text):
    camel_text = ""
    current_char = -1
    for char in text:
        current_char += 1
        if text[current_char - 1] == "-" or text[current_char - 1] == "_":
            camel_text += char.upper()
        elif char == "-" or char == "_":
            continue
        else:
            camel_text += char
    return(camel_text)
