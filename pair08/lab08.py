

#1

# number1 = int(input('введіть перше число'))
# number2 = int(input('введіть друге число'))
# operation = input('введіть операцію')

# try:
#     if operation == '/':
#         print(number1 / number2)
#     if operation == '+':
#         print(number1 + number2)
#     if operation == '-':
#         print(number1 - number2)
#     if operation == '*':
#         print(number1 * number2)
#     else:
#         raise FileNotFoundError('невідома операція')
# except ValueError:
#     print('введіть два числа')
# except FileNotFoundError as error:
#     print('невідома операція')
# except ZeroDivisionError:
#     print('на нуль ділити не можна')


#2

# def input_grade():
#     while True:
#         try:
#             grade = int(input('введіть оцінку від 1 до 12'))
#             if grade < 1 or grade > 12:
#                 raise TypeError('оцінка має бути в діапазоні від 1 до 12')
#             return grade
#         except TypeError as error:
#             print(error)
#         except ValueError:
#             print('введіть число')

# grades = input_grade()
# print(f'прийнято: {grades}')


#3

# students = [
#     'Isha',
#     'Lenny',
#     'Hannah',
#     'Jackie',
#     'Arthur'
# ]

# subject_grade = {
#     'Math': 10,
#     'History': 9,
#     'IT': 12,
#     'PE': 11,
#     'Biology': 8
# }

# choice = input('оберіть. 1 - учень, 2 - оцінка')

# if choice == '1':
#     try:
#         index = int(input(f"введіть індекс учня (від 0 до {len(students) - 1}) "))
#     except ValueError:
#         print(f"введіть ціле число")
#     else:
#         try:
#             print(f"Учень: {students[index]}")
#         except IndexError:
#             print(f"нема такого індексу")

# elif choice == "2":
#     subject = input(f"введіть назву предмета ")

#     try:
#         print(f"оцінка з предмета {subject}: {subject_grade[subject]}")
#     except KeyError:
#         print(f"предмету {subject} немає у словнику")

# else:
#     print(f"оберіть 1 або 2")


#4

# correct = []
# skipped = 0

# try:
#     with open('students.txt', 'r', encoding='utf-8') as file:
#         for line_number, line in enumerate(file, start=1):
#             parts = line.strip().split(';')

#             if len(parts) != 2:
#                 print(f'рядок {line_number} пропущено: неправильна структура')
#                 skipped += 1
#                 continue

#             name = parts[0].strip()
#             grade_text = parts[1].strip()

#             try:
#                 grade = int(grade_text)
#             except ValueError:
#                 print(f'рядок {line_number} пропущено: бал не є числом')
#                 skipped += 1
#                 continue

#             if grade < 0 or grade > 100:
#                 print(f'рядок {line_number} пропущено: бал поза діапазоном')
#                 skipped += 1
#                 continue

#             correct.append((name, grade))

# except FileNotFoundError:
#     print('файл students.txt не знайдено.')

# else:
#     correct.sort(key=lambda student: student[1], reverse=True)

#     with open('report.txt', 'w', encoding='utf-8') as file:
#         for name, grade in correct:
#             file.write(f'{name};{grade}\n')

#     print(f'правильних записів: {len(correct)}')
#     print(f'пропущено: {skipped}')
#     print('створено report.txt')
