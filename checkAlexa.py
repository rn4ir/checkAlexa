#!/usr/bin/env python

import urllib.request
import argparse
import zipfile
import csv
from itertools import islice

rankings = {}

url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
alexa_zipfile = 'top-1m.csv.zip'
alexa_csvfile = 'top-1m.csv'

"""
urllib.request.urlretrieve(url, alexa_zipfile)

with zipfile.ZipFile(alexa_zipfile, 'r') as alexazip:
    alexazip.extractall()
"""

csv_reader = csv.reader(open(alexa_csvfile, 'r'))
for row in csv_reader:
    key, value = row
    rankings[key] = value

def topn_domains(num):
    firstn_list = list(islice(rankings.items(), num))
    for item in firstn_list:
        print ("Rank #" + str(item[0]) + "\t\t" + item[1])

def query_domains(domain):
    print ("In query_domain()")

def outfile_domains(filename, num):
    print ("In outfile()")

cli_argparser = argparse.ArgumentParser(description='')
cli_argparser.add_argument('-n', '--number', type=int, help="Displays the top 'n' Alexa rankings.", required=False)
cli_argparser.add_argument('-q', '--query', help="Checks a website's current ranking.", required=False)
cli_argparser.add_argument('-o', '--outfile', help="Saves the output to an external file.", required=False)
cli_args = cli_argparser.parse_args()

if (cli_args.number and cli_args.outfile):
    outfile_domains(cli_args.outfile, cli_args.number)
elif (cli_args.outfile):
    outfile_domains(cli_args.outfile, 50)
elif (cli_args.number):
    topn_domains(cli_args.number)
elif (cli_args.query):
    query_domains(cli_args.query)
else:
    topn_domains(50)
