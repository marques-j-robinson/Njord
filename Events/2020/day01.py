from util import BaseSolution


class Solution(BaseSolution):

    def translate(self):
        self.split_by_new_line()
        self.int_list()

    def part_01(self):
        for i in self.data:
            for j in self.data:
                if i+j == 2020:
                    self.p1 = i*j

    def part_02(self):
        for i in self.data:
            for j in self.data:
                for k in self.data:
                    if i+j+k == 2020:
                        self.p2 = i*j*k
