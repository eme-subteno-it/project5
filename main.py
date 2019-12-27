#! /usr/bin/env python
# coding: utf-8
from models import Connexion as co
from models import Database as db
from models import RequestSQL as sq
import mysql.connector

def main():
    # new_user = db.Database()
    db.Database.db_connect()
    db.Database.create_database()
    print(db.Database.cursor)

    connexion = co.Connexion()
    
    connexion.action()
    connexion.save_it()
    connexion.connect()

    sql = sq.RequestSQL()
    sql.save_user()
    sql.view_user()
    

if __name__ == '__main__':
    main()