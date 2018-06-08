# 非同期でロックを取る asyncio.Lock

import asyncio

loop = asyncio.get_event_loop()

# ロックを先に取得したほうが先にsleepに入る
async def worker1(lock):
    print('worker1 start')
    with await lock: # コルーチンのlockを呼び出すには、awaitを使う
        print('workder1 got lock')
        await asyncio.sleep(3)
    print('workder1 end')


async def worker2(lock):
    print('worker2 start')
    with await lock:
        print('workder1 got lock')
        await asyncio.sleep(3)
    print('workder2 end')


lock = asyncio.Lock()
loop.run_until_complete(asyncio.wait([
    worker1(lock), worker2(lock)
]))

loop.close()


# 参考：デコレータを使った古いやり方 Python version <= 3.5
@asyncio.coroutine
def worker_old(lock):
    with (yield from lock):
        yield from asyncio.sleep(3)