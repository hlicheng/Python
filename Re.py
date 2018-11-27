'''
Created on 2018年11月27日

@author: 雪狮子
'''
#爬取应用宝上某个页面的全部游戏及其种类

import re
import requests

#页面url
url = "http://app.mi.com/category/15"


response = requests.get(url)

#应用正则表达式搜索爬取到的页面中的指定信息，并返回给games
games = re.findall('<h5><a href=".*?">(.*?)</a></h5><p class="app-desc"><a href=".*?">(.*?)</a></p>', response.text, re.S)



print(len(games))
for game in games:
	#由于爬取到的页面中有某些文本和正则表达式匹配，但不是我们想要的，将其remove
    if(game[0].find("\r\n") == -1):
        print(game)
    else:
        games.remove(game)
print(len(games))

