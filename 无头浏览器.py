# -*- coding: UTF-8 -*-
import time
from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select

url = "https://lsheng0-0.github.io/index.html"
# 无头浏览器参数配置
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

dr = Firefox(options=opt)
dr.get(url)

sleep(3)
'''
# dr.find_element(By.XPATH, '/html/body/main/div/div/div/div/div[3]/div[2]/div[1]/div/div/a[2]').click()
# 定位到下拉列表
sel_el = dr.find_element(By.XPATH, '')
# 对元素进行包装，包装成下拉菜单
sel = Select(sel_el)
# 让浏览器进行调整选项
for i in range(len(sel.options)):  # i 就是一个下拉框选项的索引位置
    sel.select_by_index(i)  # 按照索引进行切换
    # 窗口切换
    dr.switch_to.window(dr.window_handles[-1])
    title = dr.find_element(By.XPATH, '/html/body/main/div/div/div/div/div[1]/div[1]').text
    print(title)
    time.sleep(2)
'''
# 执行elements(经过数据加载，js请求之后的结果，html内容)
print(dr.page_source.encode('utf-8'))  # dr.page_source提取页面源代码

input("回车关闭：")
dr.close()
