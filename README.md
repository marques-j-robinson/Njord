# Njord
Njord – The God of Seas and Wealth.

Solutions for [Advent of Code](https://adventofcode.com/) puzzles.

## Setup
Using Python3.
- Clone repository
- Create virtual environment
- Activate virtual environment
- Install requirements

A note about some of the things that get installed.
- **[pyperclip](https://pypi.org/project/pyperclip/)** auto copy answer, decreases solve time.
- **[requests](https://pypi.org/project/requests/)** fetch data.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** handle session cookie value.

## Data Translation Layer
`BaseSolution` inherits a class called `DataTranslation`.
This allows for common data translations to be described with plain english.
Below is a list of the available translations:
```
- split_by_empty_line
- split_by_new_line
- int_list
```

### Usage
Define a `translate` method on `Solution` and include custom or predefined translations.
The example below will split the data by new line, then perform the custom translation.
```
from lib.solution import BaseSolution


class Solution(BaseSolution):

    def translate(self):
        # Available
        self.split_by_new_line()

        # Custom
        self.data = [(d[0], int(d[1:len(d)])) for d in self.data.split(', ')]
```

## Running Solutions
`python main.py --year=2015 --day=1`
`python main.py -y 2015 -d 1`
