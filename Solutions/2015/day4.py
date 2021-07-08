import hashlib
from lib.solution import BaseSolution


class Solution(BaseSolution):

    def part_01(self):
        m = Mine(self.data, 5)
        m.run()
        self.p1 = m.val

    def part_02(self):
        m = Mine(self.data, 6)
        m.run()
        self.p1 = m.val


class Mine:

    def __init__(self, key, num_zeros):
        self.key = key
        self.num_zeros = num_zeros
        self.zeros = ''.join(['0']*num_zeros)
        self.val = 0

    def run(self):
        ready = False
        while ready is False:
            hash_str = self.hash()
            if hash_str[0:self.num_zeros] == self.zeros:
                ready = True
            else:
                self.val += 1

    def hash(self):
        hash_input = f'{self.key}{self.val}'
        hash_str = hashlib.md5(hash_input.encode())
        return hash_str.hexdigest()
