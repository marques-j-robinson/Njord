from puzzle_input import PuzzleInput


class BaseSolution(DataTranslation):

    def __init__(self, year, day):
        self.year = year
        self.day = day
        self.data = None
        self.p1 = 0
        self.p2 = 0

    def solve(self):
        puzzle_input = PuzzleInput(self.year, self.day)
        self.data = puzzle_input.get()
        self.translate()
        self.reset()
        self.part_01()
        self.part_02()

    def reset(self):
        self.p1 = 0
        self.p2 = 0

    def part_01(self):
        "Wrapper for the first part of the puzzle"
        pass

    def part_02(self):
        "Wrapper for the second part of the puzzle"
        pass


class DataTranslation:

    def translate(self):
        "Optional method for perform custom translations to the input data"
        pass

    def split_by_empty_line(self):
        self.data = [l.replace('\n', ' ').split(' ') for l in self.data.split('\n\n')]

    def split_by_new_line(self):
        self.data = self.data.split('\n')

    def int_list(self):
        self.data = [int(i) for i in self.data]
