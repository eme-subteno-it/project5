#! /usr/bin/env python
# coding: utf-8
from models import Request as req
from models import APIrequest as api
from views.View import *
from views import Program as pr
from controllers import User as user
from controllers.Category import *

    
class Product:

    
    def __init__(self):
        self.name = ''
        self.description = ''
        self.store = ''
        self.url = ''
        self.nutriscore = ''
        self.category = ''
    
    def insert(self, name, desc, store, url, nutriscore, category):
        self.name = name
        self.description = desc
        self.store = store
        self.url = url
        self.nutriscore = nutriscore
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
            )
            products_categories = {
                'product_name': self.name,
                'category_name': self.category
            }

            # Add in database
            sql.set_products(products)
            sql.set_products_categories(products_categories)
            

    def get(self, choice_category):
        # Check in database if products exist
        sql = req.Request()
        result = sql.get_products_by_category(choice_category)
        View.view_products(result)

    def delete(self):
        sql = req.Request()
        sql.delete_products()

    def display_information(self, choice_product):
        pass
        # sql = req.Request()
        # result = sql.get_products(choice_product)
        # View.view_informations_products(result)
        
        # Faire une recherche par nutriscore pour afficher
        # un substitut au produit sélectionné. 
