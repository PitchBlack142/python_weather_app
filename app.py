import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=32.6483&lon=-83.4445#.XpG3DMhKi00')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
# print(week)

items = week.find_all(class_='tombstone-container')

# print(items[0])

period = items[0].find(class_='period-name').get_text()
short_desc = items[0].find(class_='short-desc').get_text()
temp = items[0].find(class_='temp').get_text()

# print(period)
# print(short_desc)
# print(temp)

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
tempratures = [item.find(class_='temp').get_text() for item in items]

# print(period_names)
# print(short_descriptions)
# print(tempratures)

weather_stuff = pd.DataFrame(
    {'period': period_names,
    'short_descriptions': short_descriptions,
    'tempratures': tempratures,
})

print(weather_stuff)

weather_stuff.to_csv('weather.csv')