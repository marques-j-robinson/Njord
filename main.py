import os
import sys
import importlib

import requests
from dotenv import load_dotenv

load_dotenv()
SESSION = os.getenv('SESSION')


def get_puzzle_input(event, day):
    uri = f"http://adventofcode.com/{event}/day/{day}/input"
    res = requests.get(uri, cookies={"session": SESSION})
    return res.text


def is_event(event):
    return os.path.isdir(f'Events/{event}')


def is_day(event, day):
    return os.path.isfile(f'Events/{event}/day{day}.py')


def is_cache(cache_path):
    return os.path.isfile(cache_path)


def main():
    event = None
    day = None
    data = None

    # allow user to provide args, eg: $ python main.py {event} {day}
    if len(sys.argv) >= 2:
        event = sys.argv[1]
        day = sys.argv[2]

    # prompt user for event
    while event is None:
        event = input('Event (year): ')
        if is_event(event) is False:
            print('Event does not exist... Try again.')
            event = None

    # prompt user for day
    while day is None:
        day = input('Day: ')
        if is_day(event, day) is False:
            print('Day does not exist... Try again.')
            day = None

    # cache layer
    if os.path.isdir('cache') is False:
        os.mkdir('cache')
    cache_path = f'cache/{event}_{day}'
    if is_cache(cache_path) is True:
        print('Cached!')
        f = open(cache_path, 'r')
        data = f.read()
    else:
        print('need to get data from server...')
        data = get_puzzle_input(event, day)
        f = open(cache_path, 'a')
        f.write(data)
        f.close()

    # get module and execute solution
    module = importlib.import_module(f"Events.{event}.day{day}")
    solution = module.Solution(data.strip())
    solution.part_01()
    print(solution.p1)
    solution.part_02()
    print(solution.p2)


if __name__ == "__main__":
    main()
