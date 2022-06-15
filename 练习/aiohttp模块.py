# -*- coding: UTF-8 -*-
import requests

# requests.get() 同步的代码 ->异步操作aiohttp、
# pip install aiohttp
import asyncio
import aiohttp

urls = [
    "https://pic.netbian.com/uploads/allimg/220407/005709-16492642292e8d.jpg",
    "https://pic.netbian.com/uploads/allimg/211219/114328-16398854086bac.jpg",
    "https://pic.netbian.com/uploads/allimg/210812/234309-1628782989eba1.jpg"

]


async def aiodownlode(url):
    name = url.split("/", -1)[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name, mode="wb") as f:
                f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起
    # s= aiohttp.ClientSession() === requests
    # requests.get()  .post()
    # 发送请求
    # 得到图片内容
    # 保存到文件
    print(name, "完成")


async def main():
    task = [asyncio.create_task(aiodownlode(url)) for url in urls]
    await asyncio.wait(task)


if __name__ == '__main__':
    asyncio.run(main())
