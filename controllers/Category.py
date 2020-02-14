#! /usr/bin/env python
# coding: utf-8
from models import Request as req
from models import APIrequest as api
from views.View import *
from views import Program as pr
from controllers import User as user
from controllers.Product import *
from colorama import init, Fore
init(autoreset=True)


class Category:

    categories_list = []

    @classmethod
    def view(cls):
        sql = req.Request()
        result = sql.get_categories()
        
        View.view_categories(result)
    
    @classmethod
    def get(cls):
        """ To get the categories in database if exists. Else we insert this """
        sql = req.Request()
        result = sql.get_categories()
        if len(result) == 0:
            cls.insert()
        else:
            pr.Program.third_loop = 0
            pr.Program.fourth_loop = 1
            cls.view()

    @classmethod
    def insert(cls):
        """ Get the categories (and products) from API to insert in database """
        res = api.APIrequest()
        # res.get_datas()
        products_categories = res.get_datas()
        products = res.products

        for res in res.categories:
            category_name = res[0]
            cls.categories_list.append(category_name)

        # Add in database
        sql = req.Request()
        sql.set_categories(cls.categories_list)

        # Get the product from API to insert in database
        Product.insert(products_categories, products)

        cls.view()

    @classmethod
    def delete(cls):
        cls.categories_list = []
        sql = req.Request()
        sql.delete_categories()

    @classmethod
    def update(cls):
        nb = 0
        sql = req.Request()
        result = sql.get_categories()

        if not(result):
            print('--------------------------------------------------------------------')
            print(Fore.RED + 'Aucune catégorie présente en base, veuillez poursuivre le programme.')
            print('--------------------------------------------------------------------')
        else:
            sql = req.Request()
            # Delete olds Categories in database 
            sql.delete_categories()

            # Get new Categories in API
            cls.insert()
