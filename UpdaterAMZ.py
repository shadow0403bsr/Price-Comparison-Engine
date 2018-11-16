from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re
import time
import mysql.connector

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = 'https://www.amazon.in/Time-Travelers-Wife-AUDREY-NIFFENEGGER/dp/B06XVFVM1D/ref=sr_1_220_twi_pap_4/258-0238419-7820972?s=books&ie=UTF8&qid=1542206512&sr=1-220'
source_code = urlopen(url)
soup = BeautifulSoup(source_code, 'html.parser')

offerPrice = soup.find('span',attrs={'class' : 'a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P'}).get_text().strip()
print(offerPrice)
title = soup.find(id="productTitle").get_text().strip()
print(title)
author = soup.find('span',attrs={'class' : 'author notFaded'})
try:
    print(author.find('span', attrs={'class': 'a-size-medium'}).get_text().split('\n')[0])
except:
    print(author.find('a', attrs={'class': 'a-link-normal'}).get_text().split('\n')[0])
details = soup.find(id="detail_bullets_id").get_text().strip().split('\n')
for var in range(3,8):
    print(details[var])