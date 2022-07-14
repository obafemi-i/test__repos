import requests
from bs4 import BeautifulSoup
import time
import pandas as pd 


print('Scraping...') 

book_information = []

def get_book_info():

    for x in range(1,81):
        url = 'https://www.pdfdrive.com/search?q=comics&pagecount=&pubyear=&searchin=&page='

        main_content = requests.get(url + str(x)).text

        soup = BeautifulSoup(main_content, 'lxml') 

        books = soup.find_all('div', class_ = 'file-right')


        for book in books:

            size = book.find('span', class_ = 'fi-size hidemobile').get_text()

            downloads = book.find('span', class_ = 'fi-hit').get_text().replace('Downloads','').replace(',','.')

            title = book.a.h2.get_text()


            book_info = {
                'title':title,
                'size':size,
                'downloads':downloads
            } 

            book_information.append(book_info) 
        print(len(book_information), 'books scraped')
        print('waiting 3 secs before next scrape...')
        time.sleep(3)
    
    
get_book_info()

df = pd.DataFrame(book_information)
print(df.tail())
df.to_csv('comics.csv')

print('All done!')

