# ДЗ


# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2
# from random import randint

# n = int(input("Введите количество монет: "))

# numbers = []

# for i in range(n):
#     number = randint(0, 1)
#     numbers.append(number)

# print(numbers)

# count1 = 0
# count2 = 0

# for i in numbers:
#     if i == 1:
#         count1 += 1
#     elif i == 0:
#         count2 += 1

# if count1 > count2:
#     print(F"Нужно перевернуть минимум {count2} монеток")
# else:
#     print(F"Нужно перевернуть минимум {count1} монеток")


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3



# S = int(input("Введите сумму чисел S: "))
# P = int(input("Введите произведение чисел P: "))
# X = 1
# Y = S - X
# while X <= 1000 and Y <= 1000:
#     if X * Y == P:
#         print("Задуманные числа: X =", X, "и Y =", Y)
#         break
#     X += 1
#     Y = S - X



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N

# 10 -> 1 2 4 8

# n = int(input("Введите степень: "))

# numbers=[]

# for i in range(n):
#     number = 2**i
#     numbers.append(number)
# print(numbers)

# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1
