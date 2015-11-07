__author__ = 'aaronmsmith'
from peewee import *

db = PostgresqlDatabase('postgres', user='postgres',  password='roman1', host='localhost')


class Products(Model):
    product_no=CharField()
    name=CharField()
    price=DecimalField()

    class Meta:
        database=db

for pdct in Products.select():
    print pdct.name

