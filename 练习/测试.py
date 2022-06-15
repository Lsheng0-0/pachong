# -*- coding: UTF-8 -*-
from time import sleep
import sys, io

import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# 解决  'gbk' codec can't encode character '\xa0' inposition 3330问题
from bs4 import BeautifulSoup

url = 'https://www.2meinv.com/article-2585.html'
while True:
    if url is not None:
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        # print(resp.text)
        resp.close()

        img_page = BeautifulSoup(resp.text, "html.parser")
        img_href = img_page.find("div", class_="pp hh").find_all('a')
        #print(img_href)
        for b in img_href:
            imgage = b.find('img')
            src = imgage.get('src')
            #print(src)
            # 下载图片
            img_resp = requests.get(src)
            # img_resp.content #这里拿到的是字节
            img_name = src.split("/")[-1]  # 拿到url中最后的一个/以后的内容
            with open("../img/" + img_name, mode="wb") as f:
                f.write(img_resp.content)  # 打印写入
                print("over", img_name)
            url = b.get('href')
            print(url)
    else:
        break