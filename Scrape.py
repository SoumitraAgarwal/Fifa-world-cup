# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd
import shutil
import os
import urllib3

urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()

df = pd.read_csv("Players.csv")

print("Read complete")
countries = []
for i in range(len(df)):
	print(df['Name'][i] + ' ' + str(i))
	url_temp = df['Url'][i]
	if(df['Country'][i] not in countries):
		countries.append(df['Country'][i])
		os.mkdir('Pictures/Country/' + df['Country'][i])


	while(True):
		try:
			response = requests.get(url_temp, stream=True)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break
	with open('Pictures/Country/' + df['Country'][i] + '/' +df['Name'][i]+'.jpg', 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response