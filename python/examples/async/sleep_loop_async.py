import time
import asyncio

async def sleep(cnt, sec):
    print(f"Start {cnt}")
    await asyncio.sleep(sec)
    print(f"End {cnt}")

async def main():
    co_routines = [sleep(i, 1) for i in range(4)]
    for t in co_routines:
        await t

start = time.monotonic()
asyncio.run(main())
end = time.monotonic()
print(f"Elapsed {end-start}")
