# 非同期で他のコルーチンから通知を受け取るまで待機する asyncio.condition

import asyncio

loop = asyncio.get_event_loop()


async def worker1(condition):
    with await condition: # コルーチンのconditionを呼び出すには、awaitを使う
        print('worker1 start')
        await condition.wait() # notifyを受け取るか、Timeoutするまでここで待つ. wait_for()
        print('workder1 got condition')
        await asyncio.sleep(3)
        print('workder1 end')


async def worker2(condition):
    with await condition:
        print('worker2 start')
        await condition.wait()
        print('workder2 got condition')
        await asyncio.sleep(3)
        print('workder2 end')

async def worker3(condition):
    with await condition:
        print('worker3 start')
        await asyncio.sleep(3)
        print('worker3 send notify_all')
        condition.notify_all() # 通知を送る
        print('worker3 end')

condition = asyncio.Condition()
loop.run_until_complete(asyncio.wait([
    worker1(condition), worker2(condition), worker3(condition)
]))

loop.close()