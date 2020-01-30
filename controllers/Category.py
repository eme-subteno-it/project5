#! /usr/bin/env python
# coding: utf-8
from models import Database as db
from models import Request as req
from models import APIrequest as api
from controllers import User as user
from colorama import init, Fore
init(autoreset=True)


class Category:

    categories_list = []
    
    @classmethod
    def get(cls):
        sql = req.Request()
        sql.check_category_table()

    @classmethod
    def insert(cls):
        res = api.APIrequest()
        res.get_categories()
        cls.categories_list = res.categories

        # Add in database
        sql = req.Request()
        sql.set_categories(cls.categories_list)

    @classmethod
    def delete(self):
        cls.categories_list = []
        sql = req.Request()
        sql.delete_categories()

    @classmethod
    def update(cls):
        nb = 0
        sql = req.Request()
        result = sql.get_categories()

        print(cls.categories_list)
        if not(result):
            print('--------------------------------------------------------------------')
            print(Fore.RED + 'Aucune catégorie présente en base, veuillez poursuivre le programme.')
            print('--------------------------------------------------------------------')
        else:
            # Get new Categories in API
            res = api.APIrequest()
            res.get_categories()
            cls.categories_list = res.categories

            # Update in database 
            sql.delete_categories()
            sql.set_categories(cls.categories_list)
            # result = sql.set_categories()

            # for res in result:
            #     nb += 1
            #     if nb <= 9:
            #         print('0' + str(nb), '-', res)
            #     else:
            #         print(nb, '-', res)