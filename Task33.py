#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int(input("Enter a natural degree k "))

def write_file(st):
    with open('Task33.txt', 'w') as data:
        data.write(st)
def rnd():
    return random.randint(0,101)
def create_mn(k):
    numbers = [rnd() for i in range(k+1)]
    return numbers 
def create_str(sp):
    numbers= sp[::-1]
    wr = ''
    if len(numbers) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(numbers)):
            if i != len(numbers) - 1 and numbers[i] != 0 and i != len(numbers) - 2:
                wr += f'{numbers[i]}x^{len(numbers)-i-1}'
                if numbers[i+1] != 0:
                    wr += ' + '
            elif i == len(numbers) - 2 and numbers[i] != 0:
                wr += f'{numbers[i]}x'
                if numbers[i+1] != 0:
                    wr += ' + '
            elif i == len(numbers) - 1 and numbers[i] != 0:
                wr += f'{numbers[i]} = 0'
            elif i == len(numbers) - 1 and numbers[i] == 0:
                wr += ' = 0'
    return wr

coef = create_mn(k)
write_file(create_str(coef))