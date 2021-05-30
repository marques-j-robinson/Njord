import os
import sys
from shutil import copyfile

from util import ALL_DAYS, UserInput, leading_zero


def copy_temp(e, d):
    copyfile('templates/day.py', f'Events/{e}/day{leading_zero(d)}.py')
    copyfile('templates/day_test.py', f'Events/{e}/day{leading_zero(d)}_test.py')


def create_event(event):
    path = f'Events/{event}'
    is_dir = os.path.isdir(path)
    if is_dir is False:
        os.mkdir(path)
    return is_dir


def main():
    if not os.path.exists('Events'):
        os.makedirs('Events')
    user_input = UserInput()
    event = user_input.event
    day = user_input.day
    if event is not None and day != '':
        create_event(event)
        copy_temp(event, day)
    else:
        is_dir = create_event(event)
        if is_dir is False:
            for day in ALL_DAYS:
                copy_temp(event, day)
        else:
            print('Event already exists...')


if __name__ == "__main__":
    main()
