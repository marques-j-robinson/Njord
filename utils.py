import os


def is_event(event):
    return os.path.isdir(f'Events/{event}')


def is_day(event, day):
    return os.path.isfile(f'Events/{event}/day{day}.py')


def is_cache(cache_path):
    return os.path.isfile(cache_path)
