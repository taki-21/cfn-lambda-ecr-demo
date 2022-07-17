import sys


def handler(event, context):
    print('event: ', event)
    print('type_of_event: ', type(event))
    return 'Hello from AWS Lambda using Python' + sys.version + '!'
