import argparse


class UserInput:

    def __init__(self):
        parser = self.parser_setup()
        args = parser.parse_args()
        self.year = args.year
        self.day = args.day
        if self.year is None or self.day is None:
            raise Exception('MISSING_REQUIRED_ARGUMENTS')

    def parser_setup(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-y', '--year')
        parser.add_argument('-d', '--day')
        return parser