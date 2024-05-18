import asyncio
from random import shuffle


async def bogosort(data: list[int]):
    attempt = 1
    while not sorted(data) == data:
        attempt += 1
        shuffle(data)
    print('Попыток', attempt)
    print(data)


async def print_string(string):
    print(string)


async def main():
    a = [8, 6, 1, 9, 3, 7, 2, 5, 4]
    my_string = 'Строчка, которая гуляет сама по себе'
    await asyncio.gather(bogosort(a), print_string(my_string))
    # tasks = [asyncio.ensure_future(bogosort(a)), asyncio.ensure_future(print_string(my_string))]
    # await asyncio.wait(tasks)
    # await asyncio.wait([bogosort(a), print_string(my_string)], return_when=asyncio.FIRST_COMPLETED)
    # task1 = asyncio.create_task(bogosort(a))
    # task2 = asyncio.create_task(print_string(my_string))
    # await task1
    # await task2
    # await bogosort(a)
    # await print_string(my_string)


if __name__ == '__main__':
    asyncio.run(main())
