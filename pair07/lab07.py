import os

#1

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

lines = text.splitlines()
words = text.split()

print(f"рядків: {len(lines)}")
print(f"слів: {len(words)}")
print(f"символів: {len(text)}")

if lines:
    longest_line = max(lines, key=len)
    number = lines.index(longest_line) + 1
    print(f"найдовший рядок: №{number}, {len(longest_line)} символів")
    print(f"текст: {longest_line}")


#2

fragment = input(f"введіть фрагмент тексту: ").lower()
found = False

with open("text.txt", "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        if fragment in line.lower():
            print(f"{number}: {line.strip()}")
            found = True

if not found:
    print(f"збігів не знайдено.")


3
students = []

with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, score = line.strip().split(";")
        score = int(score)

        if score > 80:
            students.append([name, score])

students.sort(key=lambda student: student[1], reverse=True)

with open("result.txt", "w", encoding="utf-8") as file:
    for name, score in students:
        print(f"{name};{score}", file=file)
#4

def calculate_average(grades):
    return sum(grades) / len(grades)

students_grades = {}

with open("grades.csv", "r", encoding="utf-8") as file:
    for line in file:
        name, subject, grade = line.strip().split(";")
        grade = float(grade)
        if name not in students_grades:
            students_grades[name] = []
        students_grades[name].append(grade)

results = []
for name, grades in students_grades.items():
    average = calculate_average(grades)
    results.append([name, len(grades), average])

results.sort(key=lambda student: student[2], reverse=True) 
if results:
    best_average = results[0][2]
    best_students = []

    for name, count, average in results:
        if average == best_average:
            best_students.append(name)
    with open("report.txt", "w", encoding="utf-8") as file:
        for name, count, average in results:
            print(
                f"{name} — оцінок: {count} — середній: {average:.2f}",
                file=file
            )
        best_names = " та ".join(best_students)
        print(
            f"найкращмй результат: {best_names} — {best_average:.2f}",
            file=file
        )

