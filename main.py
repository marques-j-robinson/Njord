import importlib
from input_request.user_input import UserInput


if __name__ == "__main__":
    u = UserInput()
    module = importlib.import_module(f'Solutions.{u.year}.day{u.day}')
    s = module.Solution()
    s.solve()