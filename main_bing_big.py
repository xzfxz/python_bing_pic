
#!/usr/bin/env python3
#获取bing首页大图片的方法

from bs4 import BeautifulSoup
import urllib.request
import requests
import os


url = 'https://bing.ioliu.cn/'
pic_path="./pic"

if(os.path.exists(pic_path)):
    print(pic_path +" exists...")
else:
    os.mkdir(pic_path)

try:
    response = urllib.request.urlopen(url)
    the_page = response.read()
    soup = BeautifulSoup(the_page, "html5lib")
    imgList = soup.find_all('img')

    pic_url = [];
    for item in imgList:
        pic_url.append(item.get('data-progressive'));

    print(pic_url);

    for i in range(len(pic_url)):
        url = pic_url[i];
        pic = requests.get(url,timeout=10)
        jpg = pic_path +os.sep +"b"+ str(i) + '0.jpg'
        fp = open(jpg, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1

except BaseException:
    print("error");
