# -*- coding: UTF-8 -*-
# 1.拿到网站提取子页面的地址链接，href
# 2.通过url拿到子页面的内容，从子页面中找到图片的下载地址img->src
# 3.下载图片
from time import sleep

import requests
from bs4 import BeautifulSoup

url = 'https://www.umeitu.com/meinvtupian/rentiyishu/'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
}
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
# print(res.text)
res.close()
# 把源代码交给bs4
main_page = BeautifulSoup(res.text, "html.parser")
href = main_page.find("ul", class_="pic-list after").find_all("a")
# print(href)
for a in href:
    _img = a.get('href')
    # print(a.get('href'))  # 直接通过get拿到属性的值
    while True:
        if _img is not None:
            url_img = 'https://www.umeitu.com' + _img
            # 拿到子页面的源代码
            res_page = requests.get(url_img)
            res_page.encoding = 'utf-8'
            # print(res_page.text)
            res_page_text = res_page.text
            res_page.close()
            # 从子页面中拿到图片的下载路径
            img_page = BeautifulSoup(res_page_text, "html.parser")
            _img_href = img_page.find("section", class_="img-content").find_all('a')
            # print(_img_href)
            # 套图的下一张图的路径
            for b in _img_href:
                imgage = b.find('img')
                src = imgage.get('src')
                # print(src)
                # 下载图片
                img_resp = requests.get(src)
                # img_resp.content #这里拿到的是字节
                img_name = src.split("/")[-1]  # 拿到url中最后的一个/以后的内容
                with open("img/"+img_name, mode="wb") as f:
                    f.write(img_resp.content)  # 打印写入
                    print("over", img_name)
                    sleep(1)
                _img = b.get('href')
                # print(_img)
        else:
            break

    break
