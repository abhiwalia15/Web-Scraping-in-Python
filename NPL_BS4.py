import requests 
from bs4 import BeautifulSoup as bs

url = 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'
page = requests.get(url)
#print(page.content)

#prettify the page html content
soup = bs(page.content, 'html.parser')
#print(soup.prettify())
#print(type(soup))
#print(soup.find_all('p'))

#get the title
#print(soup.title)

#get all the a tag with the link
tag = soup.find_all('a')[:8]
print(tag.get_text())
#print(tag.get_text('href'))
