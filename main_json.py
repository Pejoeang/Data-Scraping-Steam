import requests
import json

url = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=440&count=3&maxlength=300&format=json'

r = requests.get(url).json()
users=r['appnews']['newsitems']
for user in users:
    print(user['appid'])
    print(user['title'])
    print(user['url'])
