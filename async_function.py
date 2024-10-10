import asyncio
import time

async def func1():
    print(f"started at func1  {time.strftime('%X')}")
    await asyncio.sleep(3)
    print(f"finished at func1 {time.strftime('%X')}")
    print("func1")
    
async def func2():
    print(f"started at func2  {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"finished at func2 {time.strftime('%X')}")
    print("func2")
    
async def func3():
    print(f"started at func3 {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"finished at func3  {time.strftime('%X')}")
    print("func3")
        
async def main():
    print(f"started at {time.strftime('%X')}")
    task = asyncio.create_task(func2())
    await func1()
    #await func2()
    await func3()
    print(f"finished at {time.strftime('%X')}")
    
asyncio.run(main())