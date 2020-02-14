#! /usr/bin/env python
# coding: utf-8
from colorama import init, Fore
init(autoreset=True)
from controllers.Category import *
from controllers.Product import *
from views import Program as pr
from models.Database import *
from models import APIrequest as http
import mysql.connector
from mysql.connector import errorcode


class Request:

    
    def __init__(self, *args, **kwargs):
        Database.connect_user()
        self.connection = Database.connection
        self.cursor = Database.cursor

# ----------------------------------------------------------------------------
# --------------------------------- USERS ------------------------------------
# ----------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------
# ---------------------------- CATEGORIES ------------------------------------
# ----------------------------------------------------------------------------

    def get_categories(self):
        request = "SELECT * FROM Category"
        self.cursor.execute(request)
        result = self.cursor.fetchall()

        return result

    def set_categories(self, response):
        for res in response:
            request_done = "INSERT INTO Category (category_name) VALUES (%s)"
            self.cursor.execute(request_done, (res,))
        self.connection.commit()

    def delete_categories(self):
        request = "DELETE FROM Category"
        self.cursor.execute(request)
        self.connection.commit()

# ----------------------------------------------------------------------------
# ------------------------------ PRODUCTS ------------------------------------
# ----------------------------------------------------------------------------

    def get_products(self):
        request = "SELECT * FROM Category_product"
        self.cursor.execute(request)
        result = self.cursor.fetchall()

        return result

    # def check_category_product_table(self):
    #     select_products = self.get_products()
    #     if len(select_products) == 0:
    #         Product.insert()
    #     else:
    #         for res in select_products:
    #             pr.Program.third_loop = 0
    #             pr.Program.fourth_loop = 1

    #         Product.view()

    def set_products(self, products):
        select_product = self.get_products()
        if len(select_product) == 0:
            for res in products:
                request = "INSERT INTO Product (product_name) VALUES (%s)"
                self.cursor.execute(request, (res,))
                self.connection.commit()
        else:
            exit()

# ----------------------------------------------------------------------------
# ------------------------ CATEGORY_PRODUCTS ---------------------------------
# ----------------------------------------------------------------------------

    def set_products_categories(self, products_categories):
        """ Add the id's products and categories in reference table """

        for res in products_categories:
            products = res['product_name']
            categories = res['category_name']

            for i in products:
                try:
                    request_all = "INSERT INTO Category_product (id_category, id_product) \
                        VALUES ( \
                            (SELECT id FROM Category WHERE category_name = %s), \
                            (SELECT id FROM Product WHERE product_name = %s) \
                        )"
                    self.cursor.execute(request_all, (categories, i))
                    self.connection.commit()
                except mysql.connector.Error as err:
                    pass

    # def get_products(self, choice):
    #     request = "SELECT id_product FROM Category_product WHERE id_category = %s"
    #     self.cursor.execute(request, (choice,))
    #     result = self.cursor.fetchall()

    #     return result

    def get_products_by_category(self, choice):
        request = "SELECT id, product_name FROM Product \
                INNER JOIN Category_product ON Product.id = Category_product.id_product \
                WHERE id_category = %s"
        self.cursor.execute(request, (choice,))
        result = self.cursor.fetchall()
        return result

# Lors du choix de la catégorie, il faut afficher les produits liés à celle-ci. 
# Il faut vérifier que les produits n'existent pas déjà en base (pour éviter les doublons)
# Sinon, les ajouter pour ne pas avoir à recharger tout le json à chaque fois... 
# Après la vérif du nb category == nb, faire une méthode qui vérifie si nous possédons
# les produits en base correspondant à la catégorie cité
