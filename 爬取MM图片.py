'''
Created on 2018年11月28日

@author: 雪狮子
'''
'''
    找出某个页面的所有MM的名字，主页url和头像url
    接着由得到的主页url找出该MM的主页中的所有图片，将图片和头像
    存入以每个MM的名字命名的目录中
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import re,os
from urllib import request

#创建目录
def md(path):
    isExist = os.path.exists(path)
    if not isExist:
        os.mkdir(path)

#得到某个MM主页的所有图片
def getOneImage(url):   
    bro = webdriver.Firefox()
    bro.get(url)    
    content = bro.page_source  
    soup = BeautifulSoup(content, 'lxml')
    images_url_txt = soup.find_all('div', class_="pic").__str__()
    images_url= re.findall('<div class="pic"><div class="ice-img sharp ".*?><img .*?src="(.*?)".*?', images_url_txt, re.S)
    bro.quit()
    return images_url

#将某个images_url中所有的图片URL存入目录中
def saveImageToDir(images_url, path, filename):
    md(path)
    for i in range(len(images_url)):
        response = request.urlopen(images_url[i])
        data = response.read()
        with open(path+"/"+filename+str(i)+".jpg", "wb") as f:
            f.write(data)
            f.close()
    
#得到某个页面的所有MM
def getMM():
    broswer = webdriver.Firefox()
    broswer.get("https://v.taobao.com/v/daren/find?activeTab=%E5%88%9B%E4%BD%9C%E8%80%85&keyWord=mm")
    soup = BeautifulSoup(broswer.page_source, 'lxml')
    
    #找出anchor所在的标签文本
    anchors_list = soup.find_all('h3', class_="anchor-name").__str__()
    #找出image所在的标签代码
    image_list = soup.find_all('a', class_="anchor-profile-info").__str__()
    
    #利用中则表达式匹配，从anchors_list中找出所有的anchor
    anchors = re.findall('<h3.*?><!--.*?-->(.*?)<!--.*?-->.*?</h3>', anchors_list, re.S)
    
    #找出所有image的URL
    images_url = re.findall('<a class="anchor-profile-info".*?href="(.*?)".*?src="(.*?)".*?', image_list, re.S)
    broswer.quit()
    return anchors,images_url

def saveOneImage(url, path, name):
    response = request.urlopen(url)
    data = response.read()
    with open(path, "wb") as f:
        f.write(data)
        print("正在保存"+name+"的头像")
        f.close()
    

#将某个MM的所有图片存入目录
def saveMM(MM_anchors, MM_images_url, path):
    for i in range(len(MM_anchors)):
        #建立以MM命名的目录
        md(path+MM_anchors[i])
        
        #将该MM的头像保存到目录    
        MM_head = MM_images_url[i][1]
        if(MM_head.find("http")==-1):
            url = "http:"+MM_head
        filename = path+MM_anchors[i]+"/"+MM_anchors[i]+".jpg"
        saveOneImage(url, filename, MM_anchors[i])
        
        MM_url = MM_images_url[i][0]
        #得到该MM主页的图片的所有image_url
        MM_all_url = getOneImage(MM_url)
        saveImageToDir(MM_all_url,path+MM_anchors[i], MM_anchors[i])
        print(MM_anchors[i]+"的主页的所有图片保存完成")
        

if __name__ == '__main__':
    path = "d:/image_test/"
    md(path)
    MM_anchors,MM_images_url = getMM()
    saveMM(MM_anchors, MM_images_url, path)
    
    
        
        
        
        
        
    
# print(images[18])
# print(images[19])