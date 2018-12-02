import mysql.connector
import time

class Book():
    def __init__(self,isbn,isbn13,title,image_url,author_id,rating,genre_1,genre_2,genre_3,amazon_url,amazon_price,flipkart_url,flipkart_price,infibeam_url,infibeam_price,snapdeal_url,snapdeal_price):
        value = []
        self.ISBN = isbn
        value.append(self.ISBN)
        self.ISBN13 = isbn13
        value.append(self.ISBN13)
        self.Title = title
        value.append(self.Title)
        self.AuthorID = author_id
        value.append(self.AuthorID)
        self.Rating = rating
        value.append(self.Rating)
        self.Genre1 = genre_1
        value.append(self.Genre1)
        self.Genre2 = genre_2
        value.append(self.Genre2)
        self.Genre3 = genre_3
        value.append(self.Genre3)
        self.ImageSrc = image_url
        value.append(self.ImageSrc)
        self.Amazon = amazon_url
        value.append(self.Amazon)
        self.AmazonPrice = amazon_price
        value.append(self.AmazonPrice)
        self.Flipkart = flipkart_url
        value.append(self.Flipkart)
        self.FlipkartPrice = flipkart_price
        value.append(self.FlipkartPrice)
        self.Infibeam = infibeam_url
        value.append(self.Infibeam)
        self.InfibeamPrice = infibeam_price
        value.append(self.InfibeamPrice)
        self.Snapdeal = snapdeal_url
        value.append(self.Snapdeal)
        self.SnapdealPrice = snapdeal_price
        value.append(self.SnapdealPrice)
        value.append(time.time())
        value.append(86400)
        mydb = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='project')
        mycursor = mydb.cursor()
        sql = "INSERT INTO book(isbn,isbn13,title,author_id,rating,genre1,genre2,genre3,image_url,amazon_url,amazon_price,flipkart_url,flipkart_price,infibeam_url,infibeam_price,snapdeal_url,snapdeal_price,lastVisited,refreshPeriod) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            mycursor.execute(sql, tuple(value))
        except:
            try:
                sqlquery = "DELETE FROM book WHERE isbn13 = %(value)s"
                params = {'value': isbn13}
                mycursor.execute(sqlquery, params)
                mycursor.execute(sql, tuple(value))
            except Exception as e:
                print(e)
        mydb.commit()
        
        