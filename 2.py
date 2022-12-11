# Д/З 2 Pyhton

# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

# def sum (num):
#     sum = 0
#     for i in num:
#         if i != '.':
#             sum = sum + int(i)
#     return sum
# num = input('Введите вещественное число: ')
# print (sum(num))

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def factorial(n):
#     count = 1
#     for i in range (1, n + 1):
#         count *= i
#         print(count)
# n = int(input('Введите число n: '))
# factorial(n)

# 3.Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

# def in_list(n):
#     list = []
#     for i in range (1, n + 1):
#         list.append((1 + 1/i) ** i)
#     return list
# def sum(list):
#     sum=0
#     for i in range (len(list)):
#         sum=sum + list[i]
#     return sum
# n = int(input('Введите число n: '))
# list = in_list(n)
# print(list)
# result = sum(list)
# print('%.2f' % result)

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

# from random import randint
# num = []
# for i in range(7):
#     num.append(randint (-10,10))
# print(num)
# def get_num(num):
#     count = 0 
#     for element in num:
#         count += 1
#     return count
# print('Number of elements: ', get_num(num))

# x = int(input('введите позицию первого элемента: '))
# y = int(input('введите позицию второго элемента: '))
# z = int(input('введите позицию третьего элемента: '))
# for i in range(len(num)):
#     mult = num[x -1] * num[y - 1] * num[z - 1]
# print(f'Mult of elements: {num[x - 1]} * {num[y - 1]} * {num [z - 1]} =', mult)

# 5. Реализуйте алгоритм перемешивания списка.

# from random import Random, randint
# n = int(input('Введите число '))
# num = []
# for i in range(n):
#     num.append(randint(-n, n + 1))
# print(num)
# def smes(num):
#     list = num[:]
#     num_length = len(list)
#     for i in range(num_length):
#         index = randint(0, num_length - 1)
#         temp = list[i]
#         list[i] = list[index]
#         list[index] = temp
#     return list
# print(smes(num))