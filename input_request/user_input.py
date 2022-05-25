import os
import argparse
from dotenv import load_dotenv


class UserInput:

    def __init__(self):
        self.read_puzzle_id_from_env()

    def read_puzzle_id_from_env(self):
        load_dotenv()
        self.year = os.getenv('YEAR')
        self.day = os.getenv('DAY')
        if self.year is None or self.day is None:
            self.get_puzzle_id_from_argparse()
    
    def get_puzzle_id_from_argparse(self):
        self.create_parser()
        args = self.parser.parse_args()
        self.year = args.year
        self.day = args.day
        if self.year is None or self.day is None:
            raise Exception('MISSING_REQUIRED_ARGUMENTS')

    def create_parser(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-y', '--year')
        self.parser.add_argument('-d', '--day')