#Used to do multiple work/resoureces parallely

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)

# def main():
    # time1=time.perf_counter()
    #Normal function call works step by step
    # func(4)
    # func(5)
    # func(3)


    #function work all at a time 
    # t1=threading.Thread(target=func,args=[4])
    # t2=threading.Thread(target=func,args=[5])
    # t3=threading.Thread(target=func,args=[3])

    # t1.start()
    # t2.start() 
    # t3.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # time2=time.perf_counter()
    # print(time2-time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # f1=executor.submit(func,4)
        # f2=executor.submit(func,5)
        # f3=executor.submit(func,3)

        # print(f1.result())
        # print(f2.result())  
        # print(f3.result())
        l=[5,4,3]
        r=executor.map(func,l)
        for result in r:
            print(result)


poolingDemo()

# resoures "Concurrent.futures" is used to do multiple work parallely