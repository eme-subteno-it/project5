#! /usr/bin/env python
# coding: utf-8
from models import Database as db
from models import User as user
from models import RequestSQL as req
from models import HTTPrequest as http
import re
import crypt
import mysql.connector
from mysql.connector import errorcode
from hmac import compare_digest as compare_hash


class Program:

    def __init__(self):
        self.loop = 1
        self.screen = 0
        self.choice = 0
        self.user = user.User()
        # self.http = http.HTTPrequest()
        self.start()

    def start(self):
        """ Begin the program : To call MySQL connector to connect user """
        
        action = ["1 - S'enregistrer", "2 - Se connecter"]
        for act in action:
            print(act)
        
        self.choice = int(input('1 ou 2 : '))

        if self.choice == 1:
            db.Database.create_database()
            db.Database.connect_user()
            self.user.save_user_in_database()
            self.loop = 0
            self.screen = 1
        elif self.choice == 2:
            db.Database.connect_user()
            self.user.check_the_user()
            self.loop = 0
            self.screen = 1
        else:
            self.loop = 0

    def poursuit(self):
        action = ["1 - Quel aliment souhaitez-vous substituer ?", "2 - Voir mes aliments substitués."]
        for act in action:
            print(act)

        self.choice = int(input('1 ou 2 : '))

        if self.choice == 1:
            action = input('Sélectionnez la catégorie : ')
            # Affiche plusieurs propositions associées à un chiffre.
            # self.http.get_data()
            # L'utilisateur entre le chiffre correspondant et valide

            # action = input('Sélectionner l'aliment : )
            # Affiche plusieurs propositions associées à un chiffre.
            # L'utilisateur entre le chiffre correspondant et valide.

            # Proposition d'un substitut, sa description, un magasin où l'acheter et un lien

            # L'utilisateur peut enregistrer le résultat en base s'il le souhaite
        
        if self.choice == 2:
            pass
            # Afficher une liste d'aliment correspondant à un numéro. (son id ?)
            # L'utilisateur pourra alors choisir son aliment et voir les informations
