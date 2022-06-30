# https://www.codewars.com/kata/55f3da49e83ca1ddae0000ad/train/python
#
# Way too much maths. Brain hurts. Must rest.
#
# This code is a mess and so am I.
#
# def tankvol(h, d, vt):

from math import atan, sqrt, pi, degrees, sin
h = 40
d = 120
vt = 3500

r = (d / 2)

cylinder_h = vt / (pi * (r ** 2))

chord = 2 * (sqrt((d * h) - (h ** 2)))  # This calculates the base of the right triangle with the height of d - h and an arm of length d/2. I wish I knew how to make this comment line more elegant since it's so long, but I don't know how.

# angle = acos((r ** 2 + r ** 2 - chord ** 2) / ((2 ** r) ** 2))

angle = degrees(atan(chord / ((r - h))))

# area = (1/2 * (angle - sin(angle)) * r ** 2)

area = (0.5 * (r ** 2) * (angle - sin(angle)))

volume = area * cylinder_h

print(volume)

# area_triangle = r ** base
#
# angle = degrees(atan(base / ((d / 2) - h))) # This calculates the angle of the circle segment.
#
# area_segment = ((angle / 360) ** (pi ** (r ** r)))
#
# area_h = area_segment - area_triangle
# Since my maths is very rusty, only after writing the above code did I realise there is a much more efficient way
# to find the area of the circle segment minus the triangle:

# area = (0.5 * ((r ** r) * (angle - sin(angle))))

# area = ((r ** r) * acos((r - h) / r) - (r - h) * sqrt(2 ** ((r ** h) - h ** h)))
#
# v = int(area ** cylinder_h)
#
# print(v)