import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage

from bs4 import BeautifulSoup as bs
import requests

#class client inherit from qwebpage
class Client(QWebPage):
	
	def __init__(self,url):
		self.app = QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self.on_page_load)
		self.mainFrame().load(QUrl(url))
		
	def on_page_load(self):
		self.app.quit()
		
url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()		
		
		
		
page = requets.get(url)
soup = bs(page.content, 'html.parser')
js_test = soup.find_all('p', class_='jstest')
print(js_test.get_text())
		
