from lib.data_translation import DataTranslation
from lib.puzzle_input import PuzzleInput


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

    def translate(self):
        "Optional method for perform custom translations to the puzzle_input"
        pass

    def part_01(self):
        "Wrapper for the first part of the puzzle"
        pass

    def part_02(self):
        "Wrapper for the second part of the puzzle"
        pass
