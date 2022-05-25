import importlib
import pyperclip

from input_request.user_input import UserInput
# import puzzle module


def solve(year, day):
    module = importlib.import_module(f'Solutions.{year}.day{day}')
    s = module.Solution(year, day)
    s.solve()
    copy_results(s.p1, s.p2)


def copy_results(p1, p2):
    print(p1)
    if p2 is None or p2 == 0:
        pyperclip.copy(str(p1))
    else:
        print(p2)
        pyperclip.copy(str(p2))


if __name__ == "__main__":
    u = UserInput()
    solve(u.year, u.day)
