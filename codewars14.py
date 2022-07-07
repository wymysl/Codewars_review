# https://www.codewars.com/kata/6071ef9cbe6ec400228d9531/train/python

def calculator(txt):
    result = ""
    if "+" in txt:
        result += "." * (txt.count("."))
    elif "-" in txt:
        minuend = 0
        subtrahend = 0
        for index, x in enumerate(txt):
            if x == "." and index < txt.find(" "):
                minuend += 1
            elif x == ".":
                subtrahend += 1
        result += ("." * (minuend - subtrahend))
    elif "*" in txt:
        factor_1 = 0
        factor_2 = 0
        for index, x in enumerate(txt):
            if x == "." and index < txt.find(" "):
                factor_1 += 1
            elif x == ".":
                factor_2 += 1
        result += ("." * (factor_1 * factor_2))
    elif "//" in txt:
        dividend = 0
        divisor = 0
        for index, x in enumerate(txt):
            if x == "." and index < txt.find(" "):
                dividend += 1
            elif x == ".":
                divisor += 1
        result += ("." * (dividend // divisor))
    return(result)

print(calculator("..... * .."))
