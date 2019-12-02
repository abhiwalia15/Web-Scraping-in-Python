from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.fortishealthcare.com/india/doctors"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
type(soup)

# Get the title
# title = soup.title
# print(title)
#'div', {'class':'dctlist-lp-mn'}

names = []
details = []

for links in soup.find_all(class_='dctlist-lp-mn'):
    #print(links.prettify())

    #getting names of all doctors
    name = links.find('h2')
    names.append(name.get_text())
    
    p = links.find('p')
    details.append(p.get_text())

# print(names)
# print(details)

stopwords = ['/', '\t','\n']
for name in list(names):
    if name in stopwords:
        names.split('  ')
        print(names)

