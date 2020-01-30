#! /usr/bin/env python
# coding: utf-8
from models import Database as db
from models import User as user
import mysql.connector
from mysql.connector import errorcode


class Product:

    product_list = []

    def __init__(self):
        self.id = 1
        self.name = ''
    
    