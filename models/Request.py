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

    # def check_category_table(self):
    #     select_categories = self.get_categories()
    #     if len(select_categories) == 0:
    #         Category.insert()
    #     else:
    #         for res in select_categories:
    #             pr.Program.second_loop = 0
    #             pr.Program.third_loop = 1

    #         Category.view()

    def set_categories(self, response):
        for res in response:
            request_done = "INSERT INTO Category (category_name) VALUES (%s)"
            self.cursor.execute(request_done, (res,))
        self.connection.commit()
        pr.Program.second_loop = 0
        pr.Program.third_loop = 1

        # Category.view()

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

    def check_category_product_table(self):
        select_products = self.get_products()
        if len(select_products) == 0:
            Product.insert()
        else:
            for res in select_products:
                pr.Program.third_loop = 0
                pr.Program.fourth_loop = 1

            Product.view()

    def set_products(self, products_categories, products):
        select_product = self.get_products()
        if len(select_product) == 0:
            for res in products:
                request = "INSERT INTO Product (product_name) VALUES (%s)"
                self.cursor.execute(request, (res,))
                self.connection.commit()
            self.set_products_categories(products_categories)
            Category.view()
        else:
            print('Il y a déjà du contenu en base')

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
            # Categories
            # request_category = "SELECT id FROM Category WHERE category_name = %s"
            # self.cursor.execute(request_category )
            # result_category = self.cursor.fetchall()

            # print('Resultat des categories (ID) : ', int(result_category))
            # Products
            # for i in products:
            #     request_product =("""SELECT id FROM Product WHERE product_name = %s""", i)
            #     self.cursor.execute(request_product)
            #     result_product = self.cursor.fetchall()

            #     # Categories and products
            #     for i in result_product:
            #         print(i)
            #         print(result_category)
            #         request_done = "INSERT INTO Category_product (id_category, id_product) VALUES (%s, %s)"
            #         self.cursor.execute(request_done, (result_category, i[0],))


# ----------------------------------------------------------------------------
    # def select_product(self, response):
    #     request = "SELECT product_name FROM Product"
    #     self.cursor.execute(request % response)
    #     result = self.cursor.fetchall()
    #     print(result)
    #     nb = 0
    #     if len(result) > 0:
    #         for res in response:
    #             request_done = "INSERT INTO Product (product_name) VALUES (%(product_name)s)"
    #             self.cursor.execute(request_done, (res,))
    #             nb += 1
    #             print(nb, '-', res)
    #         self.connection.commit()
    #     else:
    #         ('Deja en base')

    #     for res in result:
    #         nb += 1
    #         print(nb, '-', res[0])


    # def insert_product(self, response):
        # Insert product
        # for res in res_product:
        #     print(res_category, res)
        #     request = "INSERT INTO Product (product_name) VALUES (%s)"
        #     get_category_id = "SELECT id FROM Category WHERE category_name = '%s'"
        #     get_product_id = "SELECT id FROM Product WHERE product_name ='%s'"
        #     # Insert ids in the reference table Category_product
        #     request_all = "INSERT INTO Category_product (id_category, id_product) \
        #         VALUES ( \
        #             (SELECT id FROM Category WHERE category_name = %s), \
        #             (SELECT id FROM Product WHERE product_name = %s) \
        #         )"
        #     # request_all = "INSERT INTO Category_product(id_category, id_product) \
        #     #     VALUES (%s, %s)"
        #     print(res_category, res)
            # self.cursor.execute(request % (res_category, res))
            # self.cursor.execute(request_all % (get_category_id, get_product_id))
            # self.connection.commit()

    def get_product(self, response):
        pass

    # def insert_category_product(self, response):
    #     res_product = response['product_name']
    #     res_category = response['category_name']

    #     request = "SELECT product_name FROM Product"
    #     self.cursor.execute(request)
    #     result = self.cursor.fetchall()

    #     # Si la base est vide
    #     if len(result) == 0:
    #         for res in res_product:
    #             request_done = "INSERT INTO Product (product_name) VALUES (%s)"
    #             self.cursor.execute(request_done, (res,))
    #             print('-', res)
    #             self.connection.commit()
    #     else:
    #         for res in res_product:
    #             print(res)
            

        # request = "INSERT INTO Category_product (id_category, id_product) \
        #             VALUES( \
        #                 (SELECT id FROM Category WHERE category_name = %(category_name)s), \
        #                 (SELECT id FROM Product WHERE id = (SELECT MAX(id) FROM Product)) \
        #             )"
        # self.cursor.execute(request, response)
        # self.connection.commit()

# ----------------------------------------------------------------------------
# ------------------------ CATEGORY_PRODUCTS ---------------------------------
# ----------------------------------------------------------------------------

    def get_products(self):
        request = "SELECT * FROM Category_product"
        self.cursor.execute(request)
        result = self.cursor.fetchall()

        return result
# Lors du choix de la catégorie, il faut afficher les produits liés à celle-ci. 
# Il faut vérifier que les produits n'existent pas déjà en base (pour éviter les doublons)
# Sinon, les ajouter pour ne pas avoir à recharger tout le json à chaque fois... 
# Après la vérif du nb category == nb, faire une méthode qui vérifie si nous possédons
# les produits en base correspondant à la catégorie cité
