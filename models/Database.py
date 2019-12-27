#! /usr/bin/env python
# coding: utf-8
import mysql.connector
from mysql.connector import errorcode

class Database:

    user = 'root'
    password = 'coffee61'
    host = 'localhost'
    dbname = 'db_OFF'
    cursor = ''
    connexion = ''
    state_db = False

    @classmethod
    def db_connect(cls):
        
        cls.connexion = mysql.connector.connect(
            user=cls.user,
            password=cls.password,
            host=cls.host,
            database=cls.dbname,
            raise_on_warnings=True,
        )
        cls.cursor = cls.connexion.cursor()

        cls.state_db = True
        if cls.state_db == False:
            print('Please, install mysql on your local server.')
            exit()

    @classmethod
    def create_database(cls):
        try:
            print(cls.cursor)
            with open("data/db_OFF.sql", 'r') as sql_file:
                sqltext = sql_file.read()
                sql_inst = sqltext.split(';')

                for sql in sql_inst:
                    line = sql + ';'
                    cls.cursor.execute(line)

            print("The database is installed.")
        except mysql.connector.Error as err:
            print(err)

    # def __init__(self):
    #     config = {
    #         'user': user,
    #         'password': password,
    #         'host': host,
    #         'bdname': dbname
    #     }
    # @classmethod
    # def __del__(cls):
    #     cls.cursor.close()
    #     cls.connexion.close()
    