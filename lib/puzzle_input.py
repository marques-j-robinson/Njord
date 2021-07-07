import os
from dotenv import load_dotenv


load_dotenv()
SESSION = os.getenv('SESSION')


class PuzzleInput:

    def __init__(self, year, day):
        self.cache_path = f'cache/{year}_{day}'
        self.req_path = f'http://adventofcode.com/{year}/day/{day}/input'

    def get_puzzle_input(self):
        if self.is_cached():
            return self.read_cache()
        else:
            return self.fetch()

    def is_cached(self):
        return os.path.isfile(self.cache_path) is True

    def fetch(self):
        response = requests.get(self.req_path, cookies={'session': SESSION})
        puzzle_input = response.text
        self.write_cache(puzzle_input)
        return self.format(puzzle_input)

    def write_cache(self, puzzle_input):
        f = open(self.cache_path, 'a')
        f.write(puzzle_input)
        f.close()

    def read_cache(self):
        f = open(self.cache_path, 'r')
        return self.format(f.read())

    def format(self, puzzle_input):
        return puzzle_input.strip()
