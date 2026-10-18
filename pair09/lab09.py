#1

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimetr(self):
#         return 2 * (self.width + self.height)

#     def info(self):
#         print(f"{self.width} × {self.height}: площа = {self.area()}, периметр = {self.perimetr()}")

# rec1 = Rectangle(5, 3)
# rec2 = Rectangle(10, 4)

# rec1.info()
# rec2.info()

#2

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []

#     def add_grade(self, grade):
#         if grade >= 1 and grade <= 12:
#             self.grades.append(grade)

#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)

#     def __str__(self):
#         return f"{self.name}: {self.grades}, середній бал = {self.average():.2f}"

# student = Student("Arthur Morgan")

# student.add_grade(10)
# student.add_grade(12)
# student.add_grade(15) 
# student.add_grade(9)

# print(student)

#3


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []

#     def add_grade(self, grade):
#         if grade >= 1 and grade <= 12:
#             self.grades.append(grade)

#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)

#     def __str__(self):
#         return f"{self.name} — {self.average():.2f}"

# students = [
#     Student("Molly"),
#     Student("Hosea"),
#     Student("Kitty"),
#     Student("Elio"),
#     Student("Lain")
# ]

# students[0].add_grade(10)
# students[0].add_grade(11)
# students[0].add_grade(11)

# students[1].add_grade(9)
# students[1].add_grade(10)

# students[2].add_grade(11)
# students[2].add_grade(12)
# students[2].add_grade(11)

# students[3].add_grade(8)
# students[3].add_grade(9)
# students[3].add_grade(10)

# students[4].add_grade(10)
# students[4].add_grade(11)
# students[4].add_grade(10)

# for student in students:
#     print(student)
# best_average = max(student.average() for student in students)

# for student in students:
#     if student.average() == best_average:
#         print(f"найкращий результат: {student.name} — {student.average():.2f}")

#4

# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("сума поповнення має бути більшою за 0")
#         else:
#             self.balance += amount

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("сума зняття має бути більшою за 0")
#         elif amount > self.balance:
#             print(f"недостатньо коштів для -{amount}")
#         else:
#             self.balance -= amount

#     def info(self):
#         print(f"{self.owner}: баланс {self.balance}")

# account1 = Wallet("Joe", 1000)
# account2 = Wallet("Love", 700)

# account1.deposit(500)
# account1.withdraw(300)
# account1.withdraw(2000)

# account2.withdraw(200)
# account2.deposit(100)

# account1.info()
# account2.info()
