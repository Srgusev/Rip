# Дан массив 1, содержащий положительные и отрицательные числа. Необходимо одной строкой кода вывести на экран массив 2, которые содержит значения массива 1, отсортированные по модулю в порядке убывания. Сортировку необходимо осуществлять с помощью функции sorted. 

data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data, key=abs, reverse=True)
    print('Без использования lambda-функции: ', result)
    result_with_lambda = sorted(data, key = lambda x: x if x >= 0 else -x, reverse=True)
    print('С использованием lambda-функции: ', result_with_lambda)