import asyncio

async def fetch_data(id: int, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"Данные из источника {id} получены"


async def main():

    tasks = [
        fetch_data(1, 3.0),
        fetch_data(2, 1.0),
        fetch_data(3, 2.0),
    ]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())