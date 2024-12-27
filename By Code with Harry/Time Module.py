import time

#time.time
def usingwhile():
    i=0
    while i<1000:
        i+=1
        print(i)

def usingfor():
    for x in range(1000):
        print(x)

init=time.time()        

usingfor()
t1=(time.time()-init)

init=time.time()
usingwhile()
print(time.time()-init)
print(t1)


#time.sleep
print(4)
time.sleep(3) #  code will not run for 3 seconds.
print('This is printed after 3 seconds')


#strftime
t=time.localtime() 
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)