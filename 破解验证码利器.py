# -*- coding: UTF-8 -*-

# 1.图像识别
# 2.选择互联网上成熟的验证码破解工具
from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from chaojiying import Verification

url = 'http://www.chaojiying.com/user/login/'

dr = Firefox()
dr.get(url)
sleep(2)
img = dr.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
sleep(2)
# 处理验证码
verify = Verification()
verify_code = verify.verification_code('lsheng', 'dj1522833718', '932934',img)
print(verify_code['pic_str'])
sleep(2)

# 登录 账号密码验证码
dr.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('lsheng')
dr.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('dj1522833718')
dr.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code['pic_str'])
dr.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
sleep(1)

input("登陆成功！")
dr.close()
