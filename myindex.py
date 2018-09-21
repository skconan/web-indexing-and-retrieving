import os
import gzip
import constants as CONST
from elasticsearch import Elasticsearch
import sys
import json
import time

def parse_html(file):
    f = gzip.open(file)
    number_of_doc = 0
    res = []
    for i in f:
        jj = json.loads(i)
        number_of_doc += 1
        res.append(jj)
        if number_of_doc%100 == 0:
            print('.', end='')
            sys.stdout.flush()
    print()
    print(number_of_doc, 'documents found..')
    return res


def index_doc(doc):
    myid = doc['Url']
    res = es.index(index=index, doc_type=doctype, id=myid, body=doc)
    return res

# def parse_html_2(file):
#     res = []
#     number_of_doc = 0
#     for root, dirs, files in os.walk(file):
#         for name in files:
#             file_name = os.path.join(root, name)
#             print(file_name)
#     return res

# parse_html_2(CONST.PATH_PROJECT+'\html\html')

start_time = time.time()

file = CONST.PATH_PROJECT+'/webpage.txt.gz'
json_docs = parse_html(file)
es_host = "http://localhost:9200"
index = "ku"
doctype = "webpage"
es = Elasticsearch(es_host)
# es.index(index=index, doc_type=doctype, id=json_docs[0]['Url'], body=json_docs[0])


number_of_doc = 0
for i in json_docs:
    i['Links'] = ''
    index_doc(i)
    number_of_doc += 1
    if number_of_doc % 100 == 0:
        print('.',end='')
print('\n', number_of_doc, 'doc(s) indexed')

end_time = time.time()
print(end_time - start_time)