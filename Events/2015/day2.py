# Psuedo code

# data is a list of dimensions (l, w, h)

# Part 1
# - loop through the dimensions
# - create a box
# - find the surface area of the box and add it to the total
# - find the area of the smallest side and add it to the total

# Part 2
# - loop through the dimensions
# - create a box
# - find the smallest perimeter of any one face and add it to the total
# - find the cubic feet of volume of the box


import numpy


class Solution:

    def __init__(self, data):
        self.data = data.split('\n')

    def part_01(self):
        self.res = 0
        for dimensions in self.data:
            box = Box(dimensions)
            self.res += box.calc_surface_area() + box.calc_sm_area()

    def part_02(self):
        self.res = 0
        for dimensions in self.data:
            box = Box(dimensions)
            self.res += box.calc_sm_perimeter() + box.calc_cubic_volumn()


class Box:

    def __init__(self, dimensions):
        [l, w, h] = dimensions.split("x")
        self.sides = [int(l), int(w), int(h)]

    def get_sm_side(self):
        sm_side = self.sides[:]
        sm_side.remove(max(sm_side))
        return sm_side

    def calc_surface_area(self):
        [l, w, h] = self.sides
        return 2*l*w + 2*w*h + 2*h*l

    def calc_cubic_volumn(self):
        [l, w, h] = self.sides
        return l*w*h

    def calc_sm_area(self):
        sm_side = self.get_sm_side()
        return numpy.prod(sm_side)

    def calc_sm_perimeter(self):
        sm_side = self.get_sm_side()
        return sum([2*x for x in sm_side])
