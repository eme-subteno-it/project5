#! /usr/bin/env python
# coding: utf-8
# pylint: disable=invalid-name
""" The controllers module containing all actions and treatment of program """

from colorama      import init, Fore
from models        import Request       as req
from models        import APIrequest    as api
from views         import View          as vw
from controllers   import Product       as pro

init(autoreset=True)


class Category:
    """
        Class for manage the categories
        :param arg: The category name
    """

    def __init__(self):
        self.name = ''

    @staticmethod
    def get():
        """ To get the categories in database if exists. Else we insert this """
        sql = req.Request()
        result = sql.get_categories()

        if len(result) == 0:
            res = api.APIrequest()
            res.get_datas()

            cat = req.Request() # New instance
            categories = cat.get_categories()
            vw.View().view_categories(categories)
        else:
            vw.View().view_categories(result)

    def insert(self, name):
        """
            Method for insert the category name in database
            :param arg1: The category name get in API
        """
        self.name = name
        # Add in database
        sql = req.Request()
        sql.set_categories(self.name)
