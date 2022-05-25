import importlib

from .solution import Solution


def solve(year, day):
    module = importlib.import_module(f'Solutions.{year}.day{day}')
    s = module.Solution(year, day)
    s.solve()
    copy_results(s.p1, s.p2)


if __name__ == "__main__":
    s = Solution()
    s.solve()
