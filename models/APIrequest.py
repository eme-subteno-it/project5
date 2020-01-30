#! /usr/bin/env python
# coding: utf-8
from colorama import init, Fore
init(autoreset=True)
from  urllib import request
import json
from models import Request as req
from controllers import Category as cat
import random


class APIrequest:

    def __init__(self):
        self.url = 'https://fr.openfoodfacts.org/categories.json'
        self.categories = []
        self.total_products = []
        self.result_parse = False

    def call_api(self):
        res = request.urlopen(self.url).read()
        result = res.decode('utf8')
        self.result_parse = json.loads(result)

    def get_categories(self):
        
        self.call_api()
        nb = 0 # Index for to know what is the product url and comparate with the category choice
        # Management categories for to get a random list 
        response_api = []
        for x in range(60):
            result_categories = self.result_parse['tags'][x]['name']
            response_api.append(result_categories)
        for x in range(30):
            values = random.choice(response_api)

            if values not in self.categories:
                self.categories.append(values)
            else:
                pass

        # # Management Product URL
        # product_category_url = self.result_parse['tags'][cat]['url'] + '.json'
        # nb += 1
        # tuple_product = (nb, product_category_url, result_categories)
        # self.total_products.append(tuple_product)

        # # To send in database
        # categories = cat.Category()
        # categories.insert(self.categories)
 

    # def get_products(self, nb_category):
    #     products = [] # List for add the products

    #     # To get all url and the category_name
    #     for product in self.total_products:
    #         nb = product[0]
    #         product_category_url = product[1]
    #         category_name = product[2]

    #         # If the choice matches with the url, we read the url
    #         if nb_category == nb:
    #             res = request.urlopen(product_category_url).read()
    #             result = res.decode('utf8')
    #             result_parse = json.loads(result)

    #             # To get all products and insert the product list
    #             for key in result_parse['products']: 
    #                 products.append(key['product_name'])
                
    #             # To send the products and the cateogry name in database
    #             select_products = {
    #                 'product_name': products,
    #                 'category_name': category_name
    #             }
    #             product = select_products['product_name']

    #             # Delete the empty products in the product_name list
    #             while '' in product:
    #                 del product[product.index('')]

    #             sql = req.RequestSQL()
    #             sql.check_database_product(select_products)
