import Book
import Goodreads
import Amazon
import Flipkart
import Infibeam
import Snapdeal

def main():
    file = open("BooksDatabase.txt", "r")
    data = file.readlines()
    for isbn in data:
        goodreads_data = Goodreads.get_goodreads(isbn[:-1])
        if goodreads_data == []:
            continue
        amazon_data = Amazon.get_amazon(isbn[:-1])
        flipkart_data = Flipkart.get_flipkart(isbn[:-1])
        infibeam_data = Infibeam.get_infibeam(isbn[:-1])
        snapdeal_data = Snapdeal.get_snapdeal(isbn[:-1])
        Book.Book(goodreads_data['isbn'],isbn,goodreads_data['title'],goodreads_data['image'],
                        goodreads_data['authorID'],goodreads_data['rating'],goodreads_data['genre1'],
                        goodreads_data['genre2'],goodreads_data['genre3'],
                        amazon_data['amazon_url'],amazon_data['amazon_price'],
                        flipkart_data['flipkart_url'],flipkart_data['flipkart_price'],
                        infibeam_data['infibeam_url'],infibeam_data['infibeam_price'],
                        snapdeal_data['snapdeal_url'],snapdeal_data['snapdeal_price'])

if __name__ == '__main__':
    main()
