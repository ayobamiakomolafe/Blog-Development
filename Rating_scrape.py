import urllib.request
import os
import requests
from bs4 import BeautifulSoup
html=urllib.request.urlopen('https://www.timeout.com/sydney/restaurants/the-best-restaurants-in-sydney')
html=html.read()
bs=BeautifulSoup(html, 'html.parser')
articles=bs.findAll('article')
articles=articles[:20]
links=[]
names=[]
for article in articles:
    link=article.find('div', {"class": "_title_tpquo_9"}).find('a', href=True)
    links.append(link['href'])
    names.append(article.find('h3').get_text())
fob=open('Ratings.txt', 'w')
for name, link in zip(names, links):
    html=urllib.request.urlopen(link)
    html=html.read()
    bs=BeautifulSoup(html, 'html.parser')
    try:
        star=bs.find('div', {"class": "_ratingStars_k40fn_1"}).find('span', {"class": "sr-only"}).get_text()
        fob.write('\n'+ name+ ' -- '+ star)
    except:
        star='None'
        fob.write('\n' + name+ ' -- '+ star)
        continue
fob.close()
    
