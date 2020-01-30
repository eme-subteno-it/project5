#! /usr/bin/env python
# coding: utf-8
from models import Database as db
from controllers import User as user
import mysql.connector
from mysql.connector import errorcode


class Substitute:

    substitute_list = []

    def __init__(self):
        self.id = 1
        self.name = ''
    
    