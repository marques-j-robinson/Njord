class Solution:

    def __init__(self, data):
        self.p1 = 0
        self.p2 = 0
        self.data = [int(l) for l in data.split()]

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
