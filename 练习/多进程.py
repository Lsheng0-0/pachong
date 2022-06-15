# -*- coding: UTF-8 -*-
from time import sleep
from multiprocessing import Process


def func():
    for i in range(1000):
        print("func", i)


class MyThread(Process):
    def run(self):  # 固定的  ->当线程被执行的时候，被执行的就是run()
        for i in range(100):
            print("子线程", i)
            sleep(0.1)


if __name__ == '__main__':
    p = MyThread()
    p.start()  # 开启线程
    for i in range(100):
        print('主---线程', i)
        sleep(0.1)

