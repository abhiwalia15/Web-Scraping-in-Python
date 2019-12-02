import requests 
from bs4 import BeautifulSoup as bs

page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
page
page.status_code
#print(page.content)

soup = bs(page.content, 'html.parser')
#print(soup.prettify())
#print('\n')

#print(list(soup.children))
#Print('\n')

for item in list(soup.children):
    #print(type(item))
	#print('\n')
  
	html = list(soup.children)[2]
#print(list(html.children))

#if we want to extract the text inside the p tag, so we'll dive into the body
body = list(html.children)[3]
#print(list(body.children))

p = list(body.children)[1]
#print(p.get_text())

#to return a complete list of all the tags at once
#print(soup.find_all('p')[0].get_text())

#TO FIND FIRST INSTANCE OF A TAG
print(soup.find('p'))
print(soup.find('head'))
print(soup.find('title'))

