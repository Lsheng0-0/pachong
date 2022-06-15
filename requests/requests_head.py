# -*- coding: UTF-8 -*-
import requests

query = input("输入爬取的网址：")
url = f'https://{query}'

headers= {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
}


respone = requests.get(url, headers=headers)
print(respone.text)    #拿到html文本
respone.close()