# Psuedo code

# Part 1
# - keep track of a value start with 0
# - loop through data
# - ( means positive
# - ) means negative

# Part 2
# - loop through data until the start value reaches -1 for the first time

class Solution:

    def __init__(self, data):
        self.data = data

    def part_01(self):
        self.res = 0
        for i in self.data:
            self.process_floor(i)

    def part_02(self):
        self.res = 0
        idx = 0
        while self.res >= 0:
            i = self.data[idx]
            self.process_floor(i)
            idx += 1
        self.res = idx

    def process_floor(self, i):
        if i == "(":
            self.res += 1
        elif i == ")":
            self.res -= 1
