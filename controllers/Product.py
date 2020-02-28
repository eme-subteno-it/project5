#! /usr/bin/env python
# coding: utf-8
from models import Request as req
from models import APIrequest as api
from views.View import *
from views import Program as pr
from common import constants as const
from controllers import User as user
from controllers.Category import *
import random

    
class Product:

    
    def __init__(self):
        self.id = 0
        self.name = ''
        self.description = ''
        self.store = ''
        self.url = ''
        self.nutriscore = ''
        self.nutriscore_grade = ''
        self.category = ''
    
    def insert(self, name, desc, store, url, nutriscore, nutriscore_grade, category):
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
            

    def get(self, choice_category):
        # Check in database if products exist
        sql = req.Request()
        result = sql.get_products_by_category(choice_category)
        View.view_products(result)

    def delete(self):
        sql = req.Request()
        sql.delete_ref_substitute(const.USER)
        sql.delete_products()

    def display_information_product(self, choice_product, choice_category):
        sql = req.Request()

        # Get the product
        product = sql.get_products(choice_product)
        View.view_informations_products(product)

        for element in product:
            nutri = element[5]

        # Get the substitute
        substitutes = sql.comparison_products(nutri, choice_category)

        if substitutes:
            substitute = random.choice(substitutes)
            self.id = substitute[0]
            View.view_substitute(substitute)
        else:
            self.id = choice_product
            View.no_view_substitute()

    def save(self):
        sql = req.Request()
        sql.save_product(self.id)

    def view_substitute_saved(self):
        sql = req.Request()
        substitute_saved = sql.get_substitute_saved()

        if substitute_saved:
            View.view_substitute_saved(substitute_saved)
        else:
            View.no_substitute_saved()