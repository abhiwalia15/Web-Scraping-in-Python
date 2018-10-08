
import requests
from bs4 import BeautifulSoup as bs

page = requests.get('http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html')
soup = bs(page.content, 'html.parser')
print(soup.prettify())
print('\n')

#print(soup.find_all('p'))

#print(soup.find_all('p', class_='outer-text'))

#print(soup.find_all(class_='outer-text'))

#print(soup.find_all(id='first'))

p = soup.find_all('p', class_='outer-text', id='second')
#print(p[0].get_text())

print(soup.select('div    p.inner-text'))
