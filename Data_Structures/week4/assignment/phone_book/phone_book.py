# python3

import random

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    ''' Test Implementations
    n = 12
    queries = [['add', 911, 'police'],['add', 76213, 'Mom'],['add', 17239, 'Bob'],['find', 76213],['find', 910],['find', 911],['del', 910],['del', 911],['find', 911],['find', 76213],['add', 76213, 'daddy'],['find', 76213]]

    n = 8
    queries = [['find', 3839442],['add', 123456, 'me'],['add', 0, 'granny'],['find', 0],['find', 123456],['del', 0],['del', 0],['find', 0]]
    return [Query(each) for each in queries]
    '''
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    '''
        Use Direct Addressing
    '''
    contacts = [None] * 10**7
    response = ''
    result = []

    for query in queries:
        if query.type == 'add':
            contacts[query.number] = query.name
        elif query.type == 'find':
            response = contacts[query.number]
            if response == None:
                response = 'not found'
            result.append(response)
        elif query.type == 'del':
            if contacts[query.number]:
                contacts[query.number] = None
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
