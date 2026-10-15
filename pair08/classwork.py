# if 5 > 2 синтаксична
#     print('yes')

# n = int('hello')

# try:
#     age = int(input('enter your age'))
#     print('you are' + str(age)+ 'years old')
# except ValueError:
#     print('please enter a valid age')

# try:
#     a = float(input('a = '))
#     b = float(input('b = ')) 
#     result = a / b
#     print(result)
# except ValueError:
#     print('enter a number')
# except ZeroDivisionError:
#     print('cant divide by zero')

# try:
#     number = int(input('enter a number'))
# except ValueError:
#     print('enter a number')
# else:
#     print('sqrt ', number ** 2)

# try:
#     number = int(input('enter a number'))
#     print( 100 / number)
# except ValueError:
#     print('')
# except ZeroDivisionError:
#     print('')
# finally:
#     print('bye')

# while True:
#     try:
#         grade = int(input('enter grade 1..12'))
#         if grade < 1 or grade > 12:
#             raise ValueError('grade must be beetwen 1 and 12')
#         print(f'your grade {grade}')
#         break
#     except ValueError as error:
#         print(f'error {error}')

# def int_input(message):
#     while True:
#         try:
#             return int(input(message))
#         except ValueError:
#             ('enter an integer')

# count = int_input('enter a number')
# print('quantity {count}')

# def input_grade():
#     while True:
#         try:
#             grade = int(input('enter grade 1..12'))
#             if grade < 1 or grade > 12:
#                 raise ValueError('grade must be beetwen 1 and 12')
#             return grade
#         except ValueError as error:
#             print(error)

# grade = input_grade()
# print('yes', grade)

# students = ['Anna', 'Ivan', 'Sophie']
# try:
#     index = int(input('enter a number'))
#     print(students[index])
# except ValueError:
#     print('enter a number')
# except IndexError:
#     print('nema tokoho index')

# price = {
#     'apple': 100,
#     'banana': 200,
#     'mango': 300,
# }
# product = input('enter product')
# # try:
# #     print(f'price {price[product]}')
# # except KeyError:
# #     print('nema takoho product')

# price = price.get(product, 'nema y nayavnosti')
# print(price)


# try:
#     with open('data.txt', 'r', 'utf-8') as file:
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print('file not exist')



# line = 'Anna;60'

# parts = line.strip().split(';')
# if len(parts) != 2:
#     print('error')
# else:
#     name = parts[0]
#     grade = parts[1]


#     try:
#         score = int(grade)
#         if score < 0 or score > 100:
#             raise ValueError('score must be 1..100')
#     except ValueError as error:
#         print(error)
#     else:
#         print(f'right {name}: {score}')


lines = [
    'Anna; 90',
    'Ivan; hello',
    'Matvey; 99'
]

for line_number, line in enumerate(lines, start=1):
    parts = line.strip().split(';')
    if len(parts) != 2:
        print(f'row #{line_number}: skipped through incorrect \n{line}')
        continue

    name = parts[0]
    grade = parts[1]
    try:
        grade = int(grade)
    except ValueError:
        print(f'row #{line_number}, skipped: score is not number \n{line}')
        continue

    print('correct input', name, grade)
    