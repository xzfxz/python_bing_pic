from distutils.sysconfig import get_python_lib
from bs4 import BeautifulSoup

import urllib.request
import requests
import os
import time

print(get_python_lib())

#1
# with open("/Users/zhao/workspace/zhaoGit/python_bing_pic/index.htm","r") as data:
#     soup=BeautifulSoup(data,'html')
#     print(soup)


url = 'https://bing.ioliu.cn/'
t1 =time.strftime("%Y%m%d", time.localtime())
print(t1)
pic_path="./"+t1


if(os.path.exists(pic_path)):
    print(pic_path +" exists...")
else:
    os.mkdir(pic_path)

try:
    response = urllib.request.urlopen(url)
    the_page = response.read()
    soup = BeautifulSoup(the_page, "html")
    imgList = soup.find_all('img')

    pic_url = []
    for item in imgList:
        pic_url.append(item.get('data-progressive'))

    print(pic_url)

    for i in range(len(pic_url)):
        url = pic_url[i]
        pic = requests.get(url)
        jpg = pic_path +os.sep +"b"+ str(i) + '0.jpg'
        fp = open(jpg, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1

except BaseException as e:
    print(repr(e))
    print("error")
