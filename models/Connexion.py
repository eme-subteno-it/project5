#! /usr/bin/env python
# coding: utf-8

class Connexion:

    def __init__(self):
        self.one = 1
        self.two = 2
        self.response = {}
        self.info_user = ''

    def action(self):
        action = ["1. S'enregistrer", "2. Se connecter"]
        
        for act in action:
            print(act)

        try:
            self.response = int(input("1 ou 2 : "))
        except ValueError:
            return "Entrée invalide"

    def save_it(self):
        if self.response == self.one:
            # username = input('Tapez votre prénom : ')
            # email = input('Tapez votre e-mail : ')
            # password = input('Tapez votre mot de passe : ')
            # confirm = input('Confirmez votre mot de passe : ')
            form_subscribe = {
                'username': input('Tapez votre prénom : '),
                'email': input('Tapez votre e-mail : '),
                'password': input('Tapez un mot de passe : '),
                'confirm': input('Confirmez votre mot de passe : ')
            }
            self.info_user = form_subscribe

    def connect(self):
        if self.response == self.two:
            form_connexion = [
                "e-mail : ",
                "mot de passe : "
            ]

            for form in form_connexion:
                try:
                    self.info = input(form)
                except ValueError:
                    return "Entrée invalide"
