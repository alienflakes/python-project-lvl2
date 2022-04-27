#!/usr/bin/env python
"""CLI utility that generates diff in given files."""

import argparse


def gendiff():
    """Gendiff Parser."""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.parse_args()


def main():
    """Run Gendiff."""
    gendiff()


if __name__ == '__main__':
    main()
