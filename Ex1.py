# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from random import randint

n = int(input('Enter the quantity of numbers in list: '))
# list = []
# for i in range(n):
#     list.append(randint(-10, 10))
# print(list)
# print()

# result_list = []
# for i in range((len(list) + 1)// 2):
#     result_list.append(list[i] * list[-i-1])
# print(f'The multi of pairs of numbers (example: the first * the last) is: \n{result_list}')

list = [randint(-10, 10) for i in range(n)]
print(list)
print()
result_list = [list[i] * list[-i-1] for i in range((len(list) + 1)// 2)]
print(result_list)