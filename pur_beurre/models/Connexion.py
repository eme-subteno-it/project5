#! /usr/bin/env python
# coding: utf-8

class Connexion:

    def __init__(self):
        self.one = 1
        self.two = 2
        self.response = ''
        self.info = []

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
            form_subscribe = [
                "Tapez votre prénom : ",
                "Tapez votre e-mail : ",
                "Tapez un mot de passe : ",
                "Confirmez votre mot de passe : "
            ]

            for form in form_subscribe:
                try:
                    self.info = input(form)
                except ValueError:
                    return "Entrée invalide"

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

            print(self.info)
