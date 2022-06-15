import os
import requests
from bs4 import BeautifulSoup
import re
import urllib
import time

header = {'Referer': 'http://www.kuaikanmanhua.com/',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
# 访问网站的头，避免被认为爬虫的基本操作
dir = "快看漫画/"
# 某个漫画的第一话内容，或者说是你要爬取的起始那话的链接
url = "https://www.kuaikanmanhua.com/web/comic/312005/"
# url = "https://www.kuaikanmanhua.com/web/comic/157885/"
# 爬取的漫画网站网址，作为拼接时使用
half_url = "https://www.kuaikanmanhua.com"
# 全局变量，保证自己知道
n = 1
s = requests.session()
s.headers = header


# 获取图片的链接，此处的函数时获取网站图片的链接，因为设置到查找链接的条件，所以找到的链接全部都是本url的漫画图，返回的是一个图片的列表（数组）
def get_imageurl(url):
    a = []
    global s
    html = s.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    img_links = soup.select('.kklazy')
    for img_link in img_links:
        a.append(img_link['data-kksrc'])
    return a


# 获取下一话的一半网址，因为要和该网站的网址进行拼接才可以访问。基本上就是通过正则表达式找到下一话对应的链接
def get_next(url):
    next = ""
    con = requests.get(url)
    content = BeautifulSoup(con.content, "lxml")
    li = content.find_all("ul", class_="clearfix")
    for i in range(len(li)):
        if i == 1:
            a = str(li[i].find_all("li")[-1])
            # 通过正则表达式截取相应的字符
            p = "\"/.+?\""
            pattern = re.compile(p)
            if len(pattern.findall(a)) == 0:
                print("最后！")
            else:
                next = pattern.findall(a)[0]
                next = str(next)[1:-1]
    return next


# 创建保存图片的文件夹，逻辑基本上就是有则忽略，无则创建
def createpath(path):
    flag = True
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    else:
        flag = False
    return flag


# 保存图片，我们之前已经获得了一个图片的列表，所以此时我们可以访问指定的地址获取该图片并保存
def save_img(urllist, dir):
    global s
    global n
    index = 0
    count = 1
    path = dir + "\\" + str(n)
    createpath(path)
    n += 1
    for i in urllist:
        # path = dir + "\\" + str(n)
        if int(index / 75) >= 1:
            count += 1
            path = dir + "\\" + str(n - 1) + "-" + str(count)
            index = 0
        if not os.path.exists(path): os.makedirs(path)
        img_name = str(index) + ".jpg"
        image = path + "\\" + img_name
        res = s.get(i)
        with open(image, 'wb') as f:
            f.write(res.content)
            f.close()
        index += 1
        time.sleep(0.2)  # 自定义延时
    return True


print(get_next(url))

# 主函数，大家可以按照漫画的话数设置的循环，大家也可以根据是否可以获得下一话的链接来决定是否跳出循环。
if __name__ == "__main__":
    nurl = url



    for i in range(200):
        nt = get_next(nurl)
        if len(nt) == 0:
            break
        if i == 0:
            lt = get_imageurl(url)
            save_img(lt, dir)
        else:
            print("nurl", nurl)
            nurl = half_url + nt
            lt = get_imageurl(nurl)
            save_img(lt, dir)
    print("保存成功！")

