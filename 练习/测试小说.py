# -*- coding: UTF-8 -*-
# url = "http://www.wibaidu.com/modules/article/reader.php?aid=19368"
# urls = f'http://www.wibaidu.com/modules/article/reader.php?aid={aid}&cid={cid}'
import io
import json

import aiohttp
import requests

import re
import sys

import aiofiles

aid = 19368
cid = 6209856
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


# 解决  'gbk' codec can't encode character '\xa0' imposition 3330问题
def book_down(cid, title, aid):
    url = f'http://www.wibaidu.com/modules/article/reader.php?aid={aid}&cid={cid}'
    resp = requests.get(url)
    resp.encoding = "gbk"
    obj2 = re.compile(r"&nbsp;&nbsp;&nbsp;&nbsp;(?P<text>.*?)<br />.*?", re.S)  # re.S让。能匹配到换行符
    obj1 = re.compile(r'<dd id="contents">(?P<all>.*?)</dd>', re.S)
    ret = obj1.findall(resp.text)
    f = open('text/' + title, mode="w", encoding="utf-8")
    ret2 = obj2.finditer(str(ret))
    for i in ret2:
        get =  i.group('text')
        f.write(get)


book_down(cid=6209856, title="title.text", aid=19368)
