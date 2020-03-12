#! /usr/bin/env python
# coding: utf-8
# pylint: disable=invalid-name
""" The views module containing all views of program """

import sys

from colorama         import init, Fore
from models           import Database    as db
from controllers      import User        as us
from controllers      import Category    as cat
from controllers      import Product     as pro
from common           import constants   as const

init(autoreset=True)


class Program:
    """
        Program's Engine containing all loops - ClassMethod
        :param arg1: The first loop containing the connexion to database
        :param arg2: The second loop containing the category's choice
        :param arg3: The third loop containing the product's choice and saved the substitute
        :param arg4: The user's choice
        :param arg5: The user's choice category
        :param arg6: Object APIrequest()
    """

    loop = 1
    second_loop = 0
    third_loop = 0
    choice = 0
    choice_category = 0

    @classmethod
    def start(cls):
        """ Begin the program : To connect the user """

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
                db.Database().create_database()
                db.Database().connect_user()
                us.User().save_user_in_database()
            elif cls.choice == 2:
                db.Database().connect_user()
                us.User().check_the_user()
            else:
                sys.exit()

        while cls.second_loop:
            cls.choice_categories()

        while cls.third_loop:
            cls.choice_products()

    @classmethod
    def choice_categories(cls):
        """
            The menu to substitute a product by choosing a category and view the product.
            Or, to view the products saved.
        """

        action = [
            "1 - Substituer un aliment.",
            "2 - Voir mes aliments substitués.",
            "3 - Quitter le programme"
        ]

        print('--------------------------------------------')
        for act in action:
            print(act)

        cls.choice = int(input('Tapez 1, 2 ou 3 : '))
        print('--------------------------------------------')
        if cls.choice == 1:
            print(Fore.GREEN + 'Choisir une catégorie : ')
            Category = cat.Category()
            Category.get()

            cls.choice_category = int(input('Numéro de la catégorie : '))
            Product = pro.Product()
            Product.get(cls.choice_category) # Display product
            cls.second_loop = 0
            cls.third_loop = 1
        elif cls.choice == 2:
            cls.third_loop = 0
            Product = pro.Product()
            Product.view_substitute_saved()

            # If substitutes saved, the user can delete the substitute's list
            if const.SUBSTITUTE_LIST:
                choice_delete = int(input('Oui (1) ou non (2) : '))
                if choice_delete == 1:
                    Product.delete()
                    print('Liste supprimé !')
                    cls.choice_categories()
                elif choice_delete == 2:
                    cls.choice_categories()
                else:
                    sys.exit()
            else:
                cls.choice_categories()
        else:
            sys.exit()

    @classmethod
    def choice_products(cls):
        """ The menu to choice a product for view the substitute and save it if the user wishes """

        cls.choice_product = int(input('Numéro du produit : '))
        Product = pro.Product()
        Product.display_information_product(cls.choice_product, cls.choice_category)

        print('Souhaitez-vous sauvegarder ce substitut ? ')
        choice_save = int(input('Oui (1) ou non (2) : '))
        if choice_save == 1:
            Product.save()
            cls.choice_categories()
        elif choice_save == 2:
            cls.choice_categories()
        else:
            sys.exit()
