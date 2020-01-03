#! /usr/bin/env python
# coding: utf-8
from models import Database as db
from models import User as user
import mysql.connector
from mysql.connector import errorcode


class RequestSQL:

    def __init__(self):
        db.Database.connect_user()
        self.connect_db = db.Database.connection
        self.cursor = db.Database.cursor
        self.users = ''

    def save_user(self, response):
        res_email = response['email']
        request = "SELECT * FROM Users WHERE email = '%s'" 
        self.cursor.execute(request % res_email)
        result = self.cursor.fetchall()
        if len(result) > 0:
            print("L'adresse email existe déjà.")
        else:
            request_done = 'INSERT INTO Users (username, email, pass) VALUES (%(username)s, %(email)s, %(password)s)'
            self.cursor.execute(request_done, response)
            self.connect_db.commit()
            print("--------------------------")
            print("Vous êtes bien enregistré en base de données.")
            print("--------------------------")

    def connect_user(self, response):
        res_email = response['email']
        res_pass = response['password']
        request = "SELECT * FROM Users WHERE email = '%s' AND pass = '%s'"
        self.cursor.execute(request % (res_email, res_pass))
        result = self.cursor.fetchall()
        if len(result) == 0:
            print('Cette adresse email ou ce mot de passe ne correspondent pas, veuillez rééssayer.')
        else:
            print("--------------------------")
            print('Vous êtes connectés.')
            print("--------------------------")