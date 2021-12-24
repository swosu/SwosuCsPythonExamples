#json file seems to just work!!!!

# going from dict to file:
#https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/

# going from file to dict:
# https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/

import json

player_data = {}
coin = 42
name = 'jeremy'
player_data['coin'] = coin
player_data['name'] = name

print('original dictionary:', player_data)

with open("sample.json", "w") as outfile:
    json.dump(player_data, outfile)


# Opening JSON file
with open('sample.json') as json_file:
    data = json.load(json_file)

print('data is:', data)
print('helllo', data['name'])
