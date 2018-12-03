from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re
import time

def get_url(soup):
    try:
        val = soup.find("a", attrs={"class": "dp-widget-link noUdLine"})
        return val['href']
    except:
        return "NULL"

def get_price(soup):
    try:
        data = soup.find("span", attrs={"class": "lfloat product-price"})
        return data.get_text().strip()[5:]
    except:
        return 0.0

def get_snapdeal(isbn):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://www.snapdeal.com/search?keyword='+ isbn + '&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=plth'
    source_code = urlopen(Request(url, headers=headers))
    soup = BeautifulSoup(source_code, 'html.parser')
    snapdeal_data = dict(snapdeal_url = get_url(soup), snapdeal_price = get_price(soup))
    time.sleep(2)
    return snapdeal_data

