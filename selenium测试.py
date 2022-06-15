# -*- coding: UTF-8 -*-
from time import sleep

from selenium.webdriver import Firefox, Keys
from selenium.webdriver.common.by import By

dr = Firefox()
'''
url = 'https://www.lagou.com/'
dr.get(url)
sleep(3)
# 找到全国元素，点击
dr.find_element(By.XPATH, '/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/p[1]/a/i').click()

sleep(3)  # 页面刷新
# 找到输入框，输入python => 输入回车
dr.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("python", Keys.ENTER)
sleep(3)

# li_list = dr.find_elements(By.XPATH,'/html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div')
# for li in li_list:
#     job_name = li.find_element(By.TAG_NAME,'a').text
#     job_need = li.find_element(By.XPATH, './div/div/div[2]').text
#     print(job_name+':'+job_need)
#

dr.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[1]').click()
sleep(3)
# 窗口切换
dr.switch_to.window(dr.window_handles[-1])
sleep(3)
# 新窗口提取内容
job_txt = dr.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[1]').text
print(job_txt)
#关闭当前窗口，再回到主窗口
dr.close()
dr.switch_to.window(dr.window_handles[0])
sleep(3)
'''
'''
dr.get("https://www.yunbtv.net/vodplay/fanrenxiuxianchuan-2-1.html")
sleep(3)
# 处理iframe的话，必须先拿到iframe，然后切换视角到iframe，再然后才可以拿到数据
iframe = dr.find_element(By.XPATH, '/html/body/section[2]/div/div[1]/div[1]/div/table/tbody/tr/td/iframe')

# dr.switch_to.frame(iframe)  # 切换到iframe
# dr.switch_to.default_content()  # 切换到原页面

sleep(3)
text = iframe.find_element(By.XPATH, '/html/body/div/xg-controls/xg-fullscreen/xg-icon/div[1]/svg/path').text
print(text)
sleep(3)
input("回车关闭：")
'''


dr.close()
