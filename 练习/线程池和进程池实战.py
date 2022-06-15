# -*- coding: UTF-8 -*-
# 1.如何提取单个页面的数据
# 2.上线程池，多个页面同时抓取
from time import sleep

import requests
import json
import csv
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

f = open("data_xinfadi.csv", mode="w", encoding="utf-8")
csvwrite = csv.writer(f)


# txt = (item.replace("\\","").replace("/","") for item in txt) #生成器 for item in txt
def down_first_page(url, page):
    data = {
        'limit': 20,
        'current': f'{page}',
        'pubDateStartTime': '',
        'pubDateEndTime': '',
        'prodPcatid': '',
        'prodCatid': '',
    }
    resp = requests.post(url, data=data)
    rest = json.loads(resp.text)
    list_resp = rest["list"]
    for i in list_resp:
        prodName = i['prodName']
        lowPrice = i['lowPrice']
        highPrice = i['highPrice']
        avgPrice = i['avgPrice']
        place = i['place']
        unitInfo = i['unitInfo']
        pubDate = i['pubDate']
        text = "品名：" + prodName, "最低价：" + lowPrice, "最高价：" + highPrice, "平均价：" + avgPrice, "产地：" + place, "单位：" + unitInfo, "发布时间：" + pubDate
        csvwrite.writerow(text)
    print(url + page, "提取完毕！")
    resp.close()


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 20):
            t.submit(down_first_page, url='http://www.xinfadi.com.cn/getPriceData.html', page=f'{i}')

    print("全部下载完毕！！")


