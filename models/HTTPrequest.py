#! /usr/bin/env python
# coding: utf-8
from  urllib import request
import json


class HTTPrequest:

    def __init__(self):
        self.url = 'https://fr.openfoodfacts.org/categories.json'
    
    def get_data(self):
        res = request.urlopen(self.url).read()
        result = res.decode('utf8')
        result_parse = json.loads(result)
        print('Téléchargement des catégories.')

        for cat in range(1, 20):
            category_name = result_parse['tags']
            print(category_name)

