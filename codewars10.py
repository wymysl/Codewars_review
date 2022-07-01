# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python

# This code works, but is still to inefficient.
# I am no mathematician. I (think) I used the 6k ± 1 optimization method
# which I didn't know existed until today. Yet it's still too slow.
# Like I said before - I'm still disappointed with our ways of finding primes...

def is_prime(num):
    if num <= 0 or num == 1:
        return False
    else:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
            if num == 2 or num == 3 or num == 5 or num == 7 or num == 11:
                return True
            else:
                return False
        else:
            x = 13
            while x in range(13, int((num / 2))):
                if num % x == 0:
                    return False
                else:
                    x += 6
            else: return True



print(is_prime(6475987587691))
