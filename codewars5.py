# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
# Although the code renders a nice Christmas tree, it does not pass the codewars test.
# I might have misunderstood part of the assignment. Guidance would be appreciated.

def tower_builder(n_floors):
    count = 1

    for i in range (n_floors):
        print("{:^{max_width}}".format("*" * count, max_width = ((n_floors * 2) - 1)))
        count += 2

