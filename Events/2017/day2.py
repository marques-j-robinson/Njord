class Solution:

    def __init__(self, data):
        print(data)
        self.data = [[int(x) for x in l.strip().split("\t")] for l in data]
        self.p1 = 0
        self.p2 = 0

    def part_01(self):
        for row in self.data:
            self.p1 += max(row) - min(row)

    def part_02(self):
        for row in selfdata:
            for idx, i in enumerate(row):
                for j in row[idx+1:]:
                    m = max([i, j])
                    n = min([i, j])
                    if m%n==0:
                        self.p2 += m//n
