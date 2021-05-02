import os
import sys
from shutil import copyfile

from util import has_argvs, leading_zero


ALL_DAYS = range(1, 26)


def copy_temp(e, d):
    copyfile('templates/day.py', f'Events/{e}/day{leading_zero(d)}.py')
    copyfile('templates/day_test.py', f'Events/{e}/day{leading_zero(d)}_test.py')


def main():
    if has_argvs():
        event = sys.argv[1]
        day = sys.argv[2]
        copy_temp(event, day)
    else:
        event = sys.argv[1]
        path = f'Events/{event}'
        if os.path.isdir(path) is False:
            os.mkdir(path)
            for day in ALL_DAYS:
                copy_temp(event, day)
        else:
            print('Event already exists...')


if __name__ == "__main__":
    main()
