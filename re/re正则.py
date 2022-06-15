# -*- coding: UTF-8 -*-
import re

# # findall:匹配所有字符串符合正则的内容
# list = re.findall(r"\d+", '你的电话是多少：2617238318,身份证是：12728193913013029')
# print(list)
#
# # finditer: 匹配字符串中所有的内容[返回的是迭代器],从迭代器中拿内容需要。group()
# list = re.finditer(r"\d+", '你的电话是多少：2617238318,身份证是：12728193913013029')
# print(list)
# for i in list:
#     print(i.group())
#
# #search, 找到一个结果就返回，返回的结果是match对象，拿数据需要。group()
# str = re.search(r"\d+", '你的电话是多少：2617238318,身份证是：12728193913013029')
# print(str.group())

# #match是从头开始匹配
# str = re.match(r"^\d+", '2617238318,身份证是：12728193913013029')
# print(str.group())

#预加载正则表达式
# obj = re.compile(r"\d+")
# ret = obj.finditer("你的电话是多少：2617238318,身份证是：12728193913013029")
# for i in ret:
#     print(i.group())

s= """
<div class = 'jay'><span id= '1'>没头脑</span></div>
<div class = 'adfg'><span id= '2'>没头脑</span></div>
<div class = 'eesd'><span id= '3'>没头脑</span></div>
<div class = 'caf'><span id= '4'>没头脑</span></div>
<div class = 'jvrwq'><span id= '5'>没头脑</span></div>
"""
# (?P<分组名字>正则),进一步提取内容
obj = re.compile( )#re.S让。能匹配到换行符
ret = obj.finditer(s)
for i in ret:
    print(i.group('zc'),i.group('id'),i.group('name'))