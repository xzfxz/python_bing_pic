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
pic_path="/Users/zhao/Pictures/"+t1


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
        try:
            url = pic_url[i]
            # 添加headers ，解决403请求失败的问题
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
            response = requests.get(url, headers=header)
            if response.status_code == 200:
                # 存储图片的文件名称
                jpg = pic_path + os.sep + "b_" + str(i) + '.jpg'
                # 下载文件
                fp = open(jpg, 'wb')
                fp.write(response.content)
                fp.close()
                i += 1
            else:
                print(response.status_code,url)
        except Exception as e1:
            print(e1)

except BaseException as e:
    print(repr(e))
    print("error")
