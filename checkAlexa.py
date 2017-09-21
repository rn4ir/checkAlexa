#!/usr/bin/env python

import urllib.request
import argparse
import zipfile
import csv

rankings = {}
"""
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
"""
cli_argparser = argparse.ArgumentParser(description='')
cli_argparser.add_argument('-n', '--number', type=int, help="Displays the top 'n' Alexa rankings.", required=False)
cli_argparser.add_argument('-q', '--query', help="Checks a website's current ranking.", required=False)
cli_argparser.add_argument('-o', '--outfile', help="Saves the output to an external file.", required=False)
cli_args = cli_argparser.parse_args()

if (cli_args.number):
    print (cli_args.number)
elif (cli_args.query):
    print (cli_args.query)
elif (cli_args.outfile):
    print (cli_args.outfile)
else:
    print ("Else default")
