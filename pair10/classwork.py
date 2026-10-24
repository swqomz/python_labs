class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return self.name

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
    def info(self):
        return f'{self.name}, {self.group}'

class Teacher:
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        return f'{self.name}, {self.subject}'

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
    def add_student(self, student):
        self.students.append(student)



people = [Person('John'), Student('Arthur', '10It'), Teacher('Sadie', 'Math'), Student('Abigail', '10It') ]

for person in people:
    print(person.info())
student1 = Student('John', '10IT')
person = Person('Arthur')
teacher = Teacher('Sadie', 'Math')
course2 = Course('math', teacher)
student2 = Course('Molly', '10It')
# course = Course('Math', teacher)

for student in course2.students:
    print(student.info())

# print(course.name)
# print(course.teacher.info())
# print(course.students)
# print(student.name)
# print(student.group)
# print(person.info())

# print(person.info())
# print(student.info())
# print(teacher.info())

print(isinstance(student, Student))