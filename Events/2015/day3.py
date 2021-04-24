# Psuedo code

# Part 1
# - traverse a 2d grid
# - keep track of how many locations have been visited

# Part 2
# - alternate instructions between two entities
# - keep track of combined how many locations have been visited

class Solution:

    def __init__(self, data):
        self.data = data

    def part_01(self):
        self.res = 0
        grid = Grid()
        for direction in self.data:
            grid.move(direction)
        self.res = len(grid.seen)

    def part_02(self):
        self.res = 0
        grid_a = Grid()
        grid_b = Grid()
        for idx, direction in enumerate(self.data):
            if idx%2==0:
                grid_a.move(direction)
            else:
                grid_b.move(direction)
        self.res = combined(grid_a, grid_b)


class Grid:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.seen = []

    def add_seen(self):
        coord = f"{self.x},{self.y}"
        if coord not in self.seen:
            self.seen.append(coord)

    def move(self, direction):
        self.add_seen()
        if direction == '^':
            self.y += 1
        elif direction == '>':
            self.x += 1
        elif direction == 'v':
            self.y -= 1
        elif direction == '<':
            self.x -= 1


def combined(a, b):
    return len(a.seen + list(set(b.seen) - set(a.seen)))
