import os
import sys
import requests
import pyperclip
from dotenv import load_dotenv
load_dotenv()


SESSION = os.getenv('SESSION')
BASE_URL = "http://adventofcode.com"
ALL_DAYS = range(1, 26)


def leading_zero(n):
    return str(n).zfill(2)


def create_cache_dir():
    if os.path.isdir('cache') is False:
        os.mkdir('cache')


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

    def part_01(self):
        pass

    def part_02(self):
        pass

    def reset(self):
        self.p1 = 0
        self.p2 = 0

    def solve(self, only=None):
        self.reset()
        self.translate()
        if only == 1:
            self.part_01()
        elif only == 2:
            self.part_02()
        else:
            self.part_01()
            self.part_02()

    def copy_to_clipboard(self):
        print(self.p1)
        if self.p2 == 0:
            pyperclip.copy(str(self.p1))
        else:
            print(self.p2)
            pyperclip.copy(str(self.p2))


class UserInput:

    def __init__(self):
        self.valid_events = ['2015', '2016', '2017', '2018', '2019', '2020']
        self.event = None
        self.day = None

        num_argvs = len(sys.argv)
        if num_argvs == 1:
            self.prompt()
        elif  num_argvs == 2:
            self.event = sys.argv[1]
        else:
            self.event = sys.argv[1]
            self.day = sys.argv[2]

    def prompt(self):
        while self.event is None:
            self.event = input('Event (year): ')
            if self.invalid_event():
                print('Invalid Event... Try again.')
                self.event = None
        while self.day is None:
            self.day = input('Day: ')
            if self.invalid_day():
                print('Invalid Day... Try again.')
                self.day = None

    def invalid_event(self):
        if self.event not in self.valid_events:
            return True
        dir_path_exists = os.path.isdir(f'Events/{self.event}')
        if "main" in sys.argv[0]:
            return dir_path_exists is False
        elif "generate" in sys.argv[0]:
            return dir_path_exists

    def invalid_day(self):
        if self.day == '':
            return False
        if int(self.day) not in ALL_DAYS:
            return True
        file_path_exists = os.path.isfile(f'Events/{self.event}/day{leading_zero(self.day)}.py')
        if "main" in sys.argv[0]:
            return file_path_exists is False
        elif "generate" in sys.argv[0]:
            return file_path_exists
