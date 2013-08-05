#!/usr/bin/env python
from sys import argv, exit
import json
import os

# jp.py loads -f FILE
# convert FILE & generate FILE.json

def load_json(fname, encoding = 'uft-8'):
    with open(fname) as f:
        return json.load(f, encoding)

def convert_log_to_json(fname):
    list_data = []
    with open('./posts/' + fname) as f:
        #print f.readlines()
        lines = f.readlines()
    for line in lines:
        #print line[:10], line[11:]
        data = {'name': fname, 'date': line[:10], 'text': line[11:]}
        list_data.append(data)
    #print list_data

    base = os.path.splitext(fname)
    #print base
    with open(base[0] + '.json', 'w') as f:
        for data in list_data:
            f.write(json.dumps(data))

def main():
    #load_json(argv[1])
    convert_log_to_json(argv[1])

    return 0

if __name__ == '__main__':
    exit(main())

