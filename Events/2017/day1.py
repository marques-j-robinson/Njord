# Psuedo code

# Part 1
# -

# Part 2
# -


class Solution:

    def __init__(self, data):
        nums = [int(x) for x in data]
        self.prev = nums[len(nums) - 1]
        self.half = len(nums) // 2
        self.data = nums

    def part_01(self):
        self.res = 0
        for idx, x in enumerate(self.data):
            if self.prev == x:
                self.res += x
            self.prev = x

    def part_02(self):
        self.res = 0
        for idx, x in enumerate(self.data):
            if idx + self.half > len(self.data) - 1:
                half_i = self.data[idx - self.half]
            else:
                half_i = self.data[idx + self.half]
            if half_i == x:
                self.res += x
