import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

apartment_list = []
for x in range(1,24):
    url = 'https://www.pararius.com/apartments/amsterdam/page-'
    content = requests.get(url + str(x)).text

    soup = BeautifulSoup(content, 'lxml')

    info = soup.find_all('section', class_ = 'listing-search-item') 

    for page_info in info:

        apartment = page_info.h2.a.text 

        price = page_info.find(class_ = 'listing-search-item__price').get_text().strip()

        location = page_info.find('div', class_ = 'listing-search-item__location').text.strip()

        space = page_info.find('li', class_ = 'illustrated-features__item').text 

        apartment_dic = {
            'apartment': apartment,
            'location': location,
            'space': space,
            'price': price
        }

        apartment_list.append(apartment_dic)

    print(len(apartment_list), 'apartments scraped')

    time.sleep(4)

df = pd.DataFrame(apartment_list)
df.to_csv('pararius.csv')

print(df.tail())