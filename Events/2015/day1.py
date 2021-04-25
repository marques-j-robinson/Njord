class Solution:

    def __init__(self, data):
        self.data = data
        self.p1 = 0
        self.p2 = 0

    def part_01(self):
        for i in self.data:
            self.p1 += process_floor(i)

    def part_02(self):
        idx = 0
        floor = 0
        while floor >= 0:
            i = self.data[idx]
            floor += process_floor(i)
            idx += 1
        self.p2 = idx


def process_floor(i):
    if i == "(":
        return 1
    elif i == ")":
        return -1
