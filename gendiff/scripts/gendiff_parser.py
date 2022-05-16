#!/usr/bin/env python
"""CLI utility that generates diff in given files."""

import argparse
from gendiff.gendiff import generate_diff


def gendiff():
    """Gendiff Parser."""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish', help='set format of output')

    args = parser.parse_args()

    result = generate_diff(args.first_file, args.second_file)

    print(result)


def main():
    """Run Gendiff."""
    gendiff()


if __name__ == '__main__':
    main()
