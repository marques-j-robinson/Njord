import os
import sys
import requests
import pyperclip
from dotenv import load_dotenv
load_dotenv()


SESSION = os.getenv('SESSION')
BASE_URL = "http://adventofcode.com"


class UserInput:

    def __init__(self):
        self.event = None
        self.day = None
        if self.has_argvs():
            self.event = sys.argv[1]
            self.day = sys.argv[2]
        else:
            self.prompt()

    def has_argvs(self):
        return len(sys.argv) >= 2

    def prompt(self):
        while self.event is None:
            self.event = input('Event (year): ')
            if self.invalid_event():
                print('Event does not exist... Try again.')
                self.event = None
        while self.day is None:
            self.day = input('Day: ')
            if self.invalid_day():
                print('Day does not exist... Try again.')
                self.day = None

    def invalid_event(self):
        return os.path.isdir(f'Events/{self.event}') is False

    def invalid_day(self):
        return os.path.isfile(f'Events/{self.event}/day{leading_zero(self.day)}.py') is False


class DataFetcher:

    def __init__(self, e=None, d=None):
        self.event = e
        self.e = e
        self.day = d
        self.d = d
        if e is not None and d is not None:
            self.cache_path = f'cache/{e}_{leading_zero(d)}'
            self.get_data()

    def get_data(self):
        create_cache_dir()
        if self.is_cached():
            print('Cached!')
            f = open(self.cache_path, 'r')
            data = f.read()
        else:
            print('need to get data from server...')
            data = self.get_puzzle_input()
            f = open(self.cache_path, 'a')
            f.write(data)
            f.close()
        self.data = data.strip()

    def is_cached(self):
        return os.path.isfile(self.cache_path) is True

    def get_puzzle_input(self):
        uri = f"{BASE_URL}/{self.e}/day/{self.d}/input"
        res = requests.get(uri, cookies={"session": SESSION})
        return res.text


class DataTranslations(DataFetcher):

    def translate(self):
        pass

    def split_by_empty_line(self):
        self.data = [l.replace('\n', ' ').split(' ') for l in self.data.split('\n\n')]

    def split_by_new_line(self):
        self.data = self.data.split('\n')

    def int_list(self):
        self.data = [int(i) for i in self.data]


class BaseSolution(DataTranslations):

    p1 = 0
    p2 = 0

    def part_01(self):
        pass

    def part_02(self):
        pass

    def solve(self):
        self.translate()
        self.part_01()
        print(self.p1)
        self.part_02()
        print(self.p2)
        self.copy_to_clipboard()

    def copy_to_clipboard(self):
        if self.p2 == 0:
            pyperclip.copy(self.p1)
        else:
            pyperclip.copy(self.p2)


def leading_zero(n):
    return n.zfill(2)


def create_cache_dir():
    if os.path.isdir('cache') is False:
        os.mkdir('cache')
