#!/usr/bin/env python

import urllib.request
import zipfile
import csv

rankings = {}

url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
alexa_zipfile = 'top-1m.csv.zip'
alexa_csvfile = 'top-1m.csv'

urllib.request.urlretrieve(url, alexa_zipfile)

with zipfile.ZipFile(alexa_zipfile, 'r') as alexazip:
    alexazip.extractall()

csv_reader = csv.reader(open(alexa_csvfile, 'r'))
for row in csv_reader:
    key, value = row
    rankings[key] = value

print (rankings)
