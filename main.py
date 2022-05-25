import importlib

from .solution import Solution


def solve(year, day):
    module = importlib.import_module(f'Solutions.{year}.day{day}')
    s = module.Solution(year, day)
    s.solve()


if __name__ == "__main__":
    s = Solution()
    s.solve()
