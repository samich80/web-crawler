import requests
from bs4 import BeautifulSoup
from lxml import html

parse_file = 'tmp/otput.html'
url = 'https://www.bravebird.de/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text


def download_page(url,headers):
    r = requests.get(url, headers = headers)
    r.encoding = 'utf-8'
    with open(parse_file, 'w', encoding='utf8') as output_file:
      output_file.write(r.text)

def parse_page (filename):
    text = read_file(filename)

  

#Start process
download_page(url,headers)
parse_page (parse_file)




