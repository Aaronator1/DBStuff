__author__ = 'aaronmsmith'
try:
    import simplejson as json
except ImportError:
    import json

class Fruit(object):

    def __init__(self,name,price):
            self.name=name
            self.price=price


def buildDocument():
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    return prices

def writeJSON(doc, name):
    outfile=open(name,"w")
    json.dump(doc,outfile,indent=4)

def readJSON(name):
    file=open(name,"r")
    fruit=json.loads(file.read())
    file.close()
    return fruit

def readJSONFile():
    # '{"first_name": "Guido", "last_name":"Rossum"}'
    # json_string = open("~/Projects/database_practice/json_data.txt", "r")

    json_file=open("/Users/aaronmsmith/Projects/database_practice/json_data.txt","r")
    json_string=json_file.read()
    json_file.close()

    parsed_json = json.loads(json_string)

    print(parsed_json['first_name'])

    parsed_json['first_name']+= " K"


# writeJSON(buildDocument(),"fruit.txt")
all_fruit= readJSON("fruit.txt")

fruits=[]
for item in all_fruit:
    fruits.append(Fruit(item,all_fruit[item]))

for f in fruits:
    print f.name
    print f.price

