import urllib.request
import selenium
from bs4 import BeautifulSoup
html=urllib.request.urlopen('https://www.timeout.com/sydney/restaurants/the-best-restaurants-in-sydney')
html=html.read()
bs=BeautifulSoup(html, 'html.parser')
articles=bs.findAll('article')
articles=articles[:20]
fob=open('Article.txt', 'w')
for article in articles:
    fob.write(article.find('h3').get_text())
    fob.write('\n')
    link=article.find('div', {"class": "_title_tpquo_9"}).find('a', href=True)
    fob.write(link['href'])
    fob.write('\n')
    para= article.findAll('p')
    for i in para:
        fob.write(i.get_text())
    fob.write('\n')
fob.close()
