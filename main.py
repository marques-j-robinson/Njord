import os
import sys
import importlib
import requests
from dotenv import load_dotenv


load_dotenv()
SESSION = os.getenv('SESSION')


def user_input():
    event = None
    day = None
    # allow args eg: $ python main.py {event} {day}
    if len(sys.argv) >= 2:
        event = sys.argv[1]
        day = sys.argv[2]
    else:
        # prompt for event
        while event is None:
            event = input('Event (year): ')
            if os.path.isdir(f'Events/{event}') is False:
                print('Event does not exist... Try again.')
                event = None

        # prompt for day
        while day is None:
            day = input('Day: ')
            if os.path.isfile(f'Events/{event}/day{day}.py') is False:
                print('Day does not exist... Try again.')
                day = None
    return [event, day]


def get_puzzle_input(event, day):
    uri = f"http://adventofcode.com/{event}/day/{day}/input"
    res = requests.get(uri, cookies={"session": SESSION})
    return res.text


def cache_layer(event, day):
    if os.path.isdir('cache') is False:
        os.mkdir('cache')
    cache_path = f'cache/{event}_{day}'
    if os.path.isfile(cache_path) is True:
        print('Cached!')
        f = open(cache_path, 'r')
        data = f.read()
    else:
        print('need to get data from server...')
        data = get_puzzle_input(event, day)
        f = open(cache_path, 'a')
        f.write(data)
        f.close()
    return data


def solve(event, day, data):
    module = importlib.import_module(f"Events.{event}.day{day}")
    s = module.Solution(data.strip())
    s.part_01()
    print(s.p1)
    s.part_02()
    print(s.p2)


def main():
    [event, day] = user_input()
    data = cache_layer(event, day)
    solve(event, day, data)


if __name__ == "__main__":
    main()
