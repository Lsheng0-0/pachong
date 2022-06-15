import io
import sys
import xml

import requests
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# 解决  'gbk' codec can't encode character '\xa0' inposition 3330问题
url = 'https://jiujiang.zbj.com/sem/index/'

resp = requests.get(url)
#print(resp.text)
#解析
html = etree.HTML(resp.text)
#print(html)
#拿到每一个服务商的div
divs = html.xpath("/html/body/div[1]/div[7]/div[4]/div/div[4]/div[1]")
print(divs)
resp.close()
for div in divs:#每一个服务商的div/html/body/div[1]/div[7]/div[4]/div/div[4]/div[1]/div[1]/div/div[2]/div[4]/div[1]
    price = div.xpath("./div[1]/div/div[2]/div[4]/div[1]/text()")
    # title = "saas".join(div.xpath("./div/div/div/p/a/text()"))#"saas".join拼接
    print(price)

