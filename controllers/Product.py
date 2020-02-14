#! /usr/bin/env python
# coding: utf-8
from models import Request as req
from models import APIrequest as api


class Product:

    products_list = []
    choice_category = 0

    @classmethod
    def view(cls):
        sql.req.Request()
        result = sql.get_products()
        # Gestion de récupération d'id pour ensuite pouvoir afficher les bons produits. 

    @classmethod
    def get(cls, choice_category):
        # We give a value at choice_category
        cls.choice_category = choice_category

        # Check in database if products exist
        sql = req.Request()
        sql.check_category_product_table()

    @classmethod
    def insert(cls, products_categories, products):
        """ Insert Products from API to database """

        # cls.products_list.append(products)
        
        # Add in database
        sql = req.Request()
        sql.set_products(products_categories, products)

    def delete():
        pass

    def update():
        pass
    