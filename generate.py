import os
import sys
from shutil import copyfile

from util import has_argvs, leading_zero


ALL_DAYS = range(1, 26)


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
    if has_argvs():
        event = sys.argv[1]
        day = sys.argv[2]
        create_event(event)
        copy_temp(event, day)
    else:
        event = sys.argv[1]
        is_dir = create_event(event)
        if is_dir is False:
            for day in ALL_DAYS:
                copy_temp(event, day)
        else:
            print('Event already exists...')


if __name__ == "__main__":
    main()
