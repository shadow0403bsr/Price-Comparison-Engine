import Book
import Goodreads
import Amazon
import Flipkart
import Infibeam
import Snapdeal
import mysql.connector
import time

def main():
    file = open("BooksDatabase.txt", "r")
    data = file.readlines()
    update = 1
    for isbn in data:
        isbn.strip()
        mydb = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='project')
        mycursor = mydb.cursor()
        sql = "SELECT * FROM book WHERE isbn13 = %(value)s"
        params = {'value': isbn}
        try:
            mycursor.execute(sql, params)
        except Exception as e:
            print(e)
        if(mycursor.rowcount == 1):
            for row in mycursor:
                lastVisited = row['lastVisited']
                refreshPeriod = row['refreshPeriod']
                if(time.time() - lastVisited < refreshPeriod):
                    update = 0
        if(update == 1):
            goodreads_data = Goodreads.get_goodreads(isbn[:-1])
            if goodreads_data == []:
                continue
            amazon_data = Amazon.get_amazon(isbn[:-1])
            flipkart_data = Flipkart.get_flipkart(isbn[:-1])
            infibeam_data = Infibeam.get_infibeam(isbn[:-1])
            snapdeal_data = Snapdeal.get_snapdeal(isbn[:-1])
            Book.Book(goodreads_data['isbn'], isbn, goodreads_data['title'], goodreads_data['image'],
                      goodreads_data['authorID'], goodreads_data['rating'], goodreads_data['genre1'],
                      goodreads_data['genre2'], goodreads_data['genre3'],
                      amazon_data['amazon_url'], amazon_data['amazon_price'],
                      flipkart_data['flipkart_url'], flipkart_data['flipkart_price'],
                      infibeam_data['infibeam_url'], infibeam_data['infibeam_price'],
                      snapdeal_data['snapdeal_url'], snapdeal_data['snapdeal_price'])



if __name__ == '__main__':
    main()
