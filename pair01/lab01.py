#1
#(a)

# a = int(input())

# if a % 2 == 0:
#     print("parne")
# else:
#     print("ne parne")

#(b)

# a = int(input('введіть свій вік'))

# if a >= 18:
#     print('Ви повнолітні!')
# else:
#     print('Ви неповнолітні :(')

#(c)
# r = float(input('Введіть радіус кола'))

# S = 3.14 * r ** 2
# L = 2 * 3.14 * r
# print("Площа кола", S)
# print("Довжина кола", L)

#(d)

# a, b = map(int, input("введіть два числа").split())

# if a > b:
#     print(a)
# elif a < b:
#     print(b)
# else:
#     print("числа рівні")

#2

# x, y = map(int, input("ведіть координати точки: ").split())

# if x > 0 and y > 0:
#     print("перша чверть")
# elif x < 0 and y > 0:
#     print('друга чверть')
# elif x < 0 and y < 0:
#     print("третя чверть")
# elif x > 0 and y < 0:
#     print('четверта чверть')
# else:
#     if x == 0:
#         print('точка лежить на осі x')
#     else:
#         print('точка лежать на осі y')

#3

# age = int(input("введіть вік: "))

# if age in [11, 12, 13, 14]:
#     print(age, "років")
# elif age % 10 == 1:
#     print(age, "рік")
# elif age % 10 in [2, 3, 4]:
#     print(age, "роки")
# else:
#     print(age, "років")