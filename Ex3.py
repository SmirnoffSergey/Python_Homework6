# Задайте последовательность цифр. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.


from random import randint

n = int(input('Enter the quantity of numbers in list: '))
# list = []
# for i in range(n):
#     list.append(randint(-5, 5))
# print(list)
# print()

# list_result = []
# for i in range(len(list)):
#     count = 0
#     for j in range(len(list)):
#         if list[i] == list[j]:
#             count += 1
#     if count == 1:
#         list_result.append(list[i])
# print(list_result)

list_result = [randint(-5, 5) for i in range(n)]
print(list_result)
print(list(filter(lambda x: list_result.count(x) == 1, list_result)))