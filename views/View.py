#! /usr/bin/env python
# coding: utf-8
from models import APIrequest as http
from models import Request as req
from common import constants as const
from controllers.User import *
from controllers.Category import *
from colorama import init, Fore
init(autoreset=True)


class View:
    
    @staticmethod
    def view_categories(response):
        for res in response:
            print(res[0], '-', res[1])

    @staticmethod
    def view_products(response):
        print(' ')
        for res in response:
            print(res[0], '-', res[1])

    @staticmethod
    def view_informations_products(response):
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
        print('Le produit a bien été enregistré.')

    @staticmethod
    def view_substitute_saved(response):
        print(response)
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

    @staticmethod
    def no_substitute_saved():
        print(Fore.RED + "Vous n'avez pas de substituts d'enregistré.")

    @staticmethod
    def no_view_substitute():
        print('---------------------------------------')
        print(Fore.RED + 'Ce produit ne possède pas de substitut.')
        print('---------------------------------------')