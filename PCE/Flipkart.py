from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re
import time

def get_url(soup):
    try:
        data = soup.find("a", attrs={"class": "_2cLu-l"})
        return 'https://www.flipkart.com' + data['href']
    except:
        return "NULL"

def get_price(soup):
    try:
        data = soup.find("div", attrs={"class": "_1vC4OE"})
        return data.get_text().strip()[1:]
    except:
        return 0.0

def get_flipkart(isbn):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://www.flipkart.com/search?q=' + isbn + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
    source_code = urlopen(Request(url, headers=headers))
    soup = BeautifulSoup(source_code, 'html.parser')
    flipkart_data = dict(flipkart_url = get_url(soup), flipkart_price = get_price(soup))
    time.sleep(2)
    return flipkart_data


