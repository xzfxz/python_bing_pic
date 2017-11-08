
#!/usr/bin/env python3
#获取bing首页小图片的方法 small

from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import time

url = 'https://bing.ioliu.cn/'
t1 =time.strftime("%Y%m%d", time.localtime())
pic_path="./"+t1;


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
        pic_url.append(item.get('src'));

    print(pic_url);

    for i in range(len(pic_url)):
        url = pic_url[i];
        pic = requests.get(url,timeout=10)
        jpg = pic_path+os.sep + "s_"+str(i) + '.jpg'
        fp = open(jpg, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1

except BaseException:
    print("error");
