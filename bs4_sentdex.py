import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

source = requests.get('https://pythonprogramming.net/parsememcparseface/')

soup = bs(source.content, 'html.parser')

table = soup.table
print(table)
print('--------------------')

table_rows = table.find_all('tr')

for tr in table_rows:
	#print(tr.get_text())
	td = tr.find_all('td')
	row = [i.get_text() for i in td]
	print(row)
	print('----------------')
	
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
for df in dfs:
	print(df)

