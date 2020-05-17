#!/usr/bin/env python
import os
import sys

from twisted.scripts.twistd import run
from os.path import join, dirname
from sys import argv

sys.path.append(os.getcwd())

def main():
    argv[1:1] = ['-n', '-y', join(os.getcwd(), 'scrapyd/txapp.py')]
    run()

if __name__ == '__main__':
    main()
