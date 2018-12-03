from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import mysql.connector
import re
import time

def get_isbn(soup):
    try:
        isbn = soup.find(id="bookDataBox").get_text().strip().split("\n")
        return (isbn[6].strip())
    except:
        return "NA"

def get_title(soup):
    try:
        title = soup.find(id="bookDataBox").get_text().strip().split("\n")
        return (title[1].strip())
    except:
        return "NA"

def get_author(soup):
    value = []
    details = soup.find("a", attrs={"class" : "authorName"})
    obj = re.search(r'https://www.goodreads.com/author/show/(.*?)\..*', details['href'], re.M | re.I)
    authorID = obj.group(1)
    authorName = details.get_text().strip()
    value.append(authorID)
    value.append(authorName)
    mydb = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='project')
    mycursor = mydb.cursor()
    sql = "INSERT INTO author(authorID, authorName) VALUES (%s, %s)"
    try:
        mycursor.execute(sql, tuple(value))
    except Exception as e:
        print(e)
    mydb.commit()
    return authorID

def get_rating(soup):
    rating = soup.find("span", attrs={"itemprop" : "ratingValue"}).get_text().strip()
    return rating

def get_image(soup):
    image = soup.find(id = "coverImage")
    return image['src']

def get_genre(soup, pos):
    genres = soup.find_all("a", attrs={"class" : "actionLinkLite bookPageGenreLink"})
    if(genres.__len__()<pos):
        return "NA"
    return genres[pos-1].get_text().strip()

def get_goodreads(isbn):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://www.goodreads.com/book/isbn/' + isbn
    source_code = urlopen(Request(url, headers=headers))
    soup = BeautifulSoup(source_code, 'html.parser')
    validity = soup.find(id="bookDataBox")
    if validity == None:
        invalid = []
        return invalid
    goodreads_data = dict(isbn = get_isbn(soup), isbn13 = isbn, title = get_title(soup), authorID = get_author(soup), image = get_image(soup), rating = get_rating(soup), genre1 = get_genre(soup,1), genre2 = get_genre(soup,2), genre3 = get_genre(soup,3))
    time.sleep(2)
    return goodreads_data

