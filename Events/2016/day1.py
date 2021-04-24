# Psuedo code

# Part 1
# -

# Part 2
# -


class Solution:

    def __init__(self, data):
        self.data = [(d[0], int(d[1:len(d)])) for d in data.split(', ')]

    def part_01(self):
        self.res = 0
        direction = "N"
        G = Grid()
        for turn, steps in self.data:
            direction = turns[f"{direction}{turn}"]
            while steps > 0:
                steps -= 1
                G.move(direction)
                G.add_seen()

        self.res = G.manhattan_distance()

    def part_02(self):
        self.res = 0
        direction = "N"
        G = Grid()
        for turn, steps in self.data:
            direction = turns[f"{direction}{turn}"]
            while steps > 0:
                steps -= 1
                G.move(direction)
                if self.res == 0 and G.has_seen():
                    self.res = G.manhattan_distance()
                G.add_seen()


N = "N"
E = "E"
S = "S"
W = "W"
turns = {
    "NR": E,
    "NL": W,
    "SR": W,
    "SL": E,
    "ER": S,
    "EL": N,
    "WR": N,
    "WL": S,
}


class Grid:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.seen = []

    def add_seen(self):
        coord = self.get_coord()
        if coord not in self.seen:
            self.seen.append(coord)

    def has_seen(self):
        coord = self.get_coord()
        return coord in self.seen

    def get_coord(self):
        return f"{self.x},{self.y}"

    def move(self, direction):
        if direction == N:
            self.y += 1
        elif direction == E:
            self.x += 1
        elif direction == S:
            self.y -= 1
        elif direction == W:
            self.x -= 1

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)
