# -*- coding: UTF-8 -*-
# 1.找到未加密的参数                     #window.arsea(参数，xxx,xxx,xxx)
# 2.想办法把参数进行加密(必须参考网易的逻辑)，params => encText， encSecKey=>encSecKey
# 3.请求到网易，拿到评论信息
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# 解决  'gbk' codec can't encode character '\xa0' imposition 3330问题
import requests
# 需要安装pycryptodome模块
from Crypto.Cipher import AES
from base64 import b64encode
import json


url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

# 请求方式是post
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",  # 一页多少条
    "rid": "R_SO_4_1940770243",
    "threadId": "R_SO_4_1940770243"
}
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
e = '010001'
g = "0CoJUm6Qyw8W8jud"
i = "FADzYhQBSZDSSXoM"


def get_encSecKey():
    return "509ddb4b358d77d52a276ece74d81ac1d0b068c9f71e30ccde1cac044a89e551eb9b8ff69078d615266f5bbbc1649f5c71f474fed241b464ee513d6d01d2cff313b8a98d494324bdab1bb642d52c6b650ef56f78c6a7ad89be054a9ec1c80010ba1dd5aa69f606eb2b2f7391d67446784a17aa8efcf598eca0cd7d7d8b163974"


def get_params(data):  # 默认收到的是字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second  # 返回的是params


# ValueError: Data must be padded to 16 byte boundary in CBC mode  报错，加密的长度必须是16的倍数char(2)..
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data, key):  # 加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)  # 创建加密器
    bs = aes.encrypt(data.encode("utf-8"))  # 加密
    return str(b64encode(bs), "utf-8")  # 字符串转换


# 处理加密过程
'''
function a(a = 16) {  #随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  #循环16次
            e = Math.random() * b.length,#随机数
            e = Math.floor(e),#取整
            c += b.charAt(e); #取字符串中的xxxx位置 b
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)  #b是秘钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)  #e是数据
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d, #偏移量
            mode: CryptoJS.mode.CBC #模式：cbc
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {     #d= data e= 010001 f= "xxxxx"
    g= "0CoJUm6Qyw8W8jud"
        var h = {} #空对象
          , i = a(16);  #i就是一个16位的随机值
        return h.encText = b(d, g), #g是秘钥
        h.encText = b(h.encText, i),#返回的encText  ， i是秘钥
        h.encSecKey = c(i, e, f),#返回的encSecKey #e，f是定值，i是随机数  如果我们把i固定，key就是固定的
        h
        #encText两次加密
        1.b（data+g）
        2.encText+i
    }
'''

resp = requests.post(url, data={
    'params': get_params(json.dumps(data)),  # 这里json windows要转换成utf-8编码
    'encSecKey': get_encSecKey()
})
dic = resp.json()

resp.close()

content = dic['data']['comments']
for i in content:
    print(i['user']['nickname'] + ':' + i['content'])
