import pyperclip
from lib.data_translation import DataTranslation
from lib.puzzle_input import PuzzleInput


class BaseSolution(DataTranslation):

    def __init__(self):
        u = UserInput()
        puzzle_input = PuzzleInput(u.year, u.day)
        self.data = puzzle_input.get()
        self.reset()
    
    def solve(self):
        self.translate()
        self.reset()
        self.part_01()
        self.part_02()

    def reset(self):
        self.res = 0

    def copy_results(self):
        pyperclip.copy(self.res)

    def translate(self):
        """
        Optional method for perform custom translations to the puzzle_input prior to the solution method being executed
        """
        pass

    def part_01(self):
        "Wrapper for the first part of the puzzle"
        pass

    def part_02(self):
        "Wrapper for the second part of the puzzle"
        pass
