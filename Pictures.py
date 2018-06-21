from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

player_url 	= 'https://www.fifa.com/worldcup/players/browser/'
dr 			= webdriver.Chrome('./chromedriver')
dr.get(player_url)

html 		= dr.page_source
soup 		= BeautifulSoup(html,'lxml')
images 		= soup.findAll('image', class_='image-r image-responsive')
playerData 	= soup.findAll('div', class_='fi-p__wrapper-text')
playerNames 	= []
playerCountry 	= []
imageUrl 		= []

length 		= len(images)
for i in range(length):
	imageUrl.append(images[i]['xlink:href'])
	name = playerData[i].find('div', class_ = 'fi-p__name')
	playerNames.append(name.find(text=True))
	country = playerData[i].find('div', class_ = 'fi-p__country')
	playerCountry.append(country.find(text=True))
	print(name.find(text=True) + ' ' + country.find(text=True))

df = pd.DataFrame({
	"Name" 		: playerNames,
	"Country"	: playerCountry,
	"Url"		: imageUrl
	})

df.to_csv("Players.csv", index = False)
