# -*- coding: UTF-8 -*-

import sys
import requests

def word():
    while True:
        word = input("输入需要翻译的单词：")
        if  word != "q":
            url = 'https://fanyi.baidu.com/sug'

            data = {
                "kw": {word}
            }
            respone = requests.post(url, data=data)
            print(respone.json())  # 拿到html文本
            respone.close()

        else:
            sys.exit()

word()