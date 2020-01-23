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
        self.products = []
        self.product_url = ''
        self.nb_product = 0

    def get_categories(self):
        res = request.urlopen(self.url).read()
        result = res.decode('utf8')
        result_parse = json.loads(result)
        data = json.dumps(result_parse)

        for cat in range(30):
            result_categories = result_parse['tags'][cat]['name']
            result_ids = result_parse['tags'][cat]['id']
            self.categories.append(result_categories)

            self.product_url = result_parse['tags'][cat]['url'] + '.json'
            self.nb_product += 1
            tuple_product = (self.nb_product, self.product_url)
            self.products.append(tuple_product)

        sql = req.RequestSQL()
        sql.select_category(self.categories)

    def get_products(self, nb_category):
        number = randrange(len(self.products))
        for product in self.products:
            nb_product = product[0]
            product_url = product[1]

            if nb_category == nb_product:

                res = request.urlopen(product_url).read()
                result = res.decode('utf8')
                result_parse = json.loads(result)
        
                for number in range(8):
                    if result_parse['products'][number]['product_name_fr'] != '':
                        result_products = result_parse['products'][number]['product_name_fr']
                        print('------------------------------------------------------------')
                        print(result_products)

