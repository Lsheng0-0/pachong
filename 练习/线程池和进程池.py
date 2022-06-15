# -*- coding: UTF-8 -*-
#线程池：一次性开辟一些线程，线程任务的调度交给线程池来完成
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
    for i in range(100):
        print(name, i)

if __name__ == '__main__':
    #创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn,name=f"线程{i}")
    #等待线程池中的任务全部执行结束，才继续执行(守护)
    print("123")