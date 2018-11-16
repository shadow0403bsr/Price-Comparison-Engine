from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, Request
import re
import time
import mysql.connector

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

mydb = mysql.connector.connect(user='root',password='admin',host='127.0.0.1',database='pcm')
mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE TABLE amazon_url (ASIN CHAR(10) PRIMARY KEY, url VARCHAR(255))")
except:
    print("Table is already created. Updating it...")

sql = "INSERT INTO amazon_url (ASIN, url) VALUES (%s, %s)"
for page in range(1,75):
    url = 'https://www.amazon.in/s/ref=sr_pg_' + str(page) + '?fst=as%3Aoff&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A1318157031%2Cp_n_binding_browse-bin%3A1318376031%2Cn%3A1318160031&page=' + str(page) + '&bbn=1318157031&ie=UTF8&qid=1542202429'
    source_code = urlopen(Request(url, headers=headers))
    soup = BeautifulSoup(source_code, "html.parser")
    for link in soup.find_all('a', href=True):
        data = []
        obj = re.search(r'https://www.amazon.in/(.*)/dp/(.*?)/(.*?)_twi_pap_.*', link['href'], re.M | re.I)

        if (obj):
            data.append(obj.group(2))
            data.append(link['href'])
            val = tuple(data)
            try:
                mycursor.execute(sql, val)
            except Exception as e:
                print(e)
            mydb.commit()
    time.sleep(10)
mydb.close()