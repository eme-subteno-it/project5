#! /usr/bin/env python
# coding: utf-8
# pylint: disable=invalid-name
""" The views module containing all views of program """

from colorama import init, Fore
from common   import constants  as const

init(autoreset=True)


class View:
    """ Static class call when you need display elements
    like products, categories, substitute, messages ... """

    @staticmethod
    def view_categories(response):
        """
            Method to view the categories
            :param arg1: The list of categories get in database
        """
        for res in response:
            print(res[0], '-', res[1])

    @staticmethod
    def view_products(response):
        """
            Method to view the products
            :param arg1: The list of products compared by the user's choice category get in database
        """
        print(' ')
        print(Fore.GREEN + 'Choisir un produit : ')
        for res in response:
            print(res[0], '-', res[1])

    @staticmethod
    def view_informations_products(response):
        """
            Method to view the products selected informations
            :param arg1: The product's informations get in database
        """

        print(' ')
        print(Fore.YELLOW + 'Vous avez sélectionné le produit suivant : ')
        print(' ')
        for res in response:
            print(Fore.YELLOW + 'Nom : ', res[1])
            print(Fore.YELLOW + 'Description : ', res[2])
            print(Fore.YELLOW + 'Magasin(s) : ', res[3])
            print(Fore.YELLOW + 'URL : ', res[4])
            print(Fore.YELLOW + 'Score nutritionnel : ', res[5])
            print(Fore.YELLOW + 'Nutri-Score : ', res[6])
            print('---------------------------------------------------')

    @staticmethod
    def view_substitute(response):
        """
            Method to view the substitute compared the choice's user product
            :param arg1: The informations of substitute selected
        """
        print(' ')
        print(Fore.GREEN + 'Voici le substitut de ce produit : ')
        print(' ')

        print(Fore.GREEN + 'Nom : ', response[1])
        print(Fore.GREEN + 'Description : ', response[2])
        print(Fore.GREEN + 'Magasin(s) : ', response[3])
        print(Fore.GREEN + 'URL : ', response[4])
        print(Fore.GREEN + 'Score nutritionnel : ', response[5])
        print(Fore.GREEN + 'Nutri-Score : ', response[6])
        print('---------------------------------------------------')

    @staticmethod
    def save_product():
        """ Message for indicate to the user that the substitute is saved """
        print('---------------------------------')
        print(Fore.GREEN + 'Le produit a bien été enregistré.')
        print('---------------------------------')

    @staticmethod
    def view_substitute_saved(response):
        """
            Method for view the substitute saved
            :param arg1: Get the informations of substitutes saved
            in the reference table User_product
        """
        for res in response:
            print(' ')
            print('+-------------------------------------------------------------------------------------------------+')
            print('|', Fore.GREEN + res[1])
            print('+-------------------------------------------------------------------------------------------------+')
            print('| Description : ', res[2])
            print('+-------------------------------------------------------------------------------------------------+')
            print('| Magasin : ', res[3])
            print('+-------------------------------------------------------------------------------------------------+')
            print('| Url : ', res[4])
            print('+-------------------------------------------------------------------------------------------------+')
            print('| Nutriscore : ', res[5])
            print('+-------------------------------------------------------------------------------------------------+')
            print('| Grade nutriscore : ', res[6])
            print('+-------------------------------------------------------------------------------------------------+')
            print(' ')

        print('Souhaitez-vous supprimer votre liste de substituts ?')
        const.SUBSTITUTE_LIST = True

    @staticmethod
    def no_substitute_saved():
        """ Message for indicate to the user he don't have saved substitute """
        print(Fore.RED + "Vous n'avez pas de substituts d'enregistré.")
        const.SUBSTITUTE_LIST = False

    @staticmethod
    def no_view_substitute():
        """ Message for indicate to the user that the product does'nt get a substitute """
        print('---------------------------------------')
        print(Fore.RED + 'Ce produit ne possède pas de substitut.')
        print('---------------------------------------')
