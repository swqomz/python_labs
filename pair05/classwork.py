# def say_hello():
#     print("Hello World")

# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()


# def say_hello(name): 
#     print(f"Hello {name}")
# # name - параметр функції
# # "Ivan" - аргумент
# say_hello("Ivan")
# say_hello('Oleg')


# def rectangle_area(width, height):
#     return  width * height
    

# width = int(input('write width'))
# height = int(input('write height'))

# S = rectangle_area(width, height)

# print(f'Площа дорівнює {S} см2')

# def hello_world(name, message = 'Hello WOrld'):
#     print(f'Hello {name}, your message is {message}')

# hello_world('ivan', 'python')

# def price_with_discount(price, discount = 0):
#     return price - price * discount / 100

# print(price_with_discount(1000, 10))

# def min_max(numbers):
#     return min(numbers), max(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# min_, max_ = min_max(numbers)

# def is_even(num):
#     """повертає тру якщо парне, - інакше - фолс"""
#     return num % 2 == 0

# print(is_even(3))
# print(is_even.__doc__)


# def rectangle_area(width, height):
#     return width * height

# def main():
#     width = float(input('width'))
#     height = float(input('height'))

#     print(f'Width, {width}')
#     print(f'Height, {height}')
#     result = rectangle_area(width, height)
#     print(f'площа прямокутника {result}' )