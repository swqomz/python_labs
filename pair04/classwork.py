#list - список - впорядкована змінна колекція
# grades = [10, 8, 9]
# numbers =[]
# numbers_new = list()

# grades[1] = 12


# numbers.append(10)
# numbers.append([11,4]) #додавання одного елементу
# numbers.insert(1, [5,6]) #вставка за індексом
# numbers.extend([7, 8 ,9, 7, 8, 6, 8]) #додавання декількох об'єктів
# numbers.remove(7) #видалення за значенням
# numbers.pop(1) #видалення за індексом
# # del numbers[1] видаляє повністю
# # numbers.clear() очищає список
# print(numbers.count(8)) #рахує кількість
# print(numbers.index(8)) #рахує індекс першого елементу

# print(8 in numbers)

# # len()
# # min()
# # max()
# # sum()


# numbers = [1, 4, 6, 8, 3]
# numbers.sort()
# # numbers.sort(reverse = True)
# print(numbers)

# new_numbers = sorted(numbers)
# new_numbers.reverse()
# print(new_numbers)


# for number in numbers:
#     print(number)

# numbers = [1, -9, 5, -4, 34, 5, 8 ,-3]
# positive =[]
# for number in numbers:
#     if number > 0:
#         positive.append(number)
# print(positive)



#tuple - кортежі - впорядкована незмінна колекція
# point = (-10, 12)
# rgb = (255, 0, 0)
# data = ()
# student = "Ivan", "Komarov"
# a = (10, )

# point = point + (30,)
# print(point)
# # print(point + a)
# point = point[:1] + point[2:]
# print(point)
# point = (12, 6)
# x, y = point
# print(x)
# print(y)


#set - множини - немає дублікатів, немає індексного доступу, на порядок елементів не звертаємо уваги
# subjects = {'Python', "HTML", "CSS", "JavaScript"}
# data = {}
# print(type(data))
# subjects.add("C++")
# subjects.update("Java", "Python")
# print(subjects)
# subjects.remove("Java")
# subjects.discard("C#")
# if "Python" in subjects:
#     print("Python")

# name = ["Ivan", "Oleg", "Olha", "Ivan", "Maria", "Maria"]
# unique_names = set(name)
# print(unique_names)

# group1 = {"Ivan", "Oleg", "Olha"}
# group2 = {"Ivan", "Maria", "Anna"}

# group3 = group1 & group2 #перетин спільні
# group4 = group1 | group2 #об'днання унікальні
# group5 = group1 - group2 #є в 1, відсутні в 2
# print(group3)
# print(group4)
# print(group5)




#dict - словиники
# student = {
#     "name": 'Ivan',
#     'grade': 11
# }

# student2 = {}
# student3 = dict()
# print(student["name"])
# student["age"] = 18
# print(student)
# student["age"] = 19
# print(student)
# student_update = student.pop("age")
# print(student_update)
# popitem = student.popitem() #видаляє останню пару значень
# # clear очищає повністю



# student = {
#     "name": 'Ivan',
#     'grade': 11
# }

# print(student.get("age", "Такого немає"))
# if "grade" in student:
#     print(student.get("grade"))

# if 'Ivan' in student.values(): #За значенням
#     print(student.get("name"))

# if 'Ivan' in student.keys(): #За ключем
#     print(student.get("name"))

# if 'Ivan' in student.items(): 
#     print(student.get('name'))

# print(student.items())

# for key, value in student.items():
#     print(key)
#     print(value)


prices = {
    'apple': 45,
    'banana': 70,
    'kiwi': 70,
    'mango': 150,
    'orange': 100
}

print("Усі товари:")
for name, price in prices.items():
    print(f'{name}: {price}грн')

print("від 50 до 100 грн")
for name, price in prices.items():
    if price > 50 and price <= 100:
        print(f'{name}: {price}грн')