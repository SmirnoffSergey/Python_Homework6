# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.

from random import randint

n = int(input('Enter the quantity of numbers in list: '))
# list = []
# for i in range(n):
#     list.append(randint(-10, 10))
# print(list)
# print()
# print(f'The sum of the list items standing in an odd position is equal to {sum(list[1::2])}')


list = [randint(-10, 10) for i in range(n)]
print(list)
print(f'The sum of the list items standing in an odd position is equal to {sum(list[1::2])}')