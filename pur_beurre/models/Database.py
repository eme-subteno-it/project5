#! /usr/bin/env python
# coding: utf-8
import mysql.connector


class Database:

    user = 'root'
    password = 'coffee61'
    host = 'localhost'
    dbname = 'elevage'

    @staticmethod
    def db_connect():
        connexion = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=dbname,
            auth_plugin='mysql_native_password',
        )
        connexion.close()

        return connexion
    
    # db = _mysql.connect(host="localhost", user="root", port=3306, password="root", db="project5")
    # config = {
    # 'user': 'root',
    # 'password': 'root',
    # 'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    # 'host': 'localhost',
    # 'database': 'project5',
    # # 'raise_on_warnings': True,
    # }
    # print(mysql.connector.__version__)

    # conn = mysql.connector.connect(**config)
    # conn.close()