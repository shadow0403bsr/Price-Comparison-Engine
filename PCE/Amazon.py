from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re

def get_url(soup):
    try:
        data = soup.find("a",attrs={"class": "a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})
        return data['href']
    except:
        return "NULL"

def get_price(soup):
    try:
        data = soup.find("span", attrs={"class": "a-size-base a-color-price s-price a-text-bold"})
        if data == None:
            data = soup.find("span", attrs={"class": "a-size-base a-color-price a-text-bold"})
        return data.get_text().strip()
    except:
        return 0

def get_amazon(isbn):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + isbn
    source_code = urlopen(Request(url, headers=headers))
    soup = BeautifulSoup(source_code, 'html.parser')
    amazon_data = dict(amazon_url = get_url(soup), amazon_price = get_price(soup))
    return amazon_data
