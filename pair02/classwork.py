# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# ітерація - одне виконання тіла циклу

# for i in range(1, 6, 2):
#     print(i)

# for i in range(10, 0 , -1):
#     print(i)

# n = int(input())
# for i in range(1, n + 1):
#     print(i)

# n = int(input())

# i = 1

# while i <= n:
#     print(i)
#     i += 1 #i = i + 1 інкремент 

# n = int(input())

# suma = 0 

# for i in range(1, n + 1):
#     suma += i

# print (f'Сума = {suma}')

# n = int(input())
# count = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         count += 1

# print(f"Парні {count}")


# while True:
#     n = int(input('''введіть число або число "0"'''))
#     if n == 0:
#         break

#     print(f"введено число {n}")

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)



# digit_last = n % 10 
# digit_first = n % 100
# if digit_last == digit_first:
#     print("ok")

# while n > 0:
#     digit = n % 10
#     print(f'last number {digit}')
#     # n = n // 10
#     n //= 10

# n = 1234
# max_digit = 0
# while n > 0:
#     digit = n % 10
#     if digit > max_digit:
#         max_digit = digit
#     n //= 10
# print(max_digit)

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, j)

# width = 6
# height = 4

# for row in range(height):
#     for col in range(width):
#         print('*', end='')
#     print()

# print(1, end='\n')
# print(2)
# print(3)