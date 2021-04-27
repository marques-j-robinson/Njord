class Solution:

    def __init__(self, data):
        self.p1 = 0
        self.p2 = 0
        self.data = []
        for line in data.split('\n'):
            self.data.append(list(line.strip()))

    def part_01(self):
        r = 0
        c = 0
        while r+1 < len(self.data):
            c += 3
            r += 1
            if self.data[r][c%len(self.data[r])] == '#':
                self.p1 += 1

    def part_02(self):
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        ans = 1
        r = 0
        c = 0
        for (dc, dr) in slopes:
            while r+1 < len(self.data):
                c += dc
                r += dr
                if self.data[r][c%len(self.data[r])] == '#':
                    self.p2 += 1
            ans *= self.p2
        self.p2 = ans


# slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

# G = []
# for line in fileinput.input():
    # G.append(list(line.strip()))

# ans = 1
# for (dc, dr) in slopes:
    # r = 0
    # c = 0
    # score = 0
    # while r+1 < len(G):
        # c += dc
        # r += dr
        # if G[r][c%len(G[r])] == "#":
            # score += 1
    # ans *= score
    # if dc == 3 and dr == 1:
        # print(score)
