#! /usr/bin/env python
# coding: utf-8
from common import constants as const
import mysql.connector
from mysql.connector import errorcode

class Database:

    user = const.ROOT
    password = const.PASSWORD
    host = const.HOST
    dbname = const.DB_NAME
    cursor = ''
    connection = ''
    state_db = False

    @classmethod
    def first_connect(cls):
        cls.connection = mysql.connector.connect(
            user=cls.user,
            password=cls.password,
            host=cls.host,
            raise_on_warnings=True,
        )
        cls.cursor = cls.connection.cursor()
        cls.state_db = True
        if cls.state_db == False:
            print('Please, install mysql on your local server.')
            exit()

    @classmethod
    def connect_user(cls):
        cls.connection = mysql.connector.connect(
            user=cls.user,
            password=cls.password,
            host=cls.host,
            database=cls.dbname,
            raise_on_warnings=True,
        )
        cls.cursor = cls.connection.cursor()

    @classmethod
    def create_database(cls):
        cls.first_connect()
        try:
            sql = open("data/db_OFF.sql").read()
            cls.cursor.execute(sql)
            print("--------------------------")
            print("The database is installed.")
            print("--------------------------")
        except mysql.connector.Error as err:
            print(err)

    