#! /usr/bin/env python
# coding: utf-8
# pylint: disable=invalid-name
""" The models module containing all requests of program """
import mysql.connector

from colorama        import init, Fore
from views           import Program     as pr
from views           import View        as vw
from common          import constants   as const
from models          import Database    as db

init(autoreset=True)


class Request:
    """
        This class containing all sql request
        :param arg1: Method of Database Class for keep the user's connexion
        :param arg2: Attribute of Database Class for use the connector mysql
        :param arg3: Attribute of Database Class for use the connector mysql
    """

    def __init__(self):
        db.Database().connect_user()
        self.connection = db.Database().connection
        self.cursor = db.Database().cursor

# ----------------------------------------------------------------------------
# --------------------------------- USERS ------------------------------------
# ----------------------------------------------------------------------------

    def save_user(self, response):
        """
            Method for save the user in database
            :param arg1: (dict) composed user's informations get in inscription form
        """
        res_email = response['email']
        request = "SELECT * FROM User WHERE email = '%s'"
        self.cursor.execute(request % res_email)
        result = self.cursor.fetchall()
        if len(result) > 0:
            print('----------------------------')
            print(Fore.RED + "L'adresse email existe déjà.")
            print('----------------------------')
        else:
            request_done = 'INSERT INTO User (username, email, pass)\
                        VALUES (%(username)s, %(email)s, %(password)s)'
            self.cursor.execute(request_done, response)
            self.connection.commit()
            print("---------------------------------------------")
            print(Fore.GREEN + "Vous êtes bien enregistré en base de données.")
            print("---------------------------------------------")
            self.connect_user(response)

    def connect_user(self, response):
        """
            Method for connect user
            :param arg1: (dict) composed user's login get in connexion form
        """
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
        """ Method for get the categories in database """
        request = "SELECT * FROM Category"
        self.cursor.execute(request)
        result = self.cursor.fetchall()

        return result

    def set_categories(self, response):
        """
            Method to insert the categories in database
            :param arg1: (list) of categories get in API
        """
        request_done = "INSERT INTO Category (category_name) VALUES (%s)"
        self.cursor.execute(request_done, (response,))
        self.connection.commit()

# ----------------------------------------------------------------------------
# ------------------------------ PRODUCTS ------------------------------------
# ----------------------------------------------------------------------------

    def get_products(self, choice_product):
        """
            Method for get the porducts in database
            :param arg1: (int) Product's id choose by the user
        """
        request = "SELECT * FROM Product WHERE id = %s"
        self.cursor.execute(request, (choice_product,))
        result = self.cursor.fetchall()

        return result

    def check_products(self, name):
        """
            Method for check if the product already exist in database before insertion.
            :param arg1: (string) The product name
        """
        request = "SELECT product_name FROM Product WHERE product_name = %s"
        self.cursor.execute(request, (name,))
        result = self.cursor.fetchall()

        return result

    def set_products(self, products):
        """
            Method for insert the products in database
            :param arg1: (tuple) with all product's informations get in API
        """
        request = "INSERT INTO Product (\
            product_name, product_desc, product_store, product_url, product_nutriscore, nutriscore_grade \
            ) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(request, products)
        self.connection.commit()

# ----------------------------------------------------------------------------
# ------------------------ CATEGORY_PRODUCTS ---------------------------------
# ----------------------------------------------------------------------------

    def set_products_categories(self, products_categories):
        """
            Add the id's products and categories in reference table
            :param arg1: (dict) containing all ids products and categories get in database
        """
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
        """
            Method for get the products by category
            Called for display the products.
            :param arg1: (int) id's category get by the user's choice
        """
        request = "SELECT id, product_name, product_desc, product_store,\
                product_url, product_nutriscore, nutriscore_grade FROM Product \
                INNER JOIN Category_product ON Product.id = Category_product.id_product \
                WHERE id_category = %s"
        self.cursor.execute(request, (choice,))
        result = self.cursor.fetchall()
        return result

# ----------------------------------------------------------------------------
# ------------------------------- SUBSTITUTE ---------------------------------
# ----------------------------------------------------------------------------

    def comparison_products(self, nutri, id_category):
        """
            Method to comparate the products in order to selected the substitute
            :param arg1: (int) The nutriscore of the product selected
            :param arg2: (int) The category's id for comparate the products in the category choose
        """
        request = "SELECT * FROM Product \
                INNER JOIN Category_product ON Product.id = Category_product.id_product \
                WHERE product_nutriscore < %s AND id_category = %s"
        self.cursor.execute(request, (nutri, id_category))
        result = self.cursor.fetchall()
        return result

    def save_product(self, id_product):
        """
            Method to save a substitute with the displayed product's id
            :param arg1: (int) Product's id get in database
        """
        check = "SELECT * FROM User_product WHERE id_user = '%s' AND id_product = '%s'"
        self.cursor.execute(check % (const.USER, id_product))
        checked = self.cursor.fetchall()
        if len(checked) > 0:
            print('----------------------------------------------------')
            print(Fore.RED + 'Le produit a déjà été enregistré en base de données.')
            print('----------------------------------------------------')
        else:
            request = "INSERT INTO User_product (id_user, id_product) \
                        VALUES (%s, %s)"
            self.cursor.execute(request, (const.USER, id_product))
            self.connection.commit()
            vw.View().save_product()

    def get_substitute_saved(self):
        """ Method to get the substitute saved in database """
        request = "SELECT * FROM Product \
                INNER JOIN User_product ON Product.id = User_product.id_product \
                WHERE User_product.id_user = %s"
        self.cursor.execute(request, (const.USER,))
        result = self.cursor.fetchall()
        return result

    def delete_ref_substitute(self, id_user):
        """
            Method to delete the value reference table User_product when the user update the datas
            :param arg1: (int) Get the user's id in constant declared when the user to login
        """
        request = "DELETE FROM User_product WHERE id_user = %s"
        self.cursor.execute(request, (id_user,))
        self.connection.commit()
