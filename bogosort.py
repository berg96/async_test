import asyncio
import threading
from random import shuffle


def bogosort(data: list[int]):
    attempt = 1
    while not sorted(data) == data:
        # print('Попытка #', attempt)
        attempt += 1
        shuffle(data)
    print('Попытка #', attempt)
    print(data)


def print_string(string):
    print(string)


if __name__ == '__main__':
    a = [8, 6, 1, 9, 3, 7, 2, 5, 4]
    t1 = threading.Thread(target=bogosort, args=(a,))
    t2 = threading.Thread(target=print_string, args=('Строчка, которая гуляет сама по себе',))

    # Тут запускаются дочерние потоки.
    t1.start()
    t2.start()

    # Пока дочерние потоки не закончат работу, не продолжат
    # выполняться инструкции из основного потока.
    t1.join()
    t2.join()
