print("Please provide a number: ")
number = int(input())

if number < 0:
    print(0)

total = 0

for i in range(number):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print("The sum of all the natural numbers below {} that are multiples of 3 or 5 is {}.".format(number, total))