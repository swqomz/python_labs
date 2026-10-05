#1
# numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
# positive = []
# negative = []
# two = []
# three = []

# for number in numbers:
#     if number > 0:
#         positive.append(number)

#     if number < 0:
#         negative.append(number)

#     if number % 2 == 0:
#         two.append(number)

#     if number % 3 == 0:
#         three.append(number)

# average = sum(numbers) / len(numbers)

# print(f'додатні: {positive}')
# print(f"від'ємні: {negative}")
# print(f'парні: {two}')
# print(f'кратні 3: {three}')
# print(f'Min: {min(numbers)} Max: {max(numbers)} Sum: {sum(numbers)} Average: {average}')

#2

# group1 = {'Anna','Ivan','Olha'}
# group2 = {'Ivan','Maksym','Olha'}

# group3 = group1 & group2
# group4 = group1 | group2
# group5 = group1 - group2
# group6 = group2 - group1


# print(f'спільні: {', '.join(group3)}')
# print(f'тільки group1: {', '.join(group5)}')
# print(f'тільки group2: {', '.join(group6)}')
# print(f'усі: {', '.join(group4)}')

#3

# products = {
#     "milk": 48,
#     "bread": 35,
#     "tea": 75,
#     "coffee": 120,
#     "cheese": 95
# }

# name = input("введіть назву товару: ")
# price = int(input("введіть ціну товару: "))

# products[name] = price

# search_name = input("введіть назву товару для пошуку: ")
# found_price = products.get(search_name)

# if found_price is not None:
#     print(f"{search_name} — {found_price} грн")
# else:
#     print("товар не знайдено")

# min_price = int(input("введіть мінімальну ціну: "))
# max_price = int(input("введіть максимальну ціну: "))

# print(f"товари у діапазоні {min_price}..{max_price} грн:")

# for name, price in products.items():
#     if min_price <= price <= max_price:
#         print(f"{name} — {price} грн")

#4

# students = {
#     'Ivan': [10, 11, 12, 9, 10],
#     'Anna': [8, 9, 10, 11, 9]
# }

# group = ('10-IT', '2026/2027')

# best_name = ""
# best_grade = 0

# print(f"Group: {group[0]}, {group[1]}")

# print("список:")
# for name, marks in students.items():
#     print(f"{name}: {marks}")

# name = input("введіть ім'я нового учня: ")
# marks = input("введіть 5 оцінок через пробіл: ")

# grades = []

# for mark in marks.split():
#     grades.append(int(mark))

# correct = True

# if len(grades) != 5:
#     correct = False
# else:
#     for mark in grades:
#         if mark < 1 or mark > 12:
#             correct = False
#             break

# if correct:
#     students[name] = grades

#     print(f"учень {name} доданий")

#     print("новий список:")
#     for name, marks in students.items():
#         print(f"{name}: {marks}")

#     # Середній бал
#     print("середній бал:")
#     rating = []

#     for name, marks in students.items():
#         average = sum(marks) / len(marks)

#         print(f"{name}: {average}")

#         rating.append((average, name))

#         if average > best_grade:
#             best_grade = average
#             best_name = name

#     rating.sort(reverse=True)

#     print("рейтинг:")
#     for average, name in rating:
#         print(f"{name}: {average}")
#     print(f"найкращий учень: {best_name} — {best_grade}")

# else:
#     print("помилка: потрібно ввести 5 оцінок від 1 до 12")