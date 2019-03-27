# -*- coding: UTF-8 -*-
# py文件默认是ASCII格式，解决中文保存问题
'''
获取当前路径下的文件，并将文件名重构
这是批量修改文件名称的py脚本，主要用到的方法是os模块中的listdir方法和rename方法

'''

import os

files = os.listdir(".")
# 获取当前目录
cwd = os.getcwd()
# print(cwd)

i = 1
# 迭代当前目录下的文件
for item in files:
    # print(item)
    # 获取文件的名称和后缀名
    portion = os.path.splitext(item)
    # 文件名
    # print(portion[0])
    # 文件后缀
    # print(portion[1])
    # 重命令png文件
    fileName = portion[0]
    fileTail = portion[1]
    if fileTail == ".png" or fileTail == ".gif":
        print(fileTail)
        # 旧文件
        oldFile = cwd + item
        # 新文件
        newFile = cwd + fileName + "_" + i + fileTail
        # 重命令文件
        os.renames(oldFile, newFile)
        i += 1
print("此次处理了{}个文件".format(i - 1))
