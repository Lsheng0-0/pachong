# -*- coding: UTF-8 -*-
# 登录-得到cookie
# 带着cookie去请求

# 必须把上面两个操作连起来
# 我们可以使用session进行请求--session可以任务是一串的请求，在这个过程中的cookie不会丢失
import requests

# 会话

url = "https://passport.17k.com/ck/user/login"

data = {
    'loginName': '13507922019',
    'password': 'dj1522833718'
}
session = requests.session()
resp = session.post(url, data=data)
# print(resp.text)

# 拿到书架上的数据
# 刚才的那个session中是有cookie的
resp = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
print(resp.json())
resp.close()
