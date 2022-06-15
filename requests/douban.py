# -*- coding: UTF-8 -*-
import requests

url = 'https://movie.douban.com/j/chart/top_list'
param = {
    'type': '11',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

respone = requests.get(url, params=param, headers=headers)
print(respone.json())  # 拿到html文本
respone.close()
