import math
import random
import statistics
from datetime import date

#1

# r = float(input("радіус: "))
# a, b = map(float, input("катети: ").split(","))
# N = int(input("предметів: "))
# K = int(input("в упаковці: "))

# area = math.pi * r ** 2
# hypotenuse = math.sqrt(a ** 2 + b ** 2)
# packages = math.ceil(N / K)

# print(f"площа круга: {area:.2f}")
# print(f"гіпотенуза: {hypotenuse:.2f}")
# print(f"потрібно упаковок: {packages}")

#2
# N = int(input("N = "))

# if N > 0:
#     grades = []

#     for i in range(N):
#         grades.append(random.randint(1, 12))

#     print("оцінки:", grades)
#     print("min:", min(grades))
#     print("max:", max(grades))
#     print("середнє:", statistics.mean(grades))
#     print("медіана:", statistics.median(grades))

#     count = 0
#     for i in range(N):
#         if 10 <= grades[i] <= 12:
#             count += 1

#     print("кількість оцінок 10–12:", count)
# else:
#     print("N повинно бути додатним")

#3

# year = int(input("рік: "))
# month = int(input("місяць: "))
# day = int(input("ден: "))

# event_date = date(year, month, day)
# today = date.today()

# if event_date > today:
#     print("до події залишилося:", (event_date - today).days, "днів")
# elif event_date < today:
#     print("після події минуло:", (today - event_date).days, "днів")
# else:
#     print("подія відбувається сьогодні")

#4

def generate_grades(count):
    grades = []
    for i in range(count):
        grades.append(random.randint(1, 12))
    return grades

def average_grade(grades):
    return statistics.mean(grades)
def get_level(average):
    if average >= 10:
        return "високий"
    elif average >= 7:
        return "достатній"
    elif average >= 4:
        return "середній"
    else:
        return "початковий"
