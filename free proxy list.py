import requests
from bs4 import BeautifulSoup
import pandas as pd

content = requests.get('https://free-proxy-list.net/').text

soup = BeautifulSoup(content, 'lxml')

table_list = []

tables = soup.find('table', class_ = 'table table-striped table-bordered')


table_body = tables.find('tbody')

table = table_body.find_all('tr')

for table_row in table:

    ip = table_row.find_all('td')[0].text

    country = table_row.find_all('td')[3].text

    port = table_row.find_all('td')[1].text

    http_res = table_row.find_all('td')[6].text

    anonymity = table_row.find_all('td')[4].text

    google = table_row.find_all('td')[5].text


    table_dic = {
        'ip': ip,
        'country': country,
        'port': port,
        'google': google,
        'http_response': http_res,
        'anonymity': anonymity
    }
    
    table_list.append(table_dic) 
    
    
df = pd.DataFrame(table_list)
print(df.tail())
df.to_csv('free proxy list.csv')