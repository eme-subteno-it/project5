#! /usr/bin/env python
# coding: utf-8
from models import Request as req
from models import APIrequest as api
from views.View import *
from views import Program as pr
from controllers import User as user
from controllers.Category import *


class Product:

    products_list = []
    choice_category = 0

    # @classmethod
    # def view(cls):
    #     sql.req.Request()
    #     result = sql.get_products()
    #     # Gestion de récupération d'id pour ensuite pouvoir afficher les bons produits. 

    @classmethod
    def get(cls, choice_category):
        # Check in database if products exist
        sql = req.Request()
        result = sql.get_products_by_category(choice_category)
        View.view_products(result)

        pr.Program.third_loop = 0
        pr.Program.fourth_loop = 1

    @classmethod
    def insert(cls, products_categories, products):
        """ Insert Products from API to database """

        # Add in database
        sql = req.Request()
        sql.set_products(products)
        sql.set_products_categories(products_categories)

    def display_information(cls, choice_product):
        pass

    def delete():
        pass

    def update():
        pass
    