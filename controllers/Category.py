#! /usr/bin/env python
# coding: utf-8
from models import Request as req
from models import APIrequest as api
from views.View import *
from views import Program as pr
from controllers import User as user
from controllers import Product as pro
from colorama import init, Fore
init(autoreset=True)


class Category:
    """
        Class for manage the categories 
        :param arg: The category name
    """
    
    def __init__(self):
        self.name = ''

    def get(self):
        """ To get the categories in database if exists. Else we insert this """
        sql = req.Request()
        result = sql.get_categories()

        if len(result) == 0:
            res = api.APIrequest()
            res.get_datas()
        else:
            View.view_categories(result)

    def insert(self, name):
        """ 
            Method for insert the category name in database
            :param arg1: The category name get in API
        """
        self.name = name
        # Add in database
        sql = req.Request()
        sql.set_categories(self.name)

    def view(self):
        """  Method called the method class View for displayed the categories """
        sql = req.Request()
        result = sql.get_categories()
        View.view_categories(result)

    def delete(self):
        """ Method for delete the categories in reference table Category_product, Product and Category """
        Product = pro.Product()

        sql = req.Request()
        sql.delete_ref_categories_products()
        Product.delete()
        sql.delete_categories()

    def update(self):
        """ Method to update the datas in the database. She delete the datas and get the new datas in API """
        sql = req.Request()
        result = sql.get_categories()

        if not(result):
            print('--------------------------------------------------------------------')
            print(Fore.RED + 'Aucune catégorie présente en base, veuillez poursuivre le programme.')
            print('--------------------------------------------------------------------')
        else:
            # Delete olds Categories in database 
            self.delete()

            # Get new Categories in API
            self.get()