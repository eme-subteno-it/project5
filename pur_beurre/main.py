#! /usr/bin/env python
# coding: utf-8
from models import Connexion as co
from models import Database as db
import mysql.connector

def main():
    # config = {
    # 'user': 'root',
    # 'password': 'root',
    # 'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    # 'host': 'localhost',
    # 'database': 'dbOFF',
    # # 'raise_on_warnings': True,
    # }
    # print(mysql.connector.__version__)

    # conn = mysql.connector.connect(**config)
    # conn.close()
    
    
    Database.db_connect()


    connexion = co.Connexion()
    
    connexion.action()
    connexion.save_it()
    connexion.connect()

if __name__ == '__main__':
    main()
