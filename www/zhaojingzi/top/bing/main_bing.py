# !/usr/bin/env python3.6
# 获取bing首页小图片的方法 small

from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import time

# 定义请求的路径
url = 'https://bing.ioliu.cn/'
# 定义图片存储路径
t1 = time.strftime("%Y%m%d", time.localtime())
pic_path = "/Users/zhao/Pictures/" + t1

# 校验路径是否存在
if (os.path.exists(pic_path)):
    print(pic_path + " exists...")
else:
    os.mkdir(pic_path)

try:
    # 请求
    response = urllib.request.urlopen(url)
    # 解析页面
    the_page = response.read()
    soup = BeautifulSoup(the_page, "html.parser")
    #
    print("soup....")
    print(soup)
    # 查找所有img标签的集合
    imgList = soup.find_all('img')

    pic_url = []
    for item in imgList:
        # 得到img标签中的src属性并添加到新集合中
        pic_url.append(item.get('src'))
    # 打印图片地址
    print("pic_urls....")
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
                jpg = pic_path + os.sep + "s_" + str(i) + '.jpg'
                # 下载文件
                fp = open(jpg, 'wb')
                fp.write(response.content)
                fp.close()
                i += 1
            else:
                print(response.status_code,url)
        except Exception as e1:
            print(e1)

# 深入理解requests库 http://docs.python-requests.org/zh_CN/latest/user/quickstart.html#id6
except BaseException as e:
    print(repr(e))
    print("error")
