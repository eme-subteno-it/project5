#! /usr/bin/env python
# coding: utf-8
from colorama import init, Fore
init(autoreset=True)
from controllers.Category import *
from views import Program as pr
from models.Database import *
from models import APIrequest as http


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

    def check_category_table(self):
        request = "SELECT * FROM Category"
        self.cursor.execute(request)
        result = self.cursor.fetchall()
        if len(result) == 0:
            Category.insert()
        else:
            for res in result:
                print(result)
                pr.Program.second_loop = 0
                pr.Program.third_loop = 1

            return result

    def set_categories(self, response):
        nb = 0
        for res in response:
            request_done = "INSERT INTO Category (category_name) VALUES (%s)"
            self.cursor.execute(request_done, (res,))
        self.connection.commit()
        pr.Program.second_loop = 0
        pr.Program.third_loop = 1

    def delete_categories(self):
        request = "DELETE FROM Category"
        self.cursor.execute(request)
        self.connection.commit()

    # def update_categories(self, response):
    #     for res in response:
    #         request = "UPDATE Category SET category_name = (%s)"
    #         self.cursor.execute(request, (res,))
    #         self.connection.commit()


# ----------------------------------------------------------------------------
# ------------------------------ PRODUCTS ------------------------------------
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
    #         print('Deja en base')

    #     for res in result:
    #         nb += 1
    #         print(nb, '-', res[0])

    def check_database_product(self, response):
        request = "SELECT product_name FROM Product"
        self.cursor.execute(request)
        result = self.cursor.fetchall()

        if len(result) == 0:
            self.insert_product(response)
        else:
            self.get_product(response)

    def insert_product(self, response):
        res_product = response['product_name']
        res_category = response['category_name']

        # Insert product
        for res in res_product:
            print(res_category, res)
            request = "INSERT INTO Product (product_name) VALUES (%s)"
            get_category_id = "SELECT id FROM Category WHERE category_name = '%s'"
            get_product_id = "SELECT id FROM Product WHERE product_name ='%s'"
            # Insert ids in the reference table Category_product
            request_all = "INSERT INTO Category_product (id_category, id_product) \
                VALUES ( \
                    (SELECT id FROM Category WHERE category_name = %s), \
                    (SELECT id FROM Product WHERE product_name = %s) \
                )"
            # request_all = "INSERT INTO Category_product(id_category, id_product) \
            #     VALUES (%s, %s)"
            print(res_category, res)
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



# Lors du choix de la catégorie, il faut afficher les produits liés à celle-ci. 
# Il faut vérifier que les produits n'existent pas déjà en base (pour éviter les doublons)
# Sinon, les ajouter pour ne pas avoir à recharger tout le json à chaque fois... 
# Après la vérif du nb category == nb, faire une méthode qui vérifie si nous possédons
# les produits en base correspondant à la catégorie cité
