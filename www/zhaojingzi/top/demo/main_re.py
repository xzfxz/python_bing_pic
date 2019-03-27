# -*- coding: UTF-8 -*-
# py文件默认是ASCII格式，解决中文保存问题
# python中的正则学习
# 笔记

# 1、. 匹配任意除换行符“\n”外的字符；
# 2、*表示匹配前一个字符0次或无限次；
# 3、+或*后跟？表示非贪婪匹配，即尽可能少的匹配，如*？重复任意次，但尽可能少重复；
# 4、 .*? 表示匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复。
# 如：a.*?b匹配最短的，以a开始，以b结束的字符串。如果把它应用于aabab的话，它会匹配aab和ab。
# 若以a.*b匹配如上的字符串，通常的行为是匹配尽可能多的字符所以她将匹配 aabab。.*默认的贪婪匹配
# (?=…) 比如.a(?=bbb)顺序环视 表示a后面必须紧跟3个连续的b
# (?!…) 比如.a(!=bbb)前视取反 表示a后面不能紧跟3个连续的b
# (?<=…) 匹配字符串的当前位置，它的前面匹配 … 的内容到当前位置 如 (?<=abc)def ，并不是从 a 开始搜索，而是从 d 往回看的
# 参考 https://docs.python.org/zh-cn/3.7/library/re.html#re.search

import re

patten = r"zhao"
param = r"zhaoZhaoZHAOisagoodman"
# 1
result = re.match(patten, param)
print(result.group())
# 2
prog = re.compile(patten, re.I)
result = prog.findall(param)
print(result)

result = prog.search(param)
print(result.group())

key = "<html><body><h1>hello world</h1></body></html>"  # 这段是你要匹配的文本
p1 = "(?<=<h1>).+?(?=</h1>)"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
matcher1 = re.search(pattern1, key)  # 在源文本中搜索符合正则表达式的部分
print(matcher1.group())  # 打印出来

key = r"javapythonhtmlvhdl"  # 这是源文本
p1 = r"python"  # 这是我们写的正则表达式
pattern1 = re.compile(p1)  # 同样是编译
matcher1 = re.search(pattern1, key)  # 同样是查询
print(matcher1.group())
# re.match与re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。


key = r"mat cat hat pat"
p1 = r"[^p]at"  # 这代表除了p以外都匹配
pattern1 = re.compile(p1)
print(pattern1.findall(key))

key = r"chuxiuhong@hit.edu.cn"
p1 = r"@.*?\."  # 我想匹配到@后面一直到“.”之间的，在这里是hit
pattern1 = re.compile(p1)
print(pattern1.findall(key))

m = re.search('(?<=abc)def', 'abcdef')
print(m.group())

m = re.search(r'(?<=-)\w+', 'spam-egg')
print(m.group())
