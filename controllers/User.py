#! /usr/bin/env python
# coding: utf-8
import re
import hashlib
from views import Program as pr
from models import Request as req
from colorama import init, Fore
init(autoreset=True)


class User:
    """ Static Class for displayed the forms to connect or register a user """

    @staticmethod
    def save_user_in_database():
        """ Method displayed a form for register a user """
        form_subscribe = {
            'username': input('Tapez votre prénom : '),
            'email': input('Tapez votre e-mail : '),
            'password': input('Tapez un mot de passe : '),
        }
        confirm_pass = input('Confirmez votre mot de passe : ')
        EMAIL_REGEX = re.compile(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$')

        if not EMAIL_REGEX.match(form_subscribe['email']):
            print("L'email indiqué n'est pas correctement configuré, merci de remplir à nouveau le formulaire.")
        elif form_subscribe['password'] != confirm_pass:
            print('------------------------')
            print(Fore.RED + 'Les deux mots de passe ne correspondent pas, veuillez remplir à nouveau le formulaire.')
        elif form_subscribe['password'] == '':
            print('------------------------')
            print(Fore.RED + 'Mot de passe invalide.')
        else:
            hashed = hashlib.sha256(str(form_subscribe['password']).encode('utf-8')).hexdigest()
            form_subscribe['password'] = hashed
            sql = req.Request()
            sql.save_user(form_subscribe)

    @staticmethod
    def check_the_user():
        """ Method displayed a form for connect a user """
        form_connection = {
            'email': input('E-mail : '),
            'password': input('Mot de passe : '),
        }
        hashed = hashlib.sha256(str(form_connection['password']).encode('utf-8')).hexdigest()
        form_connection['password'] = hashed
        sql = req.Request()
        sql.connect_user(form_connection)
