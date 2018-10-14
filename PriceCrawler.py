from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, Request
from PIL import Image
import re
import codecs

#urlretrieve("https://images-eu.ssl-images-amazon.com/images/I/31K7uwPOZRL.png", "local-filename.png")
#image = Image.open('local-filename.png')
#image.show()

key = input()

key_amzn = key.replace(" ", "+")
len_amzn = len(key_amzn)
key_amazon = ""
product_title = []
product_url = []
product_curprice = []
product_orgprice = []
for lc in range(0,len_amzn):
    if(re.match(r'[^a-zA-Z0-9+]',key_amzn[lc],re.M|re.I)):
        temp = codecs.encode(key_amzn[lc].encode("utf-8"), "hex")
        key_amazon += "%" + temp.decode("utf-8")
    else:
        key_amazon += key_amzn[lc]
url_amzn = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + key_amazon
print(url_amzn)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
source_code_amzn = urlopen(Request(url_amzn, headers=headers))
soup_amzn = BeautifulSoup(source_code_amzn, "html.parser")


for titles in soup_amzn.find_all('a', {'class': 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'}):
    try:
        product_title.append(titles.get('title'))
        if(re.match("/gp",titles.get('href'))):
            product_url.append('https://www.amazon.in/'+titles.get('href'))
        else:
            product_url.append(titles.get('href'))
    except AttributeError:
        continue
cnt = 0
for titles in soup_amzn.find_all('div', {'class': 'a-column a-span7'}):
    temp = ""
    check = titles.find_all('span', {'class': 'a-size-base a-color-price s-price a-text-bold'})
    if(check == []):
        product_curprice.append('Currently Not Available')
        product_orgprice.append('Currently Not Available')
        continue
    for divs in titles.find_all('span', {'class': 'a-size-base a-color-price s-price a-text-bold'}):
        temp = divs.get_text()
        product_curprice.append(divs.get_text())
        break
    check = titles.find_all('span', {'class': 'a-size-small a-color-secondary a-text-strike'})
    if(check == []):
        product_orgprice.append(temp)
    for divs in titles.find_all('span', {'class': 'a-size-small a-color-secondary a-text-strike'}):
        product_orgprice.append(divs.get_text())
        break
    cnt = cnt + 1
    if (cnt == len(product_title)):
        break
print(len(product_title),len(product_url),len(product_curprice),len(product_orgprice))
for lc in range(0, len(product_curprice)):
    print(product_title[lc] + "\n" + product_url[lc] + "\n" + product_curprice[lc] + "\n" + product_orgprice[lc] + "\n")

key_fpkt = key
len_fpkt = len(key_fpkt)
key_flipkart = ""
product_title_flipkart = []
product_url_flipkart = []
product_curprice_flipkart = []
product_orgprice_flipkart = []
for lc in range(0, len_fpkt):
    if(re.match(r'[^a-zA-Z0-9]', key_fpkt[lc], re.M|re.I)):
        temp = codecs.encode(key_fpkt[lc].encode("utf-8"), "hex")
        key_flipkart += "%" + temp.decode("utf-8")
    else:
        key_flipkart += key_fpkt[lc]
url_fpkt = 'https://www.flipkart.com/search?q='+key_flipkart+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
print(url_fpkt)
source_code_fpkt = urlopen(Request(url_fpkt, headers=headers))
soup_fpkt = BeautifulSoup(source_code_fpkt, "html.parser")

if(soup_fpkt.find_all('a', {'class': '_2cLu-l'}) == []):
    for titles in soup_fpkt.find_all('div', {'class': '_3wU53n'}):
        try:
            product_title_flipkart.append(titles.get_text())
        except AttributeError:
            continue
    for titles in soup_fpkt.find_all('a', {'class': '_31qSD5'}):
        try:
            product_url_flipkart.append('https://www.flipkart.com' + titles.get('href'))
        except AttributeError:
            continue
else:
    for titles in soup_fpkt.find_all('a', {'class': '_2cLu-l'}):
        try:
            product_title_flipkart.append(titles.get('title'))
            product_url_flipkart.append('https://www.flipkart.com' + titles.get('href'))
        except AttributeError:
            continue


cnt = 0
for titles in soup_fpkt.find_all('div', {'class': '_1uv9Cb'}):
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