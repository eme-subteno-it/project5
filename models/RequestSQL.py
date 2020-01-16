#! /usr/bin/env python
# coding: utf-8
from colorama import init, Fore
init(autoreset=True)
from models import Program as pr
from models.Database import *
from models import HTTPrequest as http


class RequestSQL:

    
    def __init__(self, *args, **kwargs):
        Database.connect_user()
        self.connection = Database.connection
        self.cursor = Database.cursor

    def save_user(self, response):
        res_email = response['email']
        request = "SELECT * FROM User WHERE email = '%s'"
        self.cursor.execute(request % res_email)
        result = self.cursor.fetchall()
        if len(result) > 0:
            print('----------------------------')
            print(Fore.RED + "L'adresse email existe déjà.")
            print('----------------------------')
        else:
            request_done = 'INSERT INTO User (username, email, pass) VALUES (%(username)s, %(email)s, %(password)s)'
            self.cursor.execute(request_done, response)
            self.connection.commit()
            print("---------------------------------------------")
            print(Fore.GREEN + "Vous êtes bien enregistré en base de données.")
            print("---------------------------------------------")
            pr.Program.loop = 0
            pr.Program.second_loop = 1

    def connect_user(self, response):
        res_email = response['email']
        res_pass = response['password']
        request = "SELECT * FROM User WHERE email = '%s' AND pass = '%s'"
        self.cursor.execute(request % (res_email, res_pass))
        result = self.cursor.fetchall()
        if len(result) == 0:
            print('--------------------------------------------------------------------------------')
            print(Fore.RED + 'Cette adresse email ou ce mot de passe ne correspondent pas, veuillez rééssayer.')
            print('--------------------------------------------------------------------------------') 
        else:
            print("--------------------")
            print(Fore.GREEN + 'Vous êtes connectés.')
            print("--------------------")
            pr.Program.loop = 0
            pr.Program.second_loop = 1

    def check_category_table(self):
        request = "SELECT * FROM Category"
        self.cursor.execute(request)
        result = self.cursor.fetchall()
        if len(result) == 0:
            print('-------------------------------------------------------------------')
            print(Fore.RED + 'Aucune catégorie à mettre à jour, veuillez poursuivre le programme.')
            print('-------------------------------------------------------------------')
            pr.Program.second_loop = 0
            pr.Program.third_loop = 1
        else:
            delete = "DELETE FROM Category"
            self.cursor.execute(delete)
            self.connection.commit()
            api = http.HTTPrequest()
            api.get_data()
            pr.Program.second_loop = 0
            pr.Program.third_loop = 1

    def select_category(self, response):
        request = "SELECT category_name FROM Category GROUP BY id"
        self.cursor.execute(request)
        result = self.cursor.fetchall()
        nb = 0
        if len(result) == 0:
            for res in response:
                request_done = "INSERT INTO Category (category_name) VALUES (%s)"
                self.cursor.execute(request_done, (res,))
                print("Inserted : ",self.cursor.rowcount,"row(s) of data.")
            
            self.connection.commit()
            print("-------------------------------------------")
            print(Fore.GREEN + "Catégories enregistrées en base de données.")
            print("-------------------------------------------")

        for res in result:
            nb += 1
            if nb <= 9:
                print('0' + str(nb), '-', res[0])
            else:
                print(nb, '-', res[0])
