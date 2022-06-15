# -*- coding: UTF-8 -*-
# 线程,进程
# 进程是资源单位,每一个进程至少要有一个线程
# 线程是执行单位


# 启动每一个程序默认都会有一个主线程

# 多线程
from threading import Thread  # 线程类
from time import sleep


def func(name):
    for i in range(100):
        print(name, i)
        sleep(0.1)


#
# def main():
#     for i in range(100):
#         print("main", i)
#         sleep(0.1)
#
#
# if __name__ == "__main__":
#     thread_func = Thread(target=func)
#     thread_main = Thread(target=main)
#     thread_func.start()#多线程状态可以开始工作状态，具体的执行时间由cpu决定
#     thread_main.start()
#     for i in range(100):
#         print("pppppppppppppppp", i)
#         sleep(0.1)


# class MyThread(Thread):
#     def run(self): #固定的  ->当线程被执行的时候，被执行的就是run()
#         for i in range(100):
#             print("子线程",i)

if __name__ == '__main__':
    t1 = Thread(target=func, args=('周杰伦',))  # 传参，元组
    t2 = Thread(target=func, args=('王力宏',))
    # t.run() #方法调用了，成单线程
    t1.start()  # 开启线程
    t2.start()
    # for i in range(100):
    #     print('主---线程',i)
