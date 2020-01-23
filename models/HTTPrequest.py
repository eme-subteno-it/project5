#! /usr/bin/env python
# coding: utf-8
from  urllib import request
import json
import csv
from models import RequestSQL as req
from random import randint, randrange


class HTTPrequest:

    def __init__(self):
        self.url = 'https://fr.openfoodfacts.org/categories.json'
        self.categories = []
        self.total_products = []

    def get_categories(self):
        res = request.urlopen(self.url).read()
        result = res.decode('utf8')
        result_parse = json.loads(result)
        data = json.dumps(result_parse)
        nb = 0

        for cat in range(30):
            # Management categories
            result_categories = result_parse['tags'][cat]['name']
            result_ids = result_parse['tags'][cat]['id']
            self.categories.append(result_categories)

            # Management Product
            product_category_url = result_parse['tags'][cat]['url'] + '.json'
            nb += 1
            tuple_product = (nb, product_category_url, result_categories)
            self.total_products.append(tuple_product)

        sql = req.RequestSQL()
        sql.select_category(self.categories)

    def get_products(self, nb_category):
        for product in self.total_products:
            nb = product[0]
            product_category_url = product[1]
            category_name = product[2]

            if nb_category == nb:
                res = request.urlopen(product_category_url).read()
                result = res.decode('utf8')
                result_parse = json.loads(result)

                import pdb; pdb.set_trace()
                for res in result_parse['products']:
                    # result_products = result_parse['product
                    print(res)
                    # while result_products != '':
                    #     for prod in range(8):
                    #         result_products = res['products'][prod]['product_name_fr']
                    #         print(result_products)
                
                    #         select_products = {
                    #             'product_name': result_products,
                    #             'category_name': category_name
                    #         }

                sql = req.RequestSQL()
                # sql.select_product(self.select_products)
                sql.insert_category_product(select_products)
