#! /usr/bin/env python
# coding: utf-8
from models.Database import *
from models.User import *
from models import HTTPrequest as http
from models import RequestSQL as req
from common import constants as const


class Program:

    loop = 1
    second_loop = 0
    third_loop = 0
    choice = 0
    http = http.HTTPrequest()

    @classmethod
    def start(cls):
        """ Begin the program : To call MySQL connector to connect user """

        while cls.loop:
            action = ["1 - S'enregistrer", "2 - Se connecter", "3 - Quitter le programme."]
            print('------------------------')
            for act in action:
                print(act)
            print('------------------------')
            cls.choice = int(input('Tapez 1, 2 ou 3 : '))

            if cls.choice == 1:
                const.ROOT = input('Entrez votre identifiant MySQL : ')
                const.PASSWORD = input('Entrez votre mot de passe MySQL : ')
                Database.create_database()
                Database.connect_user()
                User.save_user_in_database()

            elif cls.choice == 2:
                Database.connect_user()
                User.check_the_user()
            else:
                cls.loop = 0
        
        while cls.second_loop:
            cls.poursuit()

        while cls.third_loop:
            cls.view_category()

    @classmethod
    def poursuit(cls):
        action = 'Souhaitez-vous mettre à jour la liste des catégories ?'
        print(action)
        
        cls.choice = int(input('1 - Oui || 2 - Non : '))
        if cls.choice == 1:
            sql = req.RequestSQL()
            sql.check_category_table()
        elif cls.choice == 2:
            cls.second_loop = 0
            cls.third_loop = 1
    
    @classmethod
    def view_category(cls):
        action = ["1 - Substituer un aliment.", "2 - Voir mes aliments substitués.", "3 - Quitter le programme"]
        
        print('--------------------------------------------')
        for act in action:
            print(act)

        product_choice = 0
        cls.choice = int(input('Tapez 1, 2 ou 3 : '))
        print('--------------------------------------------')
        if cls.choice == 1:
            print('Choisir une catégorie : ')
            cls.http.get_categories()
            cls.choice_category = int(input('Numéro de la catégorie : '))
            cls.http.get_products(cls.choice_category)
            cls.choice_product = int(input('Quel aliment souhaitez-vous substituer ? : '))

            # Affiche plusieurs propositions associées à un chiffre.
            # L'utilisateur entre le chiffre correspondant et valide.

            # Proposition d'un substitut, sa description, un magasin où l'acheter et un lien

            # L'utilisateur peut enregistrer le résultat en base s'il le souhaite
        
        # if cls.choice == 2:
        #     cls.http.get_products()
            # Afficher une liste d'aliment correspondant à un numéro. (son id ?)
            # L'utilisateur pourra alors choisir son aliment et voir les informations