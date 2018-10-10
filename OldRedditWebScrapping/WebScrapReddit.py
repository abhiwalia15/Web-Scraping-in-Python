import csv
import requests
from bs4 import BeautifulSoup as bs
import time

#url of the old reddit page
url='https://old.reddit.com/r/datascience/'
#headers to mimic a browser visit
headers = {'User-Agent':'Mozilla/5.0'}

#returns a request.models.Response object
page = requests.get(url, headers=headers)
#print(page.content)

soup=bs(page.content, 'html.parser')
#print(soup.prettify())

domains = soup.find("span", class_ = 'domain')
#print(domains.prettify())

#ds = domains.find('a' , href='/r/datascience/')
#print(ds.prettify())
#if we want to pass multiple arguments then we can
#pass it as a dictionary.
#multiple = soup.find('span', {'class':'domain','height':'100px'})

#to get (self.datascience) domains
for domain in soup.find_all('span',class_='domain'):
	if domain!= '(self.datascience)':
		continue
	
	parent_div = domain.parent.parent.parent.parent
	print(parent_div.text)
