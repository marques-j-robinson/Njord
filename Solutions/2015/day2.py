import numpy
from lib.solution import BaseSolution


class Solution(BaseSolution):
    """
    Data Structure - List
    Algorithm - Loop
    Runtime - O(n)
    """

    def translate(self):
        self.split_by_new_line()

    def part_01(self):
        for sides in self.data:
            box = Box(sides)
            self.p1 += box.surface_area() + box.area()

    def part_02(self):
        for sides in self.data:
            box = Box(sides)
            self.p2 += box.volumn_cubic_ft() + box.perimeter()


class Box:

    def __init__(self, sides):
        self.parse_sides(sides)
        self.get_sm_sides()

    def parse_sides(self, sides):
        [l, w, h] = sides.split('x')
        self.sides = [int(l), int(w), int(h)]

    def get_sm_sides(self):
        self.sm_sides = self.sides[:]
        self.sm_sides.remove(max(self.sm_sides))

    def surface_area(self):
        [l, w, h] = self.sides
        return 2*l*w + 2*w*h + 2*h*l

    def area(self):
        return numpy.prod(self.sm_sides)

    def volumn_cubic_ft(self):
        [l, w, h] = self.sides
        return l*w*h

    def perimeter(self):
        return sum([2*x for x in self.sm_sides])
