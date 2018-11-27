'''
Created on 2018年11月27日

@author: 雪狮子
'''

#爬取应用宝中某个页面的所有游戏及其类别


import re
from urllib import request
import requests

url = "http://app.mi.com/category/15"


response = requests.get(url)


games = re.findall('<h5><a href=".*?">(.*?)</a></h5><p class="app-desc"><a href=".*?">(.*?)</a></p>', response.text, re.S)
#type = re.findall('<p class="app-desc"><a href=".*?">(.*?)</a></p>', response.text, re.S)

print(type(games))
print(len(games))
for game in games:
    if(game[0].find("\r\n") == -1):
        print(game)
    else:
        games.remove(game)
print(len(games))

#print(type[0])
