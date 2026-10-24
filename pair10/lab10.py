#1

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"ім'я: {self.name}"

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def info(self):
        return f"ім'я: {self.name}, група: {self.group}"

#2
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def info(self):
        return f"викладач: {self.name}, предмет: {self.subject}"

#3
class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.name == student.name:
                print("Такий студент уже є")
                return

        self.students.append(student)

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return

    def show_students(self):
        print(f"курс: {self.title}")
        print(f"{self.teacher.info()}")
        print("студенти:")
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student.info()}")



#1
student1 = Student('Лара', '10IT')
student2 = Student('Боб', '10IT')

print(student1.info())
print(student2.info())

#2
people = [
    Person("Sadie Adler"),
    Student("Arthur Morgan", "IT-10"),
    Student("John Marston", "IT-11"),
    Teacher("Dutch van der Linde", "Python")
]

for person in people:
    print(person.info())


#3
teacher = Teacher("Ivan Komarov", "Python")

student1 = Student("Clay Jansen", "IT-10")
student2 = Student("Jessica Davis", "IT-10")
student3 = Student("Justin Foley", "IT-11")
student4 = Student("Tony Padilla", "IT-11")

course = Course("Python", teacher)

course.add_student(student1)
course.add_student(student2)
course.add_student(student3)
course.add_student(student4)

course.remove_student("Tony Padilla")

course.show_students()

#4

# Завдання 4

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Ім'я: {self.name}"


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
        self.grades = []

    def info(self):
        return f"учень: {self.name}, група: {self.group}"

    def add_grade(self, grade):
        if 1 <= grade <= 12:
            self.grades.append(grade)
            print("оцінку додано")
        else:
            print("неправильна оцінка")

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def info(self):
        return f"викладач: {self.name}, предмет: {self.subject}"


class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        if not student.name or not student.group:
            print("ім'я і група не можуть бути порожніми")
            return

        if self.find_student(student.name) is not None:
            print("такий студент уже існує")
            return

        self.students.append(student)
        print("студента додано")

    def remove_student(self, name):
        student = self.find_student(name)

        if student is not None:
            self.students.remove(student)
            print("студента видалено")
        else:
            print("студента не знайдено")

    def show_students(self):
        print(f"\nкурс: {self.title}")
        print(self.teacher.info())
        print("студенти:")

        if len(self.students) == 0:
            print("студентів немає")

        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student.info()}")

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def add_grade_to_student(self, name, grade):
        student = self.find_student(name)

        if student is not None:
            student.add_grade(grade)
        else:
            print("студента не знайдено")

    def show_rating(self):
        rating = sorted(
            self.students,
            key=lambda student: student.average(),
            reverse=True
        )

        print("\nРейтинг:")

        if len(rating) == 0:
            print("студентів немає")

        for i, student in enumerate(rating, 1):
            print(f"{i}. {student.name} — {student.average():.2f}")

    def save_data(self):
        try:
            with open("course_data.txt", "w", encoding="utf-8") as file:
                for student in self.students:
                    grades = ",".join(str(grade) for grade in student.grades)
                    print(f"{student.name};{student.group};{grades}", file=file)

            print("Дані збережено")

        except OSError as error:
            print(f"помилка: {error}")

    def load_data(self):
        try:
            loaded_students = []

            with open("course_data.txt", "r", encoding="utf-8") as file:
                for line in file:
                    name, group, grades_text = line.strip().split(";")

                    if not name or not group:
                        raise ValueError("неправильні дані студента")

                    for s in loaded_students:
                        if s.name.lower() == name.lower():
                            raise ValueError("повторюється ПІБ")

                    student = Student(name, group)

                    if grades_text:
                        for grade in grades_text.split(","):
                            number = int(grade)

                            if not 1 <= number <= 12:
                                raise ValueError("неправильна оцінка у файлі")

                            student.grades.append(number)

                    loaded_students.append(student)

            self.students = loaded_students
            print("джані відновлено")

        except FileNotFoundError:
            print("файл відсутній, список студентів порожній")

        except (ValueError, OSError, UnicodeError) as error:
            print(f"помилка: {error}")


teacher = Teacher("Sadie Adler", "Python")
course = Course("Python", teacher)

course.load_data()


while True:
    print("\n меню")
    print("1 - показати курс")
    print("2 - додати студента")
    print("3 - видалити студента")
    print("4 - знайти студента")
    print("5 - виставити оцінку")
    print("6 - показати рейтинг")
    print("7 - зберегти дані")
    print("0 - вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        course.show_students()

    elif choice == "2":
        name = input("ПІБ: ").strip()
        group = input("група: ").strip()
        course.add_student(Student(name, group))

    elif choice == "3":
        name = input("ПІБ: ").strip()
        course.remove_student(name)

    elif choice == "4":
        name = input("ПІБ: ").strip()
        student = course.find_student(name)

        if student is not None:
            print(student.info())
            print(f"оцінки: {student.grades}")
            print(f"середній бал: {student.average():.2f}")
        else:
            print("студента не знайдено")

    elif choice == "5":
        name = input("ПІБ: ").strip()

        try:
            grade = int(input("Оцінка: "))
            course.add_grade_to_student(name, grade)

        except ValueError:
            print("введіть правильну оцінку")

    elif choice == "6":
        course.show_rating()

    elif choice == "7":
        course.save_data()

    elif choice == "0":
        print("завершення ")
        break

    else:
        print("неправильний пункт меню")
