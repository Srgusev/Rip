# Необходимо реализовать генератор gen_random(количество, минимум, максимум), который последовательно выдает заданное количество случайных чисел в заданном диапазоне от минимума до максимума, включая границы диапазона. 

import random


def gen_random(num_count: int, begin: int, end: int) -> iter:
    #Генерирует num_count случайных чисел от begin до end, включая их.

    for i in range(num_count):
        yield random.randint(begin, end)


if __name__ == '__main__':
    print(str(list(gen_random(5, 1, 3)))[1:-1])