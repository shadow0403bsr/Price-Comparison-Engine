from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, Request
import re
import time
import mysql.connector

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

mydb = mysql.connector.connect(user='root',password='admin',host='127.0.0.1',database='pcm')
mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE TABLE flipkart_url (FSN CHAR(13) PRIMARY KEY, url VARCHAR(255))")
except:
    print("Table is already created. Updating it...")

sql = "INSERT INTO flipkart_url (FSN, url) VALUES (%s, %s)"
for page in range(1,50):
    url = 'https://www.flipkart.com/books/fiction-nonfiction-books/literature-fiction-books/pr?sid=bks%2Cfnf%2Cgld&otracker=categorytree&p%5B%5D=facets.binding%255B%255D%3DPaperback&page=' + str(page)
    source_code = urlopen(Request(url, headers=headers))
    soup = BeautifulSoup(source_code, "html.parser")
    for link in soup.find_all('a', href=True):
        data = []
        obj = re.search(r'/(.*)?pid=(.*?)&.*', link['href'], re.M | re.I)

        if (obj):
            data.append(obj.group(2))
            data.append('https://www.flipkart.com' + link['href'])
            val = tuple(data)
            try:
                mycursor.execute(sql, val)
            except Exception as e:
                print(e)
            mydb.commit()
    time.sleep(10)
mydb.close()