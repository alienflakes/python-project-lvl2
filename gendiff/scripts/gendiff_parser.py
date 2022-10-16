#!/usr/bin/env python
import argparse
from gendiff import generate_diff


def parse_arguments():
    """Parse arguments for gendiff parser."""

    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish', help='set format of output')

    args = parser.parse_args()
    return args


def gendiff():
    """CLI for generating stylized diff between two files."""

    args = parse_arguments()
    result = generate_diff(args.first_file, args.second_file, args.format)

    print(result)


def main():
    gendiff()


if __name__ == '__main__':
    main()
