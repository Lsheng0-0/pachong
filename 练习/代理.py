# -*- coding: UTF-8 -*-
#通过第三方的机器区发送请求

import requests
#218.60.8.83:3129
proxies = {
    "https":"https://218.60.8.83:3129"
}
resp = requests.get("https://www.baidu.com/",proxies=proxies)
resp.encoding= "utf-8"
print(resp.text)
