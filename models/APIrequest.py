#! /usr/bin/env python
# coding: utf-8
from colorama import init, Fore
init(autoreset=True)
from  urllib import request
import json
from common import constants as const
from models import Request as req
from controllers import Category as cat
from controllers import Product as pro
from colorama import init, Fore
init(autoreset=True)


class APIrequest:

    def __init__(self):
        self.url = ''
        self.categories = []
        self.url_products = []
        self.result_parse = False
        self.products = []

    def call_api(self):
        res = request.urlopen(self.url).read()
        result = res.decode('utf8')
        self.result_parse = json.loads(result)

    def get_datas(self):
        print('---------------------------')
        print(Fore.GREEN + 'Ajout des catégories...')
        print('---------------------------')
        self.url = 'https://fr.openfoodfacts.org/categories.json'
        self.call_api()

        # Management categories for to get a list
        Category = cat.Category()
        response_api = []
        for x in range(30):
            result_categories = self.result_parse['tags'][x]['name']
            result_products_urls = self.result_parse['tags'][x]['url'] + '.json'
            response_api = [result_categories, result_products_urls]
            self.categories.append(response_api)
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

            for x in range(20): 

                try:
                    name = self.result_parse['products'][x]['product_name']
                    store = self.result_parse['products'][x]['stores']
                    desc = self.result_parse['products'][x]['ingredients_text_debug']
                    code = self.result_parse['products'][x]['code']
                    p_url = self.result_parse['products'][x]['url']
                    nutriscore = self.result_parse['products'][x]['nutriscore_score']
                    nutriscore_grade = self.result_parse['products'][x]['nutriscore_grade']
                except KeyError:
                    name = ''

                if name != '':
                    Product.insert(name, desc, store, p_url, nutriscore, nutriscore_grade, category_name)
                else:
                    pass
