from bs4 import BeautifulSoup
import requests
import time
import datetime

req=requests.get("https://www.amazon.com/Giorgio-Armani-Acqua-Toilette-Spray/dp/B0002JVJ2C/ref=sr_1_1?crid=3OQ9N1MMC8E0J&keywords=aqua+di+gio&qid=1656863449&sprefix=%2Caps%2C157&sr=8-1")

soup= BeautifulSoup(req.content, "html.parser")

print(soup.prettify())

title=soup.find(id='productTitle').get_text()

price=soup.find(id='priceblock_ourprice').get_text()

print(title)
print(price)

price=price.strip()
title=title.strip()

print(title)
print(price)

import csv
header=['Title', 'Price', 'Date']
data=[title, price]

type(data)

with open('Amazonwebscraper.csv', 'w', newline='', encoding='UTF8') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    
import datetime
Today=datetime.date.today()
print(Today)

import pandas as pd
df=pd.read_csv(r'C:\Users\Muhib\Amazonwebscraper.csv')
print(df)


with open('Amazonwebscraper.csv', 'a+', newline='', encoding='UTF8') as f:
    writer=csv.writer(f)
    writer.writerow(data)
    
def checkprice():
    req=requests.get("https://www.amazon.com/Giorgio-Armani-Acqua-Toilette-Spray/dp/B0002JVJ2C/ref=sr_1_1?crid=3OQ9N1MMC8E0J&keywords=aqua+di+gio&qid=1656863449&sprefix=%2Caps%2C157&sr=8-1")

    soup= BeautifulSoup(req.content, "html.parser")

    price=soup.find(id='priceblock_ourprice').get_text()
    
    price=price.strip()
    
    title=title.strip()
    
    import datetime
    
    Today=datetime.date.today()
    
    import csv
    
    header=['Title', 'Price', 'Date']
    
    data=[title, price]
    
    with open('Amazonwebscraper.csv', 'a+', newline='', encoding='UTF8') as f:
     writer=csv.writer(f)
     writer.writerow(data)
     
     while True:
      checkprice()
    time.sleep(86400)