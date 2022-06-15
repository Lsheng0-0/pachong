# -*- coding: UTF-8 -*-
import io
import sys

import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# 解决  'gbk' codec can't encode character '\xa0' imposition 3330问题
url = 'https://www.pearvideo.com/video_1760587'

contId = url.split("_")[1]

video_url = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.5516830196156912 '

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 '
                  'Safari/537.36 ',
    'Referer': 'https://www.pearvideo.com/video_1760587'
}
# 防盗链
resp = requests.get(video_url, headers=headers)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
resp.close()
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")  # 替换
# https://video.pearvideo.com/mp4/adshort/20220429/cont-1760587-15871613_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20220429/1651310699733-15871613_adpkg-ad_hd.mp4
# https://www.pearvideo.com/video_1760587

# print(srcUrl)

# 下载视频
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
f.close()