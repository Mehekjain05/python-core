# multi-threading creates multiple threads
# whereas async utilize the single thread fully.

import asyncio
import time

async def main():  #this is a coroutine
    print("Hello")
    await asyncio.sleep(3) # this wont block the resource
    print("World")

#main()
asyncio.run(main())