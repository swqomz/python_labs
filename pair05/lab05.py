#1
# def circle_area(radius):
#     return 3.14159 * radius ** 2

# def rectangle_area(width, height):
#     return width * height

# def triangle_area(side, height2):
#     return 0.5 * side * height2

# def main():
#     print("оеріть фігуру:")
#     print("1 -коло")
#     print("2 - прямокутник")
#     print("3 - трикутник")

#     choise = int(input("фігура: "))

#     if choise == 1:
#         radius = float(input(" введіть радіус: "))
#         print(f'radius: {radius}')
#         result1 = circle_area(radius)
#         print(f"площа кола: {result1}")

#     if choise == 2:
#         width = float(input('введіть ширину:'))
#         height = float(input('введіть висоту:'))
#         print(f'ширина {width}')
#         print(f'висота {height}')
#         result2 = rectangle_area(width, height)
#         print(f'площа прямокутника {result2}' )

#     if choise == 3:
#         side = float(input("введіть сторону: "))
#         height2 = float(input("введіть висоту: "))
#         print(f'side, {side}')
#         print(f'height, {height2}')  
#         result3 = triangle_area(side, height2)    
#         print(f'площа трикутника: {result3}')  

# main()

#2

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def divisors(n):
#     result = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             result.append(i)
#     return result

# def digit_sum(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total

# def main():
#     n = int(input("введіть натуральне число "))
#     if is_prime(n):
#         print("просте число: так")
#     else:
#         print("просте число: ні")
#     print(f"дільники: {divisors(n)}")
#     print(f"сума цифр: {digit_sum(n)}")

# main()

# def check_length(password):
#     return len(password) >= 8

# def check_digit(password):
#     for char in password:
#         if char.isdigit():
#             return True
#     return False

# def check_upper(password):
#     for char in password:
#         if char.isupper():
#             return True
#     return False

# def check_lower(password):
#     for char in password:
#         if char.islower():
#             return True
#     return False

# def check_special(password):
#     for char in password:
#         if not char.isalnum():
#             return True
#     return False

# def validate_password(password):
#     errors = []

#     if not check_length(password):
#         errors.append("пароль має містити мінімум 8 символів")
#     if not check_digit(password):
#         errors.append("немає цифри")
#     if not check_upper(password):
#         errors.append("немає великої літери")
#     if not check_lower(password):
#         errors.append("немає малої літери")
#     if not check_special(password):
#         errors.append("немає спеціального символу")
#     return len(errors) == 0, errors

# def main():
#     password = input("Введіть пароль: ")
#     valid, errors = validate_password(password)
#     if valid:
#         print(f"пароль надійний.")
#     else:
#         print(f"пароль не відповідає вимогам.")
#         print(f"не виконано: {', '.join(errors)}")

# main()

