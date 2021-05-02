# Njord
Solutions to Advent of Code.

Njord – The God of Seas and Wealth.

## Setup
- Clone repo
- Create virtual environment `python -m venv venv`
- Activate venv `source venv/bin/activate`
- Install requirements `pip install -r requirements.txt`

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

## Templates
Templates live in `templates/`. Copy the templates when beginning a new solution.

## Tests
Using standard `unittest` module for testsing.
Custom `discover` arguments make the filesystem architecture flexible.


The following are useful testing commands:
- `python -m unittest discover -s Events/2020 -p "*_test.py"` Test all of 2020
- `python -m unittest discover -s Events/2020 -p "*01_test.py"` Test only day 01 of 2020

## TODO
- Write a script to automate solution/test files from the templates
