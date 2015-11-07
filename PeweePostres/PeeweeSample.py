__author__ = 'aaronmsmith'
# from Peewee tutorial
# http://docs.peewee-orm.com/en/latest/peewee/quickstart.html

from peewee import *
from datetime import date


db = PostgresqlDatabase('postgres', user='postgres',  password='roman1', host='localhost')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database


def create_sample_data():
    db.create_tables([Person, Pet])

    #save method of creating records
    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
    uncle_bob.save() # bob is now stored in the database

    #create method
    grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
    herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)

    #update a record
    grandma.name="Grandma L."
    grandma.save()

    #pets
    bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

    #delete a row
    print herb_mittens.delete_instance()



db.connect()

grandma=Person.select().where(Person.name=='Grandma').get()
print grandma.name
print ""

for person in Person.select():
    print person.name, person.is_relative

print ""

#Query for all pet owners who have a cat
query=Pet.select().where(Pet.animal_type=='cat')
for pet in query:
    print pet.name, pet.owner.name

#more efficient query
query = (Pet
          .select(Pet, Person)
          .join(Person)
          .where(Pet.animal_type == 'cat'))
for pet in query:
     print pet.name, pet.owner.name

#Pet's owned by bob
print ""
print "Pet's owned by Bob"
for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
     print pet.name