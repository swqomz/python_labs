# book ={
#     'title': 'Кобзар',
#     'author': 'Тарас Шевченко',
#     'copies': 15
# }

# print(book)

# class Book:
#     def __init__(self, title, author,copies):
#         self.title = title
#         self.author = author
#         self.copies = copies
#     def available(self):
#         return self.copies > 0


# book1 = Book('Кобзар', 'Тарас Шевченко', 15)
# # book2 = Book()

# print(book1.title, book1.author, book1.copies)
# print(book1.available())
# # print(book2)


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimetr(self):
#         return 2 *(self.width + self.height)

#     def info(self):
#         print(f'rec width {self.width} height {self.height}')
#         print(f'perimetr {self.perimetr}')
#         print(f'area {self.area()}')


# rec = Rectangle(100 ,200)
# rec.info()
# area = rec.area()
# print(area)
# print(area > 10000)


# class Counter:
#     def __init__(self):
#         self.value = 0

#     def increment(self):
#         self.value += 1

# counter1 = Counter()
# counter2 = Counter()
# print(f'було {counter1.value, counter2.value}')

# counter1.increment()
# counter2.increment()
# print(f'стало {counter1.value, counter2.value}')


# class Book:
#     def __init__(self, title, copies):
#         self.title = title
#         self.copies = copies

#     def give_one(self):
#         if self.copies > 0:
#             self.copies -= 1
#             print(f'видано книгу {self.title}')
#         else:
#             print(f'нема доступгих примірників {self.title}')


# book = Book('Кобзар', 1)
# book.give_one()
# book.give_one()
# print(f'remain {book.copies}')


# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def add_grade(self, grade):
#         if grade >= 1 and grade <= 12:
#             self.grades.append(grade)
#         else:
#             print('grade must be 1..12')
#     def average_grade(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
#     def info(self):
#         print(f'name {self.name}, grades {self.grades}')
#     def __str__(self):
#         return f'student {self.name}, grades {self.grades}, aerage {self.average_grade()}'

# student1 = Student("Ivan")
# student2 = Student("Anna")
# student1.add_grade(12)
# student2.add_grade(1)

# print(f'Ivan: {student1.grades}, Anna: {student2.grades}')
# print(f'average {student1.average_grade()}')


# students = {
#     Student('Anna', [1, 2, 3]),
#     Student('Ivan', [12,10, 11])
# }

# print(f'students: {len(students)}')
# for student in students:
#     print(f'student {student.name}, grades {student.grades}')

class Product:
    def __init__(self,name, price, count):
        self.name = name
        self.price = price
        self.count = count
    def total_price(self):
        return self.price * self.count

mouse = Product("mouse", 1500, 10)
keyboard = Product("keyboard", 1800, 4)

print(mouse.total_price())
print(keyboard.total_price())