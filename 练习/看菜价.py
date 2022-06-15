# -*- coding: UTF-8 -*-
import re

from bs4 import BeautifulSoup

import requests

url = 'http://xinfadi.com.cn/getCat.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
data = {
    'prodCatid': 1186
}

respone = requests.post(url, headers=headers, data=data)
# print(respone.json())

respone.close()
get = respone.text
obj = re.compile(r'prodName":"(?P<name>.*?)",.*?lowPrice":"(?P<low>.*?)",.*?highPrice":"(?P<high>.*?)",.*?'
                 r'avgPrice":"(?P<avg>.*?)",.*?place":"(?P<place>.*?)",.*?unitInfo":"(?P<info>.*?)",.*?',re.S)
ret = obj.finditer(get)
for i in ret:

    # print(i.group("name","low","high","avg","place","info"))
    dic = i.groupdict()
    print(dic)


# from bs4 import BeautifulSoup

# 解析数据
# 1.把页面源代码交给BeautifulSoup进行处理，生成bs对象
# page = BeautifulSoup(respone.text, "html.parser")  # 指定html解析器
# 2.从bs对象中查找数据
# find(标签，属性=值)
# find_all(标签,属性=值)
# table = page.find("table",attrs={"class_="hq_table"})#class是py的关键字
# table = page.find("ul", attrs={"class": "nav dropdown-menu"})
# print(table)
# trs = table.find_all("li")[1:]
# 拿到所有数据行
# print(trs)
# for tr in trs:
#     tds = tr.find_all("td")  # 拿到每行中的所有td
#     name = tds[0].text  # .text表示拿到被标签标记的内容
#     cat = tds[0].text  # .text表示拿到被标签标记的内容
#     price = tds[0].text  # .text表示拿到被标签标记的内容
#     con = tds[0].text  # .text表示拿到被标签标记的内容
#     avg = tds[0].text  # .text表示拿到被标签标记的内容
#     low = tds[0].text  # .text表示拿到被标签标记的内容
#     high = tds[0].text  # .text表示拿到被标签标记的内容
#     print(tds,name,cat,price,con,avg,low,high)
