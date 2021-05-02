import numpy

from util import BaseSolution


class Solution(BaseSolution):

    def translate(self):
        self.split_by_new_line()

    def part_01(self):
        for dimensions in self.data:
            box = Box(dimensions)
            self.p1 += box.calc_wrapping_paper()

    def part_02(self):
        for dimensions in self.data:
            box = Box(dimensions)
            self.p2 += box.calc_ribbon()


class Box:

    def __init__(self, dimensions):
        [l, w, h] = dimensions.split("x")
        self.sides = [int(l), int(w), int(h)]

    def calc_wrapping_paper(self):
        return self.surface_area() + self.sm_area()

    def calc_ribbon(self):
        return self.sm_perimeter() + self.cubic_volumn()

    def surface_area(self):
        [l, w, h] = self.sides
        return 2*l*w + 2*w*h + 2*h*l

    def sm_area(self):
        sm_side = self.sm_side()
        return numpy.prod(sm_side)

    def sm_perimeter(self):
        sm_side = self.sm_side()
        return sum([2*x for x in sm_side])

    def cubic_volumn(self):
        [l, w, h] = self.sides
        return l*w*h

    def sm_side(self):
        sm_side = self.sides[:]
        sm_side.remove(max(sm_side))
        return sm_side
