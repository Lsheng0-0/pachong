# -*- coding: UTF-8 -*-
from time import sleep
from urllib.request import urlopen

url = "https://movie.douban.com/top250"
respone = urlopen(url)


resp = respone.read().decode("utf-8")
print(resp)
with open("myblog.html", "w", encoding='utf-8') as f:#encoding='utf-8'：编码错误解决乱码问题
    f.write(resp)
    sleep(1)
    f.close()
print('完成!')
respone.close()