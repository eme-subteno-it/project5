#! /usr/bin/env python
# coding: utf-8
from  urllib import request
import json
from models import RequestSQL as req


class HTTPrequest:

    def __init__(self):
        self.url = 'https://fr.openfoodfacts.org/categories.json'
    
    def get_data(self):
        res = request.urlopen(self.url).read()
        result = res.decode('utf8')
        result_parse = json.loads(result)

        category_name = []
        for cat in range(20):
            result_name = result_parse['tags'][cat]['name']
            category_name.append(result_name)
        sql = req.RequestSQL()
        sql.select_category(category_name)
