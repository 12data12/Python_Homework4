#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Enter a natural number: "))
i = 2 
numbers = []
num = number
while i <= number:
    if number % i == 0:
        numbers.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Prime fracs for entered number are {numbers}")