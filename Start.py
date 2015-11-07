__author__ = 'aaronmsmith'


from boto.dynamodb2.fields import HashKey, RangeKey, GlobalAllIndex
from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb2.table import Table
from boto.dynamodb2.items import Item
import boto

from boto.dynamodb2.table import Table
conn = DynamoDBConnection()
tables = conn.list_tables()
for s in tables['TableNames']:
    print s
print tables['TableNames']

table_name = 'myTable001'
if table_name not in tables['TableNames']:
    Table.create(table_name, schema=[HashKey('firstKey')], throughput={'read': 5, 'write': 2}, global_indexes=[
        GlobalAllIndex('secondKeyIndex', parts=[HashKey('secondKey')], throughput={'read': 5, 'write': 3})], connection=conn)

table = Table(table_name, connection=conn)

with table.batch_write() as batch:
    batch.put_item(data={'firstKey': 'fk01', 'secondKey':'sk001', 'message': '{"firstKey":"fk01", "secondKey":"sk001", "comments": "fk01-sk001"}'})
    # ...
    batch.put_item(data={'firstKey': 'fk74', 'secondKey':'sk112', 'message': '{"firstKey":"fk74", "secondKey":"sk012", "comments": "fk74-sk012"}'})

# members = Table('members')
#
# print members
# s = members.get_item(last='Smith')

# # Create the new user.
# members.put_item(data={
#          'MemberID': '2',
#          'first': 'Melanie',
#          'last': 'Smith'
#      })
