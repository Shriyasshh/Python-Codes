import time
import asyncio
import requests


async def func1():
    print('func1')
    Url="https://imgs.search.brave.com/pmNCX7oy9e9Rc8BwRUVET4OPsv3qz3JsOKqXCiJ7DPQ/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA1LzcwLzkyLzQ3/LzM2MF9GXzU3MDky/NDcwNF9DUkZzZTZy/SHZKR1c4YkRYOUNo/Q1BOdmZTRzB3eW9Z/di5qcGc"
    r=requests.get(Url)
    open("image1.jpg","wb").write(r.content)
    # await asyncio.sleep(1)
    
    return 'Bob1'

async def func2():
    print('func2')
    Url="https://imgs.search.brave.com/nYzdj93kjyehvya9Y4JQjKC2gIq9VAKUv1tDvfTGnGI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzA2LzU5LzM4LzM2/LzM2MF9GXzY1OTM4/MzYyN19VdHBIMThv/R0YwUWxzRWtoZzBT/bjV6VkpJVmxhb0Jz/Zy5qcGc"
    r=requests.get(Url)
    open("image2.jpg","wb").write(r.content)
    # await asyncio.sleep(1)
    
    return 'Bob2'

async def func3():
    print('func3')
    Url="https://imgs.search.brave.com/iNCev3rfZtMKcRfPEcLojS4iw7uE3BhN-07s29CJlrs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJjYXZlLmNv/bS93cC93cDQyNTQ4/ODAuanBn"
    r=requests.get(Url)
    open("image3.jpg","wb").write(r.content)
    # await asyncio.sleep(4)
    
    return 'Bob3'

async def main():
    # task=asyncio.create_task(func1())
    await func1()
    await func2()
    await func3()

    # L=await asyncio.gather(func1(),
    #                     func2(),
    #                     func3()
    #                     )
    # print(L)

asyncio.run(main())