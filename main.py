import argparse
import importlib
from lib.util import copy_results


def get_args():
    parser = parser_setup()
    args = parser.parse_args()
    year = args.year
    day = args.day
    if year is None or day is None:
        raise Exception('MISSING_REQUIRED_ARGUMENTS')
    return [year, day]


def parser_setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--year')
    parser.add_argument('-d', '--day')
    return parser


def solve(year, day):
    module = importlib.import_module(f'Solutions.{year}.day{day}')
    s = modlue.Solution(year, day)
    s.solve()
    copy_results(s.p1, s.p2)


if __name__ == "__main__":
    [year, day] = get_args()
    solve(year, day)
