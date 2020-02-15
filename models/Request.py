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
        request_done = "INSERT INTO Category (category_name) VALUES (%s)"
        self.cursor.execute(request_done, (response,))
        self.connection.commit()

    def delete_categories(self):
        request = "DELETE FROM Category"
        self.cursor.execute(request)
        self.connection.commit()

# ----------------------------------------------------------------------------
# ------------------------------ PRODUCTS ------------------------------------
# ----------------------------------------------------------------------------

    def delete_products(self):
        request = "DELETE FROM Product"
        self.cursor.execute(request)
        self.connection.commit()

    def get_products(self, choice_product):
        request = "SELECT * FROM Product WHERE id = %s"
        self.cursor.execute(request, (choice_product,))
        result = self.cursor.fetchall()

        return result

    def check_products(self, name):
        request = "SELECT product_name FROM Product WHERE product_name = %s"
        self.cursor.execute(request, (name,))
        result = self.cursor.fetchall()
        
        return result

    def set_products(self, products):
        request = "INSERT INTO Product (\
            product_name, product_desc, product_store, product_url, product_nutriscore \
            ) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(request, products)
        self.connection.commit()

# ----------------------------------------------------------------------------
# ------------------------ CATEGORY_PRODUCTS ---------------------------------
# ----------------------------------------------------------------------------
    def delete_ref_categories_products(self):
        request = "DELETE FROM Category_product"
        self.cursor.execute(request)
        self.connection.commit()


    def set_products_categories(self, products_categories):
        """ Add the id's products and categories in reference table """
        products = products_categories['product_name']
        categories = products_categories['category_name']

        try:
            request_all = "INSERT INTO Category_product (id_category, id_product) \
                VALUES ( \
                    (SELECT id FROM Category WHERE category_name = %s), \
                    (SELECT id FROM Product WHERE product_name = %s) \
                )"
            self.cursor.execute(request_all, (categories, products))
            self.connection.commit()
        except mysql.connector.Error as err:
            pass

    def get_products_by_category(self, choice):
        request = "SELECT id, product_name FROM Product \
                INNER JOIN Category_product ON Product.id = Category_product.id_product \
                WHERE id_category = %s"
        self.cursor.execute(request, (choice,))
        result = self.cursor.fetchall()
        return result
