#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint(-5, 5))
print(f'List of random numbers: {numbers}')
print(f'List of unique numbers: {[i for i in numbers if numbers.count(i) == 1]}')