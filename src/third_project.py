"""Даны два списка чисел. Посчитайте, сколько различных чисел содержится

одновременно как в первом списке, так и во втором.

"""

first_list = [1, 6, 4, 7, 3, 84, 2, 2, 654, 2, 67, 42]
second_list = [5, 3, 2, 1, 6, 3, 73, 32, 63]
result = set(first_list).symmetric_difference(second_list)
print(len(result))
