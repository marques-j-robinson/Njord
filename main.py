import importlib
from util import UserInput, leading_zero


def main():
    user_input = UserInput()
    event = user_input.event
    day = user_input.day

    module = importlib.import_module(f"Events.{event}.day{leading_zero(day)}")
    s = module.Solution(event, day)
    s.solve()
    s.copy_to_clipboard()


if __name__ == "__main__":
    main()
