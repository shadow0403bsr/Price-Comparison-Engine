from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re
import time
import mysql.connector
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = 'https://www.flipkart.com/in-high-places/p/itmethpgamvwcw5p?pid=9798129108042&lid=LSTBOK9798129108042NZROT3&marketplace=FLIPKART&srno=b_36_1435&otracker=browse&fm=organic&iid=9726f507-de2e-4b78-953a-c145f3c63ed6.9798129108042.SEARCH'
source_code = urlopen(url)
soup = BeautifulSoup(source_code, 'html.parser')

all_scripts = soup.find_all('script')
offerPrice = soup.find('div',attrs={'class': '_1vC4OE _3qQ9m1'}).get_text().strip()
print(offerPrice)
title = soup.find('span', attrs={'class': '_35KyD6'}).get_text().strip()
print(title)
data = all_scripts[8].get_text().strip()
json_data = json.loads(data, cls=json.JSONDecoder)
print(re.sub("128","256",json_data[0]['image']))
author = soup.find('a',attrs={'class': '_3la3Fn _1zZOAc oZoRPi'}).get_text().strip()
print(author)
details = soup.find('div',attrs={'class':'_3WHvuP'}).get_text().strip()
print(details)