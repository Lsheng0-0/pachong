# -*- coding: UTF-8 -*-
"""
流程：
1.拿到/43614-1-1.html
2.从源代码中提取m3u8的url
3.下载m3u8
4.读取m3u8文件，下载视频
5.合并视频
"""
import io
from time import time

import re
import sys
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# 解决  'gbk' codec can't encode character '\xa0' imposition 3330问题

# obj = re.compile(r'"url":"(?P<m3u8>.*?)",',re.S)
# url = 'https://www.91jinsu.com/vodplay/43614-1-1.html'
#
# resp = requests.get(url)
# m3u8_url = obj.findall(resp.text)
# url_m = m3u8_url[1].replace("\\","")
# # print(url_m)
# #下载m3u8文件
# resp2 = requests.get(url_m)
# with open("哲仁王后.m3u8",mode="wb")as f:
#     f.write(resp2.content)
# # print(resp2.text)
# resp2.close()
# print("下载完毕！")


# 解析m3u8
# with open("哲仁王后.m3u8", mode="r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()  # 先去掉空格，空白，换行符
#         if line.startswith("#"):  # 如果以#开头，我不要
#             continue
#         print(line)
#         f.close()

# url = 'https://b1.szjal.cn/ppvod/ADECDE4B56A9B24907EB74F174B0F863.m3u8'

# resp = requests.get(url)
# print(resp.text)
# with open("哲仁王后.m3u8",mode="wb")as f:
#     f.write(resp.content)
# # print(resp2.text)
# resp.close()
# print("下载完毕！")
# 解析m3u8
name = 1
with open("哲仁王后.m3u8", mode="r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # 先去掉空格，空白，换行符
        if line.startswith("#"):  # 如果以#开头，我不要
            continue
        print(line)
        # 下载片段
        url_ts = 'https://b1.szjal.cn' + line
        resp_vedio = requests.get(url_ts)

        with open(f'vedio/{name}.ts', mode="wb") as ff:
            ff.write(resp_vedio.content)
            name += 1
            print("%d：下载完成！" % name)
            ff.close()
            resp_vedio.close()
