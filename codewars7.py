# https://www.codewars.com/kata/5815f7e789063238b30001aa/train/python

def redistribute_wealth(wealth):
    if sum(wealth) % len(wealth) == 0:
        wealth = [int((sum(wealth) / len(wealth)))] * len(wealth)
    else:
        wealth = [float((sum(wealth) / len(wealth)))] * len(wealth)
