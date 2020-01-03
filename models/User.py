#! /usr/bin/env python
# coding: utf-8
import re
import crypt
import hashlib
from hmac import compare_digest as compare_hash
from models import RequestSQL as req


class User:

    def __init__(self):
        self.request = req.RequestSQL()

    def action(self):
        action = ["1. S'enregistrer", "2. Se connecter"]
        
        for act in action:
            print(act)

        try:
            self.response = int(input("1 ou 2 : "))
        except ValueError:
            return "Entrée invalide"

    def save_user_in_database(self):
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
            print('Les deux mots de passe ne correspondent pas, veuillez remplir à nouveau le formulaire.')
        else:
            # hashed = crypt.crypt(form_subscribe['password'])
            # if not compare_hash(hashed, crypt.crypt(form_subscribe['password'], hashed)):
            #     raise ValueError("Hashed version doesn't validate against original")
            # else:
            hashed = hashlib.sha256(str(form_subscribe['password']).encode('utf-8')).hexdigest()
            form_subscribe['password'] = hashed
            self.request.save_user(form_subscribe)

    def check_the_user(self):
        form_connection = {
            'email': input('E-mail : '),
            'password': input('Mot de passe : '),
        }
        EMAIL_REGEX = re.compile(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$')

        if not EMAIL_REGEX.match(form_connection['email']):
            print("L'email n'a pas été saisie de manière correcte, veuillez vous reconnecter.")
        else:
            hashed = hashlib.sha256(str(form_connection['password']).encode('utf-8')).hexdigest()
            form_connection['password'] = hashed
            self.request.connect_user(form_connection)