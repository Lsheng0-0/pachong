# -*- coding: UTF-8 -*-
import io
import aiofiles
import re
import sys
from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# 解决  'gbk' codec can't encode character '\xa0' imposition 3330问题
'''
1.同步操作：getCatlog拿到所有的章节的连接和名称
2.异步操作：访问getChapterContent 下载所有的文章内容
'''


async def book_down(cid, title, aid):
    get_list = []
    url = f'http://www.wibaidu.com/modules/article/reader.php?aid={aid}&cid={cid}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.text()
            # print(dic)
            ret = re.compile(r'<dd id="contents">(?P<all>.*?)</dd>', re.S).findall(dic)
            ret2 = re.compile(r"&nbsp;&nbsp;&nbsp;&nbsp;(?P<text>.*?)<br />.*?", re.S).finditer(str(ret))
            for i in ret2:
                get_list.append(i.group('text'))
            # print(get_list)
            async with aiofiles.open('text/' + title + '.csv', mode="w", encoding="utf-8") as f:  # aiofile.open ：异步打开文件
                for i in get_list:
                    await f.write(i + '\n')
                    print(title + "写入完成")


async def book_scr(url):
    resp = requests.get(url)
    resp.encoding = 'gbk'
    # print(resp.text)
    resp.close()

    # 把源代码交给bs4
    task = []

    main_page = BeautifulSoup(resp.text, "html.parser")
    href = main_page.find('table', cellspacing="1", cellpadding="0", bgcolor="#E4E4E4", id="at").find_all('a')
    for i in href:
        src = i.get("href")
        title = i.text
        cid = src.split('=')[-1]
        # print(cid, title)
        task.append(book_down(cid, title, aid))
    # print(task)
    # asyncio.run(asyncio.wait(task))
    await asyncio.wait(task)


if __name__ == '__main__':
    aid = 19368
    url = f"http://www.wibaidu.com/modules/article/reader.php?aid={aid}"
    asyncio.run(book_scr(url))
