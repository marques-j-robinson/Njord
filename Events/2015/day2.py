import numpy


class Solution:

    def __init__(self, data):
        self.data = data.split('\n')
        self.p1 = 0
        self.p2 = 0

    def part_01(self):
        for dimensions in self.data:
            box = Box(dimensions)
            self.p1 += box.calc_surface_area() + box.calc_sm_area()

    def part_02(self):
        for dimensions in self.data:
            box = Box(dimensions)
            self.p2 += box.calc_sm_perimeter() + box.calc_cubic_volumn()


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
