import re
import pandas as pd

data = pd.read_csv('Players.csv')
length = len(data)
for i in range(length):
	data["Name"][i] = re.sub(r"[\n\t\s]*", "", data["Name"][i])
	data["Country"][i] = re.sub(r"[\n\t\s]*", "", data["Country"][i])

data.to_csv('Players.csv', index=False)