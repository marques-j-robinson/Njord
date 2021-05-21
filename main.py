import importlib
from util import UserInput, leading_zero


print('hi')


def main():
    x = UserInput()
    module = importlib.import_module(f"Events.{x.event}.day{leading_zero(x.day)}")
    s = module.Solution(x.event, x.day)
    s.solve()
    s.copy_to_clipboard()


if __name__ == "__main__":
    main()
