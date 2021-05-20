# Njord
Solutions to [Advent of Code](https://adventofcode.com/).

Njord – The God of Seas and Wealth.

## Getting Started
### Initial Setup
This project is written in Python3.

- Check version `python --version`
- Install python `brew install python` (Only if current version is 2)
- Clone repo `git clone https://github.com/marques-j-robinson/Njord.git && cd Njord`
- Create virtual environment `python -m venv venv`
- Activate venv `source venv/bin/activate`
- Install requirements `pip install -r requirements.txt`

A note about some of the things that get installed.

- **[pyperclip](https://pypi.org/project/pyperclip/)**
auto copy answer, decreases solve time.
- **[requests](https://pypi.org/project/requests/)** fetch data.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**
handle session cookie value.

### Authentication
Create a `.env` file at the projects root.
Input your session cookie from the aoc website `SESSION=xxx`.

## Cache Layer
Built into this project is a cache layer.

When a solution is run the script will first look in `cache/` for the file.
If the file is not there, the script will request the data and then save the data to `cache/`.

## Data Translation Layer
Built into the `BaseSolution` class is a data translation layer.

This allows for some reoccurring data translations to be described with english.
Below is a list of the available translations:

```
- split_by_empty_line
- split_by_new_line
- int_list
```

### Usage
Inside of the `Solution` class, define a `translate` method and include
translations already on the `Solution` class, or create custom ones here.

The example below will split the data by new line, then perform the custom translation.
```
from util import BaseSolution


class Solution(BaseSolution):

    def translate(self):
        # Available
        self.split_by_new_line()

        # Custom
        self.data = [(d[0], int(d[1:len(d)])) for d in self.data.split(', ')]

    def part_01(self):
        ...
```

## Templates
Templates live in `templates/`.
Generate solution files from templates using this script: `generate.py`.

Examples:
- `$ python generate_templates.py 2021` Generate all of 2021
- `$ python generate_templates.py 2021 1` Generate only day 01 of 2021

## Running Solutions
There are a few options when running solutions.
1) `python main.py` will prompt the user for event and day:

```
$ python main.py
Event (year): 2020
Day: 1
need to get data from server...
877971
203481432
```

2) Alternatively, `python main.py 2020 1` will accomplish the same.

```
$ python main.py 2020 1
Cached!
877971
203481432
```

## Tests
Using standard `unittest` module for testsing.
Custom `discover` arguments make the filesystem architecture flexible.


The following are useful testing commands:
- `python -m unittest discover -s Events/2020 -p "*_test.py"` Test all of 2020
- `python -m unittest discover -s Events/2020 -p "*01_test.py"` Test only day 01 of 2020

Useful tip, add this as an alias:

```
pytest() {
    python -m unittest discover -s Events/$1 -p "*$2_test.py"
}
```

With the above added:
- `pytest 2020` Test all of 2020
- `pytest 2020 01` Test only day 01 of 2020

**Note** The leading zero is required here.
