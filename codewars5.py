# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
# this code does not pass the codewars test, but it prints
# a neat Christmas tree, and I like it better than the
# codewars targeted result. I would still like to understand
# what exactly am I missing from the assignment :)

# def tower_builder(n_floors):
    # build here

n_floors = int(input("Select number of floors: "))

count = 1

for i in range (n_floors):
    print("{:^{max_width}}".format("*" * count, max_width = ((n_floors * 2) - 1)))
    count += 2