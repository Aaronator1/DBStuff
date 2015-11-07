__author__ = 'aaronmsmith'


class Product(object):


    def __init__(self):
        self.product_no=""
        self.name=""
        self.price=""

    def load(self,product_no,name,price):
        self.product_no=product_no
        self.name=name
        self.price=price