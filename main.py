#! /usr/bin/env python
# coding: utf-8
from models import Database as db
from models import RequestSQL as sq
from models import Program as pr

import mysql.connector

def main():
    Program = pr.Program()
    loop = Program.loop
    screen = Program.screen


    while loop:
        start = pr.Program()

    while screen:
        poursuit = Program.poursuit()

if __name__ == '__main__':
    main()