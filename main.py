import argparse
import importlib
import pyperclip


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


def copy_results(p1, p2):
    "Automatic copy of results to clipboard"
    print(p1)
    if p2 is None or p2 == 0:
        pyperclip.copy(str(p1))
    else:
        print(p2)
        pyperclip.copy(str(p2))


if __name__ == "__main__":
    [year, day] = get_args()
    solve(year, day)
