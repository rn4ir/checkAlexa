#!/usr/bin/env python
"""
A python script to check Alexa rankings of websites.

Requirements:

"""
import sys
import urllib.request
import argparse
import zipfile
import csv
from itertools import islice
from pathlib import Path

rankings = {}

url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
alexa_zipfile = 'top-1m.csv.zip'
alexa_csvfile = 'top-1m.csv'

def download_rankings():
    """
    Function to download the first million ranks.
    Downloads a zipped csv file.
    """
    
    print ("\nDownloading latest Alexa rankings. Please wait..\n")
    urllib.request.urlretrieve(url, alexa_zipfile)

    with zipfile.ZipFile(alexa_zipfile, 'r') as alexazip:
        alexazip.extractall()

def rankings_dict():
    """
    Imports the csv file into an empty dictionary.
    Key: Ranks
    Value: Domain Names
    """
    
    csv_reader = csv.reader(open(alexa_csvfile, 'r'))
    for row in csv_reader:
        key, value = row
        rankings[key] = value

def topn_domains(num):
    """
    Displays the first 'n' ranks
    """

    rankfile = Path(alexa_csvfile)
    if not rankfile.is_file():
        download_rankings()

    rankings_dict()

    if num > 1000000:
        print ("\nQuery out-of-range. Currently displays websites from Rank #1 to Rank #1,000,000.\nExiting..\n")
        sys.exit()

    firstn_list = list(islice(rankings.items(), num))
    for item in firstn_list:
        print ("Rank #" + str(item[0]) + "\t\t" + item[1])

def query_domains(domain):
    """
    Queries a domain and displays it's Alexa rank.
    """

    rankfile = Path(alexa_csvfile)
    if not rankfile.is_file():
        download_rankings()

    rankings_dict()

    if (domain.count('.') > 1) or (domain.count('.') < 1):
        error = "Invalid Domain-Name. Please enter a valid domain name, of the form 'domainname.tld'"
        print (error)
    else:
        check_flag = 0
        for rank, domain_name in rankings.items():
            if domain_name == domain:
                print ("Rank #" + rank + "\t" + domain_name)
                check_flag = 1
                break
        if check_flag == 0:
            print ("Domain '" + domain + "' not found in the first million Alexa rankings.")

def outfile_domains(filename, num):
    """
    Saves the output to an output file.
    """

    rankfile = Path(alexa_csvfile)
    if not rankfile.is_file():
        download_rankings()

    rankings_dict()

    if num > 1000000:
        print ("\nQuery out-of-range. Currently displays websites from Rank #1 to Rank #1,000,000.\nExiting..\n")
        sys.exit()

    fileobj = open(filename, 'w')
    firstn_list = list(islice(rankings.items(), num))
    for item in firstn_list:
        fileobj.write ("Rank #" + str(item[0]) + "\t\t" + item[1] + "\n")
    fileobj.close()
    print ("\nQuery(" + str(num) + " domains) saved to '" + filename + "'\n")

def main():
    """
    Main function.
    Checks command-line arguments and calls the relevant function.
    """

    cli_argparser = argparse.ArgumentParser(description='')
    cli_argparser.add_argument('-n', '--number', type=int, help="Displays the top 'n' Alexa rankings.", required=False)
    cli_argparser.add_argument('-q', '--query', help="Checks a website's current ranking.", required=False)
    cli_argparser.add_argument('-o', '--outfile', help="Saves the output to an external file.", required=False)
    cli_argparser.add_argument('-d', '--download', nargs='?', const=1, help="Download the latest Alexa rankings.", required=False)
    cli_args = cli_argparser.parse_args()

    if (cli_args.number and cli_args.outfile):
        outfile_domains(cli_args.outfile, cli_args.number)
    elif (cli_args.outfile):
        outfile_domains(cli_args.outfile, 50)
    elif (cli_args.number):
        topn_domains(cli_args.number)
    elif (cli_args.query):
        query_domains(cli_args.query)
    elif (cli_args.download):
        download_rankings()
        print ("Download complete. Exiting.. \n")
    else:
        topn_domains(50)

if __name__ == '__main__':
    sys.exit(main())
