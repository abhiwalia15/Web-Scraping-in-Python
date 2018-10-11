import requests
from bs4 import BeautifulSoup as bs

#url of the page to scrap
url = 'http://www.pythonscraping.com/pages/warandpeace.html'
page = requests.get(url)
#print(page.content)
print('=------------------------------------------------=')

#structered format of the html content
soup = bs(page.content, 'html.parser')
#print(soup.prettify())
print('------------------------------------------')

#all the names are written in green,find al names
namelist = soup.find_all('span', class_='green')
#print(namelist)

#get all the names
print('ALL NAMES OF AUTHOR IN GREEN-\n')
for name in namelist:	
	print(name.get_text())
	print('---------------------------')
	
para = soup.find_all('span', class_='red')
#print(para)
print('ALL PARAGRAPHS IN RED COLOR-\n')
for par in para:
	print(par.get_text())
	print('--------------')
