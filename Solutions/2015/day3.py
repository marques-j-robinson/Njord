from lib.solution import BaseSolution


class Solution(BaseSolution):
    """
    Data Structure -
    Algorithm -
    Runtime -
    """

    def part_01(self):
        g = Grid()
        for direction in self.data:
            g.move(direction)
        self.p1 = len(g.seen)

    def part_02(self):
        grid_a = Grid()
        grid_b = Grid()
        for idx, direction in enumerate(self.data):
            if self.is_even(idx):
                grid_a.move(direction)
            else:
                grid_b.move(direction)
        self.p2 = self.combine(grid_a.seen, grid_b.seen)

    def is_even(self, val):
        return val % 2 == 0

    def combine(self, a, b):
        return len(a + list(set(b) - set(a)))


class Grid:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.seen = ['0,0']

    def move(self, direction):
        if direction == '^':
            self.up()
        elif direction == '>':
            self.right()
        elif direction == 'v':
            self.down()
        elif direction == '<':
            self.left()
        self.add_seen()

    def up(self):
        self.y += 1

    def right(self):
        self.x += 1

    def down(self):
        self.y -= 1

    def left(self):
        self.x -= 1

    def add_seen(self):
        coord = f'{self.x},{self.y}'
        if coord not in self.seen:
            self.seen.append(coord)
