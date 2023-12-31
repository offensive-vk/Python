# Delay in Asynchronous Code:
import asyncio

async def my_coroutine():
    print("Start")
    await asyncio.sleep(3)  # Pause the coroutine for 3 seconds
    print("End")

asyncio.run(my_coroutine())

# Throttling Requests:

async def fetch_data(url):
    print(f"Fetching data from {url}")
    await asyncio.sleep(1)  # Throttle requests with a 1-second delay

async def main():
    urls = ["url1", "url2", "url3"]
    tasks = [fetch_data(url) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())

# asyncio.sleep() is used to enforce a rate limit on processing data,
# ensuring that only one task is processed every 2 seconds.

async def process_data(data):
    print(f"Processing data: {data}")
    await asyncio.sleep(2)  # Limit processing to one task every 2 seconds

async def main():
    data_list = ["data1", "data2", "data3"]
    for data in data_list:
        await process_data(data)

asyncio.run(main())
