# Psuedo code

# Part 1
# -

# Part 2
# -


import hashlib


class Solution:

    def __init__(self, data):
        self.data = data

    def part_01(self):
        self.res = 0
        mine = Mine(self.data)
        self.res = mine.start(5)

    def part_02(self):
        self.res = 0
        mine = Mine(self.data)
        self.res = mine.start(6)


class Mine:

    def __init__(self, secret_key):
        self.secret_key = secret_key

    def start(self, target):
        zeros = "".join(["0"] * target)
        count = 0
        exit = False
        while exit is False:
            res = self.extract(count)
            if res[0:target] == zeros:
                exit = True
            else:
                count += 1
        return count

    def extract(self, count):
        str2hash = f"{self.secret_key}{count}"
        res = hashlib.md5(str2hash.encode())
        return res.hexdigest()
