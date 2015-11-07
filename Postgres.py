__author__ = 'aaronmsmith'

from Product_Mod import Product
import psycopg2

conn=psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='roman1'")

cur=conn.cursor()
cur.execute("Select * from products;")

products_in_db=[]
a=Product(1,"boat","2.0")
results=cur.fetchall()
for record in results:
    products_in_db.append(Product(record[0],record[1],record[2]))



# for record in cur:
#     products.append(Product.Product(record))
#     # record[0]