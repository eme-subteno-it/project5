#! /usr/bin/env python
# coding: utf-8
# pylint: disable=invalid-name
""" The models module containing all requests of program """
import json

from urllib         import request
from colorama       import init, Fore
from controllers    import Category     as cat
from controllers    import Product      as pro

init(autoreset=True)



class APIrequest:
    """
        Method for get the datas in the API OpenFoodFacts
        :param arg1: (String) Empty by default, but it will the url called for get the datas
        :param arg2: (List) Empty by default,\
            but it will contain the name of category and her url to reach her products
        :param arg3: False by default, but it will contain the result of API call (the datas)
    """

    def __init__(self):
        self.url = ''
        self.categories = []
        self.result_parse = False
        self.response_api = []

    def call_api(self):
        """ Method to call api by a request GET and return a json result """
        res = request.urlopen(self.url).read()
        result = res.decode('utf8')
        self.result_parse = json.loads(result)

    def get_datas(self):
        """ Method for get all datas (Categories and products) """
        print('---------------------------')
        print(Fore.GREEN + 'Ajout des catégories...')
        print('---------------------------')
        self.url = 'https://fr.openfoodfacts.org/categories.json'
        self.call_api()

        # Management categories for to get a list
        Category = cat.Category()

        for i in range(30):
            result_categories = self.result_parse['tags'][i]['name']
            result_products_urls = self.result_parse['tags'][i]['url'] + '.json'
            self.response_api = [result_categories, result_products_urls]
            self.categories.append(self.response_api)
            Category.insert(result_categories)

        # Management Product URL
        print('-------------------------')
        print(Fore.GREEN + 'Insertion des produits...')
        print('-------------------------')
        for categorie in self.categories:
            category_name = categorie[0]
            url = categorie[1]
            self.url = url
            self.call_api()

            Product = pro.Product()

            for i in range(20):

                try:
                    name = self.result_parse['products'][i]['product_name']
                    store = self.result_parse['products'][i]['stores']
                    desc = self.result_parse['products'][i]['ingredients_text_debug']
                    p_url = self.result_parse['products'][i]['url']
                    nutriscore = self.result_parse['products'][i]['nutriscore_score']
                    nutriscore_grade = self.result_parse['products'][i]['nutriscore_grade']
                except KeyError:
                    name = ''

                if name != '':
                    Product.insert(name, desc, store, p_url, nutriscore, nutriscore_grade, category_name)
                else:
                    pass
