#! /usr/bin/env python
# coding: utf-8
from colorama import init, Fore
init(autoreset=True)
from controllers.Category import *
from controllers.Product import *
from common import constants as const
from views import Program as pr
from views.View import *
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
            self.connect_user(response)

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
            const.USER = result[0][0]
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
        print(products)
        request = "INSERT INTO Product (\
            product_name, product_desc, product_store, product_url, product_nutriscore, nutriscore_grade \
            ) VALUES (%s, %s, %s, %s, %s, %s)"
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
            print(err)

    def get_products_by_category(self, choice):
        request = "SELECT id, product_name, product_desc, product_store, product_url, product_nutriscore, \
                nutriscore_grade FROM Product \
                INNER JOIN Category_product ON Product.id = Category_product.id_product \
                WHERE id_category = %s"
        self.cursor.execute(request, (choice,))
        result = self.cursor.fetchall()
        return result

    def get_category_by_product(self, choice):
        request = "SELECT id FROM Category \
                INNER JOIN Category_product ON Category.id = Category_product.id_category \
                WHERE id_product = %s"
        self.cursor.execute(request % choice)
        result = self.cursor.fetchone()
        return result

# ----------------------------------------------------------------------------
# ------------------------------- SUBSTITUTE ---------------------------------
# ----------------------------------------------------------------------------

    def comparison_products(self, nutri, id_category):
        request = "SELECT * FROM Product \
                INNER JOIN Category_product ON Product.id = Category_product.id_product \
                WHERE product_nutriscore < %s AND id_category = %s"
        self.cursor.execute(request, (nutri, id_category))
        result = self.cursor.fetchall()
        return result

    def save_product(self, id_product):
        check = "SELECT * FROM User_product WHERE id_user = '%s' AND id_product = '%s'"
        self.cursor.execute(check % (const.USER, id_product))
        checked = self.cursor.fetchall()
        if len(checked) > 0:
            print('----------------------------------------------------')
            print(Fore.RED + 'Le produit a déjà été enregistré en base de données.')
            print('----------------------------------------------------')
        else:
            request =  "INSERT INTO User_product (id_user, id_product) \
                        VALUES ( \
                            (SELECT id FROM User WHERE id = %s), \
                            (SELECT id FROM Product WHERE id = %s) \
                        )"
            self.cursor.execute(request, (const.USER, id_product))
            self.connection.commit()
            View.save_product()

    def get_substitute_saved(self):
        request = "SELECT * FROM Product \
                INNER JOIN User_product ON Product.id = User_product.id_product \
                WHERE User_product.id_user = %s"
        self.cursor.execute(request, (const.USER,))
        result = self.cursor.fetchall()
        return result

    def delete_ref_substitute(self, id_substitute):
        request = "DELETE FROM User_product WHERE id_user = %s"
        self.cursor.execute(request, (id_substitute,))
        self.connection.commit()