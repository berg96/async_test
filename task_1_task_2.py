import threading
from time import sleep


def task_1():
    print('Поток 1 начал работу')
    a = 2
    b = 3
    result = a + b
    print(result)
    # Вот они — дополнительные инструкции для первого потока.
    for i in range(1, 4):
        print(f'Инструкция {i} из потока 1')
        sleep(1)

    print('Поток 1 завершил работу')


def task_2():
    print('Поток 2 начал работу')
    text = 'Строчка, которая гуляет сама по себе'
    print(text)
    # Дополнительные инструкции для второго потока.
    for i in range(1, 4):
        print(f'Инструкция {i} из потока 2')
        sleep(1)

    print('Поток 2 завершил работу')


# Основной поток.
if __name__ == '__main__':
    print('Начало работы основного потока')

    t1 = threading.Thread(target=task_1)
    t2 = threading.Thread(target=task_2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Окончание работы основного потока')
