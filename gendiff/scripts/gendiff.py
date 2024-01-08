#!/usr/bin/env python3
import argparse

def foo(first_file, second_file):
    pass

def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    print(args)
    foo(args.first_file, args.second_file)
    
if __name__ == "main":
    main()