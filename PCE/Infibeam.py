from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re
import time

def get_url(soup):
    try:
        val = soup.find("div", attrs={"class": "col-md-10 col-xs-8 no-padding-xs"})
        data = val.find("a")
        return 'https://www.infibeam.com' + data['href']
    except:
        return "NULL"

def get_price(soup):
    try:
        data = soup.find("span", attrs={"class": "final-price"})
        return data.get_text().strip()[4:]
    except:
        return 0.0

def get_infibeam(isbn):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://www.infibeam.com/Books/search?q=' + isbn + '&sort=relevance'
    source_code = urlopen(Request(url, headers= headers))
    soup = BeautifulSoup(source_code, 'html.parser')
    infibeam_data = dict(infibeam_url = get_url(soup), infibeam_price = get_price(soup))
    time.sleep(2)
    return infibeam_data


