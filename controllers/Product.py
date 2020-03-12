#! /usr/bin/env python
# coding: utf-8
# pylint: disable=invalid-name, too-many-instance-attributes, too-many-arguments
""" The controllers module containing all actions and treatment of program """
import random

from models    import Request    as req
from views     import View       as vw
from common    import constants  as const


class Product:
    """
        Class for manage the products and substitutes
        :param arg1: (int) The product id
        :param arg2: (String) The product name
        :param arg3: (String) The product description
        :param arg4: (String) The product store
        :param arg5: (String) The product url in the website Open Food Facts
        :param arg6: (int) The product nutriscore
        :param arg7: (String) The product nutriscore grade
        :param arg8: (String) The product category name
    """

    def __init__(self):
        self.id = 0
        self.name = ''
        self.description = ''
        self.store = ''
        self.url = ''
        self.nutriscore = 100
        self.nutriscore_grade = ''
        self.category = ''

    def insert(self, name, desc, store, url, nutriscore, nutriscore_grade, category):
        """
        Method for insert the products in database compared to category
        :param arg1: (String) The product name
        :param arg2: (String) The product description
        :param arg3: (String) The product store
        :param arg4: (String) The product url in the website Open Food Facts
        :param arg5: (int) The product nutriscore
        :param arg6: (String) The product nutriscore grade
        :param arg7: (String) The product category name
        """
        self.name = name
        self.description = desc
        self.store = store
        self.url = url
        self.nutriscore = nutriscore
        self.nutriscore_grade = nutriscore_grade
        self.category = category

        sql = req.Request()
        result = sql.check_products(self.name)

        if len(result) > 0:
            pass
        else:
            products = (
                self.name,
                self.description,
                self.store,
                self.url,
                self.nutriscore,
                self.nutriscore_grade,
            )
             # Add in database
            sql.set_products(products)

        products_categories = {
            'product_name': self.name,
            'category_name': self.category
        }
        sql.set_products_categories(products_categories)

    @staticmethod
    def get(choice_category):
        """ Method to get the product compared to the choice's user of category """
        # Check in database if products exist
        sql = req.Request()
        result = sql.get_products_by_category(choice_category)
        vw.View().view_products(result)

    @staticmethod
    def delete():
        """ Method to delete the products in the reference table Category_product and Product """
        sql = req.Request()
        sql.delete_ref_substitute(const.USER)

    def display_information_product(self, choice_product, choice_category):
        """
            Method to display the substitute informations thanks
            to choice product and choice category.
            :param arg1: (int) The user's choice of product
            :param arg1: (int) The user's choice of category
        """
        sql = req.Request()

        # Get the product
        product = sql.get_products(choice_product)
        vw.View().view_informations_products(product)

        for element in product:
            nutri = element[5]

        # Get the substitute
        substitutes = sql.comparison_products(nutri, choice_category)

        # Check if the product has a substitute
        if substitutes:
            substitute = random.choice(substitutes)
            self.id = substitute[0]
            vw.View().view_substitute(substitute)
        else:
            self.id = choice_product
            vw.View().no_view_substitute()

    def save(self):
        """ Method to save the substitute """
        sql = req.Request()
        sql.save_product(self.id)

    @staticmethod
    def view_substitute_saved():
        """ Method to view the substitutes saved in database """
        sql = req.Request()
        substitute_saved = sql.get_substitute_saved()

        if substitute_saved:
            vw.View().view_substitute_saved(substitute_saved)
        else:
            vw.View().no_substitute_saved()
