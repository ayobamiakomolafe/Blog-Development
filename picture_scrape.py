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
for name, link in zip(names, links):
    html=urllib.request.urlopen(link)
    html=html.read()
    bs=BeautifulSoup(html, 'html.parser')
    slideshows=bs.find('div', {"class": "_slideshow_1lf47_1"}).findAll('li')
    count=0
    for slides in slideshows:
        count=count+1
        if count <=5:
            lnk = slides.find('img').get('src')
            image_name=name+ str(count) +'.jpg'
            with open(image_name, "wb") as f:
                f.write(requests.get(lnk).content)
                print(image_name)
        else:
            continue
            
            
                
    

    
    

