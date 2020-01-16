#! /usr/bin/env python
# coding: utf-8
from colorama import init, Fore
init(autoreset=True)
from common import constants as const
import mysql.connector
from mysql.connector import errorcode

class Database:

    cursor = ''
    connection = ''
    state_db = False

    @classmethod
    def first_connect(cls):
        try:
            cls.connection = mysql.connector.connect(
                user=const.ROOT,
                password=const.PASSWORD,
                host=const.HOST,
                raise_on_warnings=True,
            )
            cls.cursor = cls.connection.cursor()
            cls.state_db = True
            if cls.state_db == False:
                print('Please, install mysql on your local server.')
                exit()
        except mysql.connector.Error as err:
            print(err)
            exit()

    @classmethod
    def connect_user(cls):
        try:
            cls.connection = mysql.connector.connect(
                user='accountdb',
                password='passfordb',
                host=const.HOST,
                database=const.DB_NAME,
                raise_on_warnings=True,
            )
            cls.cursor = cls.connection.cursor()
        except mysql.connector.Error as err:
            print('--------------------------------------------------------------------------------')
            print(Fore.RED + str(err))
            print('--------------------------------------------------------------------------------')
            exit()

    @classmethod
    def create_database(cls):
        cls.first_connect()
        try:
            sql = open("data/db_OFF.sql").read()
            cls.cursor.execute(sql)
            print("--------------------------")
            print(Fore.GREEN + "The database is installed.")
            print("--------------------------")
        except mysql.connector.Error as err:
            print('--------------------------------------------------------------------------------')
            print(Fore.RED + str(err))
            print('--------------------------------------------------------------------------------')

    