#! /usr/bin/env python
# coding: utf-8
from models import APIrequest as http
from models import Request as req
from common import constants as const
from controllers.User import *
from controllers.Category import *


class View:

    def view_categories(response):
        for res in response:
            print(res[0], '-', res[1])

    def view_products(response):
        for res in response:
            print(res[0], '-', res[1])

    def view_informations_products(response):
        print(response)