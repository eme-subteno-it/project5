#! /usr/bin/env python
# coding: utf-8
from colorama import init, Fore
init(autoreset=True)
from common import constants as const
import mysql.connector
from mysql.connector import errorcode

class Database:
    """
        Class to get the connexion to mysql database with the connector and create the database
        :param arg1: (String) Nothing by default, is the cursor for the connection mysql
        :param arg2: (String) Nothing by default, is the object connection of connector mysql
        :param arg3: (Bool) False by default, is an attribute for control the state of connection mysql
    """

    cursor = ''
    connection = ''
    state_db = False

    @classmethod
    def first_connect(cls):
        """ Method for the first connection in the program. Called when the user choose to subscribe. """
        try:
            cls.connection = mysql.connector.connect(
                user=const.ROOT,
                password=const.PASSWORD,
                host=const.HOST,
                raise_on_warnings=True,
            )
            cls.cursor = cls.connection.cursor()
            cls.state_db = True
        except mysql.connector.Error as err:
            print(err)
            if cls.state_db == False:
                print('Please, install mysql on your local server.')
                exit()

    @classmethod
    def connect_user(cls):
        """ Method for connect the user in the program. Called when the user choose to connect. """
        try:
            cls.connection = mysql.connector.connect(
                user='accountdb',
                password='passfordb',
                host=const.HOST,
                database=const.DB_NAME,
                raise_on_warnings=True,
            )
            cls.cursor = cls.connection.cursor()
        except mysql.connector.Error:
            print('---------------------------------------------------------')
            print(Fore.RED + 'Veuillez vous inscrire pour installer la base de données.')
            print('---------------------------------------------------------')
            exit()

    @classmethod
    def create_database(cls):
        """ Method for create the database. Called when the user to connect for the first time. """
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

    