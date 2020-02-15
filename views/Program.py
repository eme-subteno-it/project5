#! /usr/bin/env python
# coding: utf-8
from models.Database import *
from models import APIrequest as http
from models import Request as req
from common import constants as const
from controllers.User import *
from controllers import Category as cat
from controllers import Product as pro


class Program:

    loop = 1
    second_loop = 0
    third_loop = 0
    fourth_loop = 0
    choice = 0
    choice_category = 0
    api = http.APIrequest()

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
            cls.update_categories_or_not()

        while cls.third_loop:
            cls.choice_categories()

        while cls.fourth_loop:
            cls.choice_products()

    @classmethod
    def update_categories_or_not(cls):
        action = 'Souhaitez-vous mettre à jour la liste des catégories ?'
        print(action)
        
        cls.choice = int(input('1 - Oui || 2 - Non : '))
        if cls.choice == 1:
            Category = cat.Category()
            Category.update()
            cls.second_loop = 0
            cls.third_loop = 1
        elif cls.choice == 2:
            cls.second_loop = 0
            cls.third_loop = 1
    
    @classmethod
    def choice_categories(cls):
        action = ["1 - Substituer un aliment.", "2 - Voir mes aliments substitués.", "3 - Quitter le programme"]

        print('--------------------------------------------')
        for act in action:
            print(act)

        cls.choice = int(input('Tapez 1, 2 ou 3 : '))
        print('--------------------------------------------')
        if cls.choice == 1:
            print('Choisir une catégorie : ')
            Category = cat.Category()
            Category.get()
        
            cls.choice_category = int(input('Numéro de la catégorie : '))
            Product = pro.Product()
            Product.get(cls.choice_category) # Display product
            cls.third_loop = 0
            cls.fourth_loop = 1

    @classmethod
    def choice_products(cls):
        cls.choice_product = int(input('Choisissez un produit : '))
        Product = pro.Product()
        Product.display_information(cls.choice_product)
