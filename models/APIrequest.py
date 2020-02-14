#! /usr/bin/env python
# coding: utf-8
from colorama import init, Fore
init(autoreset=True)
from  urllib import request
import json
from common import constants as const
from models import Request as req
from controllers import Category as cat
import random


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
        self.url = 'https://fr.openfoodfacts.org/categories.json'
        self.call_api()
        
        # Management categories for to get a list 
        response_api = []
        for x in range(30):
            result_categories = self.result_parse['tags'][x]['name']
            result_products_urls = self.result_parse['tags'][x]['url'] + '.json'

            response_api = [result_categories, result_products_urls]
            self.categories.append(response_api)

        # Management Product URL
        total_products = [] # List for add totaly products with her category
        for categorie in self.categories:
            category_name = categorie[0]
            url = categorie[1]
            self.url = url
            self.call_api()
            
            dict_all_products = {}

            for x in range(20): 
                try:
                    product_name = self.result_parse['products'][x]['product_name']
                    product_market = self.result_parse['products'][x]['stores']
                    product_description = self.result_parse['products'][x]['ingredients_text_debug']
                    product_url = self.result_parse['products'][x]['url']
                    product_nutriscore = self.result_parse['products'][x]['nutriscore_score']
                except KeyError:
                    product_name = ''
                    product_market = ''
                    product_description = ''
                    product_url = ''
                    product_nutriscore = '100'
                
                print('*******************************************************')
                print('Product : ', product_name, 'Categorie : ', category_name)
                print('*******************************************************')

                products = {
                    'name': product_name,
                    'market': product_market,
                    'description': product_description,
                    'url': product_url,
                    'nutriscore': product_nutriscore
                }
                print(products)
                print('----------')
                # result = {}
                # for key, value in products.items():
                #     if value not in result.values():
                #         result[key] = value

                dict_all_products = {
                    'product': products,
                    'category_name': category_name,
                }

                # Products with her category
                # products.append(product_name)
                # products = [i for i in products if i != '']
                # products = list(set(products)) # Delete the duplicate element

                # dict_products = {
                #     'product_name': products,
                #     'category_name': category_name
                # }

            # self.products = list(set(self.products + products))
            total_products.append(dict_all_products)
        print(total_products)

        return total_products
