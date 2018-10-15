from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, Request
from PIL import Image
import re
import codecs

#urlretrieve("https://images-eu.ssl-images-amazon.com/images/I/31K7uwPOZRL.png", "local-filename.png")
#image = Image.open('local-filename.png')
#image.show()

query = input()

key_a = query.replace(" ", "+")
len_a = len(key_a)
key_amazon = ""
product_title_amazon = []
product_url_amazon = []
product_curprice_amazon = []
product_orgprice_amazon = []
for lc in range(0, len_a):
    if(re.match(r'[^a-zA-Z0-9+]',key_a[lc],re.M|re.I)):
        temp = codecs.encode(key_a[lc].encode("utf-8"), "hex")
        key_amazon += "%" + temp.decode("utf-8")
    else:
        key_amazon += key_a[lc]
url_amazon = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + key_amazon
print(url_amazon)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
source_code_amazon = urlopen(Request(url_amazon, headers=headers))
soup_amazon = BeautifulSoup(source_code_amazon, "html.parser")


for titles in soup_amazon.find_all('a', {'class': 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'}):
    try:
        product_title_amazon.append(titles.get('title'))
        if(re.match("/gp",titles.get('href'))):
            product_url_amazon.append('https://www.amazon.in/'+titles.get('href'))
        else:
            product_url_amazon.append(titles.get('href'))
    except AttributeError:
        continue
cnt = 0
for titles in soup_amazon.find_all('div', {'class': 'a-column a-span7'}):
    temp = ""
    check = titles.find_all('span', {'class': 'a-size-base a-color-price s-price a-text-bold'})
    if(check == []):
        product_curprice_amazon.append('Currently Not Available')
        product_orgprice_amazon.append('Currently Not Available')
        continue
    for divs in titles.find_all('span', {'class': 'a-size-base a-color-price s-price a-text-bold'}):
        temp = divs.get_text()
        product_curprice_amazon.append(divs.get_text())
        break
    check = titles.find_all('span', {'class': 'a-size-small a-color-secondary a-text-strike'})
    if (check == []):
        product_orgprice_amazon.append(temp)
    for divs in titles.find_all('span', {'class': 'a-size-small a-color-secondary a-text-strike'}):
        product_orgprice_amazon.append(divs.get_text())
        break
    cnt = cnt + 1
    if (cnt == len(product_title_amazon)):
        break
print(len(product_title_amazon), len(product_url_amazon), len(product_curprice_amazon), len(product_orgprice_amazon))
for lc in range(0, len(product_curprice_amazon)):
    print(product_title_amazon[lc] + "\n" + product_url_amazon[lc] + "\n" + product_curprice_amazon[lc] + "\n" + product_orgprice_amazon[lc] + "\n")

key_f = query
len_f = len(key_f)
key_flipkart = ""
product_title_flipkart = []
product_url_flipkart = []
product_curprice_flipkart = []
product_orgprice_flipkart = []
for lc in range(0, len_f):
    if(re.match(r'[^a-zA-Z0-9]', key_f[lc], re.M|re.I)):
        temp = codecs.encode(key_f[lc].encode("utf-8"), "hex")
        key_flipkart += "%" + temp.decode("utf-8")
    else:
        key_flipkart += key_f[lc]
url_flipkart = 'https://www.flipkart.com/search?q='+key_flipkart+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
print(url_flipkart)
source_code_flipkart = urlopen(Request(url_flipkart, headers=headers))
soup_flipkart = BeautifulSoup(source_code_flipkart, "html.parser")

if(soup_flipkart.find_all('a', {'class': '_2cLu-l'}) == []):
    for titles in soup_flipkart.find_all('div', {'class': '_3wU53n'}):
        try:
            product_title_flipkart.append(titles.get_text())
        except AttributeError:
            continue
    for titles in soup_flipkart.find_all('a', {'class': '_31qSD5'}):
        try:
            product_url_flipkart.append('https://www.flipkart.com' + titles.get('href'))
        except AttributeError:
            continue
else:
    for titles in soup_flipkart.find_all('a', {'class': '_2cLu-l'}):
        try:
            product_title_flipkart.append(titles.get('title'))
            product_url_flipkart.append('https://www.flipkart.com' + titles.get('href'))
        except AttributeError:
            continue


cnt = 0
for titles in soup_flipkart.find_all('div', {'class': '_1uv9Cb'}):
    temp = ""
    for div in titles.find_all('div', {'class': '_1vC4OE'}):
        temp = div.get_text()
        product_curprice_flipkart.append(div.get_text())
        break
    check = titles.find_all('div', {'class': '_3auQ3N'})
    if (check == []):
        product_orgprice_flipkart.append(temp)
    for div in titles.find_all('div', {'class': '_3auQ3N'}):
        product_orgprice_flipkart.append(div.get_text())
        break
    cnt = cnt + 1
    if(cnt == len(product_title_flipkart)):
        break
#<script id="is_script" nonce="11508562286050613601"> has images for products
print(len(product_title_flipkart),len(product_url_flipkart),len(product_curprice_flipkart),len(product_orgprice_flipkart))
for lc in range(0, len(product_title_flipkart)):
    print(product_title_flipkart[lc] + "\n" + product_url_flipkart[lc] + "\n" + product_curprice_flipkart[lc] + "\n" + product_orgprice_flipkart[lc] + "\n")