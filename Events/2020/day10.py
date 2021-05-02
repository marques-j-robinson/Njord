from util import BaseSolution


class Solution(BaseSolution):

    def translate(self):
        self.split_by_new_line()
        self.int_list()

    def part_01(self):
        pass

    def part_02(self):
        pass

import fileinput
import pyperclip

# Solve below...
p1 = 0
p2 = 0

nums = [int(x) for x in fileinput.input()]
nums.append(0)
nums.append(max(nums)+3)
nums = sorted(nums)
jolt1 = 0
jolt3 = 0
for i in range(len(nums)-1):
    d = nums[i+1]-nums[i]
    if d==1:
        jolt1 += 1
    elif d==3:
        jolt3 += 1
p1 = jolt1*jolt3

DP = {}
def dp(i):
    if i==len(nums)-1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(nums)):
        if nums[j]-nums[i]<=3:
            ans += dp(j)
    DP[i] = ans
    return ans

p2 = dp(0)
print(DP)

print('---')
print(p1)
pyperclip.copy(p2)
print(p2)
