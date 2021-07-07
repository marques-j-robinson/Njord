from lib.solution import BaseSolution


class Solution(BaseSolution):
    """
    Data Structure - String
    Algorithm - Loop
    Runtime - O(n)
    """

    def part_01(self):
        apartment = Building()
        for instruction in self.data:
            apartment.step(instruction)
        self.p1 = apartment.cur_floor

    def part_02(self):
        "Identify when cur_floor is first -1"
        apartment = Building()
        idx = 0
        while apartment.cur_floor >= 0:
            instruction = self.data[idx]
            apartment.step(instruction)
            idx += 1
        self.p2 = idx


class Building:

    up = "("
    cur_floor = 0

    def step(self, instruction):
        if instruction == self.up:
            self.cur_floor += 1
        else:
            self.cur_floor -= 1
