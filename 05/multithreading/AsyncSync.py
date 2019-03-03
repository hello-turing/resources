import time 
import asyncio
from threading import Thread

async def do_some_work(x):
	print("Waiting " + str(x))
	await asyncio.sleep(x)

loop = asyncio.get_event_loop()
# 1
#loop.run_until_complete(do_some_work(5))


# 2
tasks = [asyncio.ensure_future(do_some_work(2)), 
			asyncio.ensure_future(do_some_work(5)),
			asyncio.ensure_future(do_some_work(4)),
			asyncio.ensure_future(do_some_work(3))]
loop.run_until_complete(asyncio.gather(*tasks))

