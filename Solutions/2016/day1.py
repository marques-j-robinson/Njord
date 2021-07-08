from lib.solution import BaseSolution
from lib.util import BaseGrid


class Solution(BaseSolution):

    def translate(self):
        self.data = [(i[0], int(i[1:])) for i in self.data.split(', ')]

    def part_01(self):
        g = Grid()
        for turn, steps in self.data:
            g.change_dir(turn)
            while steps > 0:
                g.move()
                steps -= 1
        self.p1 = g.manhattan_distance()

    def part_02(self):
        g = Grid()
        for turn, steps in self.data:
            g.change_dir(turn)
            while steps > 0:
                g.move()
                if self.p2 == 0 and g.has_seen():
                    self.p2 = g.manhattan_distance()
                g.add_seen()
                steps -= 1


class Grid(BaseGrid):

    cur_dir = '^'

    def change_dir(self, turn):
        if self.cur_dir == '<' and turn == 'R' or self.cur_dir == '>' and turn == 'L':
            self.cur_dir = '^'
        elif self.cur_dir == '^' and turn == 'R' or self.cur_dir == 'v' and turn == 'L':
            self.cur_dir = '>'
        elif self.cur_dir == '>' and turn == 'R' or self.cur_dir == '<' and turn == 'L':
            self.cur_dir = 'v'
        elif self.cur_dir == 'v' and turn == 'R' or self.cur_dir == '^' and turn == 'L':
            self.cur_dir = '<'

    def move(self):
        if self.cur_dir == '^':
            self.up()
        if self.cur_dir == '>':
            self.right()
        if self.cur_dir == 'v':
            self.down()
        if self.cur_dir == '<':
            self.left()
