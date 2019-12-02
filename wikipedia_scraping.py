import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Will_Smith'
page = requests.get(url)

soup = bs(page.content, 'html.parser')
#print(soup.h1)
#print(soup.h2)
#print(soup.h3)

h1 = soup.select('h1')
#print(h1)

H1_tags = [H1.get_text() for H1 in h1]
print(H1_tags)
print('------------')

#finding text in h2 tag

h2 = soup.select('h2')
#print(h2)

H2_tags = [H2.get_text() for H2 in h2]
print(H2_tags)
print('------------')

#finding text in h3 tag
h3 = soup.select('h3')
#print(h3)

H3_tags = [H3.get_text() for H3 in h3]
print(H3_tags)
print('------------')

'''
#ploting via pandas if of same length then follow this method
df = pd.DataFrame({
				'H1': H1_tags,
				'H2': H2_tags,
				'H3': H3_tags,
				})
				
print(df)
'''

'''
#finding text in p tag
p = soup.find_all('p')
#print(p)

for P in p:
	print(P.get_text())
print('------------')
#finding text in para tag
p = soup.find_all({'h1','h2','h3','p'})

for all_content in p:
	print(all_content.get_text())
	
	
'''
