# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3]
# summa = 0
# for i in range(1, len(list), 2):
#     summa += int(list[i])
# print(f'{list} -> ответ: {summa} ')

# Напишите программу, которая найдёт 
# произведение пар чисел списка.
#  Парой считаем первый и последний элемент, 
#  второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list = input ('Enter 4 or 5 numbers:').split()
# newlist = []
# for i in range(0, (len(list) - 1) // 2+1):
#     newlist.append(int(list[i]) * int(list[len(list) - i - 1]))
# print(f'{list} => {newlist}')

# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = input('Задайте список из вещественных чисел:').split()
# maxx = 0
# minn = 1
# for el in list:
#     if '.' in el:
#         number = el.split('.')[1]
#         if int(number) != 0:
#             if float('0.' + number) < minn:
#                 minn = float('0.' + number)
#             elif float('0.' + number) > maxx:
#                 maxx = float('0.' + number)
# print (f'{list} => {maxx - minn}')

# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Enter numbe:'))
number2 = ''
while number > 0:
    number2 = str(number % 2) + number2
    number //= 2
print (f'{number} -> {number2}')