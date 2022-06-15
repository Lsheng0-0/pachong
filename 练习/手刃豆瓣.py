# -*- coding: UTF-8 -*-
# request 到网站信息
# 通过re 提取想要的信息
from time import sleep

import re
import csv
import requests
code = 25
while True:
    url = 'https://movie.douban.com/top250?start={cote}&filter='

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
    }

    respone = requests.get(url, headers=headers)

    page_content = respone.text
    #print(page_content)
    respone.close()
    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                     r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                     r'<span>(?P<num>.*?)</span>', re.S)
    #开始匹配
    s = obj.finditer(page_content)
    f = open("data.csv", mode="a", encoding='utf-8')
    csvwriter = csv.writer(f)
    for it in s:
        # print(it.group("name"))
        # print(it.group("score"))
        # print(it.group("num"))
        # print(it.group("year").strip())
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
    f.close()
    code = code +25
    sleep(2)
    if code >250:
        break

