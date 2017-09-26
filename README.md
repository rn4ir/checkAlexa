### checkAlexa - a Python script to check the top Alexa rankings for websites.

#### Requirements

- Python 3.x

#### Purpose

The purpose of this script is to download the first million ranked websites, [ranked as per Alexa](https://www.alexa.com/topsites).
It then, by default, lists the first 50 websites, sorted by rank. The script can also accept various arguments for various tasks like:

- Display the first 'n' websites, sorted by rank.
- Save the first 'n' websites, sorted by rank, to an output file.
- Query a domain's current rank.
- Force download the rankings at any given time.

```
$ python checkAlexa.py --help
usage: checkAlexa.py [-h] [-n NUMBER] [-q QUERY] [-o OUTFILE] [-d [DOWNLOAD]]

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        Displays the top 'n' Alexa rankings.
  -q QUERY, --query QUERY
                        Checks a website's current ranking.
  -o OUTFILE, --outfile OUTFILE
                        Saves the output to an external file.
  -d [DOWNLOAD], --download [DOWNLOAD]
                        Download the latest Alexa rankings.
```

#### Usage

- Default (first 50 websites)
```
$ python checkAlexa.py
Rank #1         google.com
Rank #2         youtube.com
Rank #3         facebook.com
.
.
.
Rank #49                ok.ru
Rank #50                apple.com
```

- First 'n' rankings
```
$ python checkAlexa.py -n 5
Rank #1         google.com
Rank #2         youtube.com
Rank #3         facebook.com
Rank #4         baidu.com
Rank #5         wikipedia.org
```

- Query a domain's rank
```
$ python checkAlexa.py -q github.com
Rank #61        github.com

$ python checkAlexa.py -q netflix.com
Rank #33        netflix.com

$ python checkAlexa.py -q muchbits.com
Domain 'muchbits.com' not found in the first million Alexa rankings.
```

- Save output to a file
  - when `-n` (number of websites/domains) is specified
```
$ python checkAlexa.py -o outfile.txt -n 1000000

Query(1000000 domains) saved to 'outfile.txt'

$ python checkAlexa.py -o outfile.txt

Query(50 domains) saved to 'outfile.txt'
```

- Force a download of the latest Rankings
```
$ python checkAlexa.py -d

Downloading latest Alexa rankings. Please wait..

Download complete. Exiting..
```
