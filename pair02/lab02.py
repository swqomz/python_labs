#1 

# N = int(input("Введіть N: "))

# suma = 0
# count = 0

# for i in range(1, N + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         suma += i
#         count += 1

# if count > 0:
#     average = suma / count
#     print("сума:", suma)
#     print("кількість:", count)
#     print("середнє арифметичне:", average)
# else:
#     print("таких чисел немає")

#2
# N = int(input("введіть число"))

# if N == 0:
#     count = 1
#     total = 0
#     maximum = 0
#     minimum = 0
# else:
#     count = 0
#     total = 0
#     maximum = 0
#     minimum = 9

#     temp = N
#     while temp > 0:
#         digit = temp % 10      
#         total += digit         
#         count += 1            

#         if digit > maximum:
#             maximum = digit
#         if digit < minimum:
#             minimum = digit

#         temp = temp // 10  


# print(f"кількість цифр: {count}")
# print(f"сума цифр: {total}")
# print(f"найбільша цифра: {maximum}")
# print(f"найменша цифра: {minimum}")


#3
# N = int(input("Введіть N: "))

# print("Числа, які діляться на всі свої ненульові цифри:")

# for num in range(1, N + 1):
#     temp = num
#     good = True

#     while temp > 0:
#         digit = temp % 10

#         if digit != 0:
#             if num % digit != 0:
#                 good = False
#                 break

#         temp = temp // 10

#     if good:
#         print(num)

#4

# width = int(input('введіть ширину'))
# height = int(input('введіть висоту'))

# border = input("введіть символ контуру: ")
# inside = input("введіть символ внутрішньої частини: ")

# if width < 3 or height < 3:
#     print("мінімальний розмір рамки — 3 × 3.")
# else:
#     for i in range(height):
#         for j in range(width):
#             if i == 0 or i == height - 1 or j == 0 or j == width - 1:
#                     print(border, end="")
#             else:
#                 print(inside, end="")
#         print()
