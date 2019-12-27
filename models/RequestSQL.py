#! /usr/bin/env python
# coding: utf-8
from models import Database as db
from models import Connexion as co
import mysql.connector
from mysql.connector import errorcode


connexion = co.Connexion()
class RequestSQL:

    def __init__(self):
        db.Database.db_connect()
        self.connect_db = db.Database.connexion
        self.cursor = db.Database.cursor
        self.response = connexion.info_user
        self.save_user()
    

    def save_user(self):
        for response in self.response:
            request = 'INSERT INTO Users (username, email, password) VALUES (:username, :email, :password)'
            self.cursor.execute(request, response)
            print(self.cursor(raw))
        self.connect_db.commit()
        self.connect_db.close()
    
    def view_user(self):
        request = 'SELECT * FROM Users'
        self.cursor.execute(request)
        coucou = self.cursor.fetchone()
        print(coucou)
        self.connect_db.close()