
# queue :  １つの処理でコルーチンに値をいれ、他の処理でその値が入るのを待つ

import asyncio

loop = asyncio.get_event_loop()


async def worker1(queue):
    print('worker1 start')
    await queue.put(100) # 値をqueueに入れる. awaitを入れないと、コルーチンに値が入らないので、いつまでもgetで待ちつける　
    print('worker1 end')


async def worker2(queue):
    print('worker2 start')
    x = await queue.get() # 値がqueueに入るのをここで待っている
    print(x)
    print('worker2 end')


queue = asyncio.Queue()
loop.run_until_complete(asyncio.wait([
    worker2(queue), worker1(queue)
]))

loop.close()