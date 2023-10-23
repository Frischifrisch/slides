import asyncio
import aiofiles
import tempfile
import os


async def save_file(filename, size):
    async with aiofiles.open(filename, 'w') as f:
        for _ in range(size):
            data = ''.join('xxxxxxxxxxx' for _ in range(1000))
            await f.write(data)

async def main():
    tempdir = tempfile.mkdtemp()

    tasks = []
    for idx in range(300):
        filename = os.path.join(tempdir, f'{idx}.txt')
        tasks.append(asyncio.create_task(save_file(filename, 10)))
    await asyncio.gather(*tasks)
    #print(os.listdir(tempdir))

asyncio.run(main())
