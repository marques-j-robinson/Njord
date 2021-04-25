class Solution:

    def __init__(self, data):
        self.data = [int(x) for x in data]
        self.p1 = 0
        self.p2 = 0

    def part_01(self):
        prev = self.data[len(self.data) - 1]
        for idx, x in enumerate(self.data):
            if prev == x:
                self.p1 += x
            prev = x

    def part_02(self):
        half = len(self.data) // 2
        for idx, x in enumerate(self.data):
            if idx + half > len(self.data) - 1:
                half_i = self.data[idx - half]
            else:
                half_i = self.data[idx + half]
            if half_i == x:
                self.p2 += x
