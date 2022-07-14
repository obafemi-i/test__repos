import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time

device_list = []

for x in range (1, 51):

    content = requests.get(f'https://www.jumia.com.ng/mlp-stay-connected-deals/other-tablets/?page={x}#catalog-listing').text

    soup = BeautifulSoup(content, 'lxml')

    page_info = soup.find_all('div', class_ = 'info')

    for info in page_info:

        device = info.find('h3', class_ = 'name').text

        price = info.find('div', class_ = 'prc').text


        device_dic = {
            'device': device,
            'price': price
        }

        device_list.append(device_dic)
        
        print(len(device_list), 'devices extracted')   
        print('waiting 4 secs before next scrap...')
        
        
        
     
df = pd.DataFrame(device_list)
print(df.tail())
df.to_csv('jumia tablet deviced.csv')


