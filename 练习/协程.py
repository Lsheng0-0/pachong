# -*- coding: UTF-8 -*-
# 一般情况下当程序处于io操作，线程都会处于阻塞状态
# 协程：当任务处于阻塞状态，可以选择性的切换到其他的任务上
# 多任务异步操作
# 单线程条件下
import asyncio
from time import sleep, time


# async def func():
#     print("yyds")
#     # sleep(3)  # 让当前的线程处于阻塞状态,cpu是不为我工作的
#     # print("ysdsddsdsds")
#
#
# if __name__ == '__main__':
#     #此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     #print(func())
#     asyncio.run(func())

async def func1():
    print("yyds")
    # sleep(3)#当程序出现了同步操作的时候异步中断了
    await asyncio.sleep(3)  # await： 挂起 asyncio.sleep：异步睡眠
    print("ysdsddsdsds")


async def func2():
    print("qqqqqq")
    await asyncio.sleep(2)
    print("qqqqqqqaaaaaaaaaaaa")


async def func3():
    print("zzzzzzzzzzz")
    await asyncio.sleep(4)
    print("zzzzzzzzcccccc")


async def main():
    # #第一种写法
    # f1 = func1()
    # await f1#一般await挂起操作放在协程对象前面
    # 第二种写法
    # f1 = func1()
    # f2 = func2()
    # f3 = func3()
    task = [
        # func1(),func2(),func3()
        asyncio.create_task(func1()),  # 3.8之后需要创建task对象
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(task)
    #await asyncio.gather(*task) *传参


if __name__ == '__main__':
    # f1 = func1()
    # f2 = func2()
    # f3 = func3()
    # task = [
    #     f1, f2, f3
    # ]
    # t1 = time()
    # # 一次性启动多个任务(协程)
    # asyncio.run(asyncio.wait(task))
    # t2 = time()
    # print(t2 - t1)
    t1 = time()
    asyncio.run(main())
    t2 = time()
    print(t2 - t1)

"""
# 在爬虫领域的应用
async def download(url):
    print("准备开始下载")
    await asyncio.sleep(2)  # 网络请求 await asyncio.requests.get()
    print(url)


async def main():
    urls = [
        "http://www.bilibili.com",
        "http://www.baidu.com",
        "http://www.163.com"
    ]
    task = []
    for url in urls:
        d = asyncio.create_task(download(url))
        task.append(d)
    
    #task = [asyncio.create_task(download(url))for url in urls]

    await asyncio.wait(task)


if __name__ == '__main__':
    asyncio.run(main())
"""
