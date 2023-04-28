import asyncio
import time


async def add(a,b):
    # time.sleep(1)
    await asyncio.sleep(1)
    return a+b

async def main():
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')
    # c = await add(6,5)
    # print(c)
    # c1 = await add(6,5)
    # print(c1)

    co = [add(6,5),add(46,15),add(61,5589),add(68,15)]
    r = await asyncio.gather(*co)
    print(r)
if __name__ == '__main__':
    asyncio.run(main())