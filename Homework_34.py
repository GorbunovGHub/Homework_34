from threading import Thread
import time


def my_list_int():
    list_int = range(1, 11)
    for i in list_int:
        print(i)
        time.sleep(1)


def my_list_str():
    list_str = list([chr(i) for i in range(97, 107)])
    for i in list_str:
        print(i)
        time.sleep(1)


thr_first = Thread(target=my_list_int)
thr_second = Thread(target=my_list_str)

thr_first.start()
thr_second.start()

thr_first.join()
thr_second.join()
