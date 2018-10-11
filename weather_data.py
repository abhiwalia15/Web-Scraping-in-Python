import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


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
tonight = forecast_items[0]
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
#print(periods)

short_desc_tags = seven_day.select('.tombstone-container .short-desc')
short_descs = [sd.get_text() for sd in short_desc_tags]
#print(short_descs)

temp_tags = seven_day.select('.tombstone-container .temp')
temps = [t.get_text() for t in temp_tags]
#print(temps)

title_tags = seven_day.select('.tombstone-container img')
descs = [d['title'] for d in title_tags]
#print(descs)

weather = pd.DataFrame({
			'period': periods,
			'short_description': short_descs,
			'temp': temps,
			'desc': descs,
			})
weather.index.name = 'SERIAL NO.'
print(weather)

temp_nums = weather['temp'].str.extract("(?P<temp_num>\d+)", expand=False)
weather['temp_nums'] = temp_nums.astype('int')
#print(temp_nums.mean())
#print(temp_nums.median())
#print(temp_nums.count())
#print(temp_nums)

is_night = weather['temp'].str.contains("Low")
weather['is_night'] = is_night
#print(is_night)
#print(weather)

weather.to_csv('weather.csv')
weather.to_json('weather.json')
weather.to_html('weather.html')
