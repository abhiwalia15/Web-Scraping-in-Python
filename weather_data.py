import requests
from bs4 import BeautifulSoup as bs

''' * Download the web page containing the forecast.
 * Create a BeautifulSoup class to parse the page.
 * Find the div with id seven-day-forecast, and assign to seven_day
 * Inside seven_day, find each individual forecast item.
 * Extract and print the first forecast item.'''

#url of the page to extract
url = 'http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'
page = requests.get(url)
#print(page.content)

soup = bs(page.content, 'html.parser')
#print(soup.prettify()) 

#extract data with id this given below
seven_day = soup.find(id='seven-day-forecast')
#print(seven_day.prettify())

forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[3]
#print(tonight.prettify())


'''As you can see, inside the forecast item tonight is all the information we want.
 There are 4 pieces of information we can extract:

 * The name of the forecast item — in this case, Tonight.
 * The description of the conditions — this is stored in the title property of img.
 * A short description of the conditions — in this case, Mostly Clear.
 * The temperature low — in this case, 49 degrees.
 '''
 
#period = tonight.find(class_="period-name").get_text()
#short_desc = tonight.find(class_="short-desc").get_text()
#temp = tonight.find(class_="temp").get_text()

'''Now, we can extract the title attribute from the img tag. To do this,
we just treat the BeautifulSoup object like a dictionary,
and pass in the attribute we want as a key'''

#img = tonight.find('img')
#desc = img['title']

period_tags = seven_day.select('.tombstone-container .period-name')
periods = [pt.get_text() for pt in period_tags]
print(periods)

short_desc_tags = seven_day.select('.tombstone-container .short-desc')
short_descs = [sdt.get_text() for sdt in short_desc_tags]
print(short_descs)

temp_tags = seven_day.select('.tombstone-container .temp')
temps = [t.get_text() for t in temp_tags]
print(temps)

title_tags = seven_day.select('.tombstone-container img')
descs = [d['title'] for d in title_tags]
print(descs)
