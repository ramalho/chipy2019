#!/usr/bin/env python3

import collections
import math
import random
from urllib import parse
import pathlib


BASE_URL = 'https://upload.wikimedia.org/wikipedia/commons/'
LOCAL_PATH = 'img/'

DEFAULT_TARGET_SIZE = 4_000_000
TOLERANCE = .05


def file_name(url):
    url_parts = parse.urlsplit(url)
    path = pathlib.PurePath(url_parts.path)
    return path.parts[-1]


def save(url, octets):
    name = file_name(url)
    save_path = LOCAL_PATH + name 
    with open(save_path, 'wb') as fp:
        fp.write(octets)
    return name


def pick_by_size(target_size):
    selected = filter_by_size(target_size)
    return random.choice(selected)


def filter_by_size(target_size):
    selected = []
    power_of_2 = math.log(target_size, 2)
    with open('jpeg.txt') as fp:
        for line in fp:
            size_field, path = line.strip().split()
            size = int(size_field)
            if abs(power_of_2 - math.log(size, 2)) <= TOLERANCE:
                selected.append((size, path))
            
    return selected


def main(args):
    if len(args) == 1:
        target_size = float(args[0])
    else:
        target_size = DEFAULT_TARGET_SIZE
        
    for size, path in filter_by_size(target_size):
        print(f'{size:_d}\t {path}')


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])