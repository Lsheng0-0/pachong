# -*- coding: UTF-8 -*-
import asyncio
import os

import aiofiles
import aiohttp
import re
import requests
import io
import sys
from Crypto.Cipher import AES

'''
1.拿到主页面的页面代码，找到iframe
2.从iframe的页面源代码中拿到m3u8
3.下载第一层的m3u8 ->下载第二层的m3u8文件(视频存放路径)
4.下载视频
5.下载秘钥，进行解密
6.合并所有的ts文件为一个MP4文件
'''
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# 解决  'gbk' codec can't encode character '\xa0' imposition 3330问题
def get_iframe_src(url):
    # iframe 地址
    iframe_src = 'https://vip.m1902.com/dp/?url=https://pps.sd-play.com/20220427/pyqCdBbv/index.m3u8'
    return iframe_src


def get_first_m3u8_url(url):
    resp = requests.get(url)
    # print(resp.text) #测试
    obj = re.compile(r'"urls":"(?P<_urls>.*?)",', re.S)
    resp_ = obj.findall(resp.text)[0]
    return resp_


def downlode_m3u8_url(url, name):  # 下载m3u8
    resp = requests.get(url)
    with open(name, mode="wb") as f:
        f.write(resp.content)


async def downlode_ts(url_ts, name, session):
    async with session.get(url_ts) as resp:
        async with aiofiles.open(f"vedio/{name}", mode="wb") as f:
            await f.write(await resp.content.read())  # 把下载到的内容写入到文件中
    print(f"{name}：下载完毕！")


async def aio_downlode():
    tasks = []
    async with aiohttp.ClientSession() as session:  # 提前准备好session
        async with aiofiles.open("重生之门第一集_m3u8_2.txt", mode="r", encoding="utf-8") as f:
            async for line in f:
                if str(line).startswith("#"):
                    continue
                line = str(line).strip()
                # print(line)
                name = line.split('/hls/')[1]
                # print(name)
                task = asyncio.create_task(downlode_ts(line, name, session))  # 创建协程任务
                tasks.append(task)
            await asyncio.wait(tasks)


def get_key(url):
    resp = requests.get(url)
    return resp.text


async def dec_ts(name, key):
    aes = AES.new(key=key.encode('utf-8'), IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"vedio/{name}", mode="rb") as f1, \
            aiofiles.open(f"vedio/temp_{name}", mode="wb") as f2:
        bs = await f1.read()  # 从源文件读取内容
        await f2.write(aes.decrypt(bs))  # 把解密好的内容写入文件
    print(f"{name}:解密完毕!!")


async def aio_dec(key):
    tasks = []
    async with aiofiles.open("重生之门第一集_m3u8_2.txt", mode="r", encoding="utf-8") as f:
        async for line in f:
            if str(line).startswith("#"):
                continue
            line = str(line).strip()
            name = line.split('/hls/')[1]
            # 开始创建异步任务
            task = asyncio.create_task(dec_ts(name, key))
            tasks.append(task)
        await asyncio.wait(tasks)


def merge_ts():
    lib = []
    # mac: cat 1.ts 2.ts 3.ts > xxx.mp4
    # win: copy /b 1.ts+2.ts+3.ts xxx.mp4
    with open("重生之门第一集_m3u8_2.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            if str(line).startswith("#"):
                continue
            line = str(line).strip()
            name = line.split('/hls/')[1]
            lib.append(f"vedio/temp_{name}")
        copy_lib = "+".join(lib)

        os.system(f"copy /b {copy_lib} chongshengzhimendiyiji.mp4")
        print('合并完成.')
        print(f"copy /b {copy_lib} chongshengzhimendiyiji.mp4" )


def main(url):
    """
    # 1.拿到主页面的源代码，找到iframe对应的url
    iframe_src = get_iframe_src(url)
    # 2.拿到第一层的m3u8文件的下载地址
    first_m3u8_url = get_first_m3u8_url(iframe_src)
    # 3.下载第一层m3u8文件
    downlode_m3u8_url(first_m3u8_url, '重生之门第一集_m3u8.txt')
    # 3.2.下载第二层m3u8文件
    url_top = first_m3u8_url.split("/20220427")[0]
    with open("重生之门第一集_m3u8.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            first_m3u8_url_2 = url_top + line
    downlode_m3u8_url(first_m3u8_url_2, '重生之门第一集_m3u8_2.txt')
    f.close()
    """
    # 4.下载视频
    # 异步协程
    # asyncio.run(aio_downlode()) #测试就注释
    # 5.1拿到秘钥
    # key_url = "https://pps.shanshanku.com/20220427/pyqCdBbv/1200kb/hls/key.key"  # 偷看，没有open去文件找
    # key = get_key(key_url)
    # 5.2解密
    # asyncio.run(aio_dec(key))  # 测试就注释

    # 6.0 合并ts文件
    merge_ts()


if __name__ == '__main__':
    url = 'http://www.pianku.top/vodplay/34332-1-1.html'

    main(url)
