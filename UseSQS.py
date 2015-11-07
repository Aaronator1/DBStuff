__author__ = 'aaronmsmith'


import simplejson, boto, uuid
sqs = boto.connect_sqs()

def FillQueue():
    q = sqs.get_queue('my_message_pump')
    message=q.new_message(body="This is a test message")
    q.write


def ReadQueue():
    q = sqs.get_queue('my_message_pump')
    message = q.read()
    if message is not None:   # if it is continue reading until you get a message
        msg_data = message.get_body()
        print msg_data
        # q.delete_message(message)

FillQueue()
ReadQueue()
