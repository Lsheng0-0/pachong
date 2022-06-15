# -*- coding: UTF-8 -*-
# 1.定位到专栏
# 2.从专栏中提取到子页面的链接地址
# 3.请求子页面的链接地址，拿到我们想要的下载链接。。。
import csv

import re

import requests

url = "https://m.dytt8.net/index2.htm"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"

}

respone = requests.get(url, headers=headers)  # verify:去掉安全验证
respone.encoding = 'gb2312'
obj1 = re.compile(r"最新影片推荐.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'>", re.S)
obj3 = re.compile(r'◎译　　名(?P<name_ch>.*?)/.*?<a target="_blank" href="(?P<bt>.*?);dn=', re.S)
set = obj1.finditer(respone.text)
respone.close()
child_helf_list = []
bt_list = []
for i in set:
    ul = i.group("ul")
    set2 = obj2.finditer(ul)
    for i2 in set2:
        # 拼接子页面的url地址：域名+子页地址
        child_helf = "https://m.dytt8.net" + i2.group("href")
        # print(child_helf)
        child_helf_list.append(child_helf)  # 把子页链接保存的列表

    # 提取子页内容
    f = open("movie.csv", mode="a", encoding='utf-8')
    csvwriter = csv.writer(f)
    for href in child_helf_list:
        child_set = requests.get(href, headers=headers)
        child_set.encoding = 'gb2312'
        # print(child_set.text)
        child_set.close()
        set3 = obj3.search(child_set.text)
        # print(set3.group('name_ch'))
        # print(set3.group('bt'))
        dic = set3.groupdict()
        csvwriter.writerow(dic.values())
    f.close()
