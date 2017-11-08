# 参考http://www.cnblogs.com/ifso/p/4707135.html
#! /usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request
import re;
import os;
import time;
pic_path="./pic"

if(os.path.exists(pic_path)):
    print(pic_path +" exists...")
else:
    os.mkdir(pic_path)

pre="http://www.baidu.com";
# BeautifulSoup(markup,"html5lib");
# url = 'https://bing.ioliu.cn/'
# url = 'http://python.org/';
url = "http://www.baidu.com/oracsmall/mall/index"

response = urllib.request.urlopen(url)
the_page = response.read()
# print(the_page.decode("utf8"))

soup = BeautifulSoup(the_page,"html5lib")

text = soup.prettify();
#print(text)

r = re.compile("^d");

div = soup.find_all(r);
print(len(div));

imgList = soup.find_all('img')

pic_url=[]

for item in imgList:
    pic_url.append(item.get('src'));

print(pic_url);

# （1）find_all( name , attrs , recursive , text , **kwargs )
#name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
#tag 获取属性，可以通过get(属性名)，例如imgList[i].get('src')
#tag 获取标签内容，可以通过string方法获取

# li=soup.find_all('li');
# print(len(li));
# for item in li:
#     print(item);
#     print(item.get('class'))
#     print(item.string)

t1 = time.time()
print(t1)
#获取当前时间戳
t2 = time.localtime()
print(t2)
#当前时间的struct_time形式

#当前时间的字符串形式
t3=time.ctime()
print(t3)

t4 =time.strftime("%Y%m%d", time.localtime())
print(t4)